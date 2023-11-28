from playwright.async_api import expect

from allure import step

class BasePage:

    def __init__(self, app):
        self.app = app

    async def open(self, url: str) -> None:
        with step(f'Opening the url "{url}"'):
            await self.app.page.goto(url)#, wait_until='networkidle')
   
    async def reload(self) -> None:
        with step(f'Reloading page with url "{self.app.page.url}"'):
            await self.app.page.reload(wait_until='domcontentloaded')

    async def click(self, locator: str) -> None:
        with step(f'Click element "{locator}"'):
            await self.app.page.locator(locator).click()

    async def fill(self, locator: str, fill: str) -> None:
        with step(f'Fill element "{locator}"'):
            await self.app.page.locator(locator).fill(fill)

    async def keyboard_press(self, keyboard: str) -> None:
        with step(f'Press keyboard "{keyboard}"'):
            await self.app.page.keyboard.press(keyboard)

    async def mouse_hover(self, locator: str) -> None:
        with step(f'Mouse hover "{locator}"'):
            element =  await self.app.page.query_selector(locator)
            await element.hover()
            
    async def get_url(self) -> str:
        return self.app.page.url

    async def get_text_element(self, locator: str) -> str:
        return await self.app.page.locator(locator).text_content()

    async def expect_contain_text(self, locator: str, text: str) -> expect:
        await expect(locator).to_contain_text(text)
