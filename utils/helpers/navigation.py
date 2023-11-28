from utils.base.base_page_interface import BasePage

class NavigationHelper(BasePage):
    
    async def open_home(self) -> None:
        await self.open("https://playwright.dev/")

    async def refresh_page(self):
        await self.reload()