import pytest
import pytest_asyncio

from asyncio import get_event_loop
from allure import label
from playwright.async_api import Page, async_playwright

from utils.application import Application

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
    return config_param

@pytest.fixture(scope="session")
def event_loop():
    loop = get_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="session")
async def page(get_param):
    async with async_playwright() as playwright:
        __headless = get_param.get("headless")
        match get_param.get("browser").lower():
            case "chromium":
                chromium = await playwright.chromium.launch(headless=__headless)
                yield await chromium.new_page()
            case "firefox":
                firefox = await playwright.firefox.launch(headless=__headless)
                yield await firefox.new_page()
            case "webkit":
                webkit = await playwright.webkit.launch(headless=__headless)
                yield await webkit.new_page()

@pytest_asyncio.fixture(scope="session")
async def app(page: Page) -> Application:
    return Application(page)

#хук распределения тестов по папкам
def pytest_collection_modifyitems(session, config, items):
    for test_case in items:
        test_case.add_marker(label("layer", "ui")) # AllureTestOps -> Settings -> Test Layers
        test_case.add_marker(label("epic", "Playwright"))
        test_case.add_marker(label("product", "Autotests"))
        test_case.add_marker(label("component", f"UI"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        task = item.funcargs['event_loop'].create_task(item.funcargs['app'].screenshot())
        item.funcargs['event_loop'].run_until_complete(task)
    return rep
