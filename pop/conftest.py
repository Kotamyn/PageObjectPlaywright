import pytest
import pytest_asyncio
from asyncio import get_event_loop
from allure import label
from playwright.async_api import Page, async_playwright
from pop.utils.application import Application

def pytest_addoption(parser):
    parser.addoption(
        '--brow',
        action="store",
        default='chromium',
        help="Choose browser!",
        choices=("chromium", "firefox", "webkit")
    )
    parser.addoption(
        '--headless',
        action="store",
        default=False,
        help="Choose headless mode!",
        choices=(True, False)
    )

@pytest.fixture(scope="session")
def get_param(request):
    config_param = {}
    config_param["browser"] = request.config.getoption("--brow")
    config_param["headless"] = request.config.getoption("--headless")
    return config_param

@pytest.fixture(scope="session")
def event_loop():
    loop = get_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="function")
async def page(get_param):
    async with async_playwright() as playwright:
        __headless = get_param.get("headless")
        browser_type = get_param.get("browser").lower()
        browser = getattr(playwright, browser_type)
        context = await browser.launch(headless=__headless)
        video_context = await context.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir="videos/",
            record_video_size={"width": 1920, "height": 1080}
        )
        yield await video_context.new_page()
        await video_context.close()
        await context.close()

@pytest_asyncio.fixture(scope="function")
async def app(page: Page) -> Application:
    return Application(page)

def pytest_collection_modifyitems(session, config, items):
    for test_case in items:
        test_case.add_marker(label("layer", "ui"))  # AllureTestOps -> Settings -> Test Layers
        test_case.add_marker(label("epic", "Playwright"))
        test_case.add_marker(label("product", "Autotests"))
        test_case.add_marker(label("component", f"UI"))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        if rep.failed:
            task = item.funcargs['event_loop'].create_task(item.funcargs['app'].screenshot_and_video())
            item.funcargs['event_loop'].run_until_complete(task)
        elif rep.outcome == "passed":
            task = item.funcargs['event_loop'].create_task(item.funcargs['app'].delete_video())
            item.funcargs['event_loop'].run_until_complete(task)
    return rep