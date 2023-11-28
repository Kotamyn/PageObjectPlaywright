
from utils.base.base_page_interface import BasePage

class HomePage(BasePage):

    locators = {
        "menu_language": "//a[@class='navbar__link']",

        "docs_section": "//div[@class='navbar__items']//a[@href='/docs/intro']",
        "api_section": "//div[@class='navbar__items']//a[@href='/docs/api/class-playwright']",
        "community_section": "//div[@class='navbar__items']//a[@href='/community/welcome']",

        "node.js": "//ul[@class='dropdown__menu']//a[@href='/']",
        "python": "//ul[@class='dropdown__menu']//a[@href='/python/']",
        "java": "//ul[@class='dropdown__menu']//a[@href='/java/']",
        ".net": "//ul[@class='dropdown__menu']//a[@href='/dotnet/']",
    }

    async def open_docs(self):
        await self.click(self.locators.get("docs_section"))
        assert 'docs/intro' in await self.get_url(), "url is not in 'docs/intro'"

    async def open_api(self):
        await self.click(self.locators.get("api_section"))
        assert '/docs/api/class-playwright' in await self.get_url(), "url is not in '/docs/api/class-playwright'"

    async def open_community(self):
        await self.click(self.locators.get("community_section"))
        assert '/community/welcome' in await self.get_url(), "url is not in '/community/welcome'"

    async def select_language(self, language):
        await self.click(self.locators.get("menu_language"))
        await self.click(self.locators.get(language))