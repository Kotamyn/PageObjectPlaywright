from allure import step, attach
from allure_commons.types import AttachmentType
from datetime import datetime

from utils.helpers.navigation import NavigationHelper
from utils.pages.home_page import HomePage

class Application:

    def __init__(self, page):
        self.page = page
        self.navigation = NavigationHelper(self)
        self.home = HomePage(self)

    @step("Screenshot error")
    async def screenshot(self):
        url = self.page.url
        screenshot = await self.page.screenshot()
        attach(
            screenshot,
            name=f"{url}|{datetime.now().strftime('%d.%m.%Y %H:%M')}",
            attachment_type=AttachmentType.PNG
        )
