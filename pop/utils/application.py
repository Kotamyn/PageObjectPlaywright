import os

from allure import step, attach, attachment_type
from datetime import datetime

from pop.utils.helpers.navigation import NavigationHelper
from pop.utils.pages.home_page import HomePage

class Application:

    def __init__(self, page):
        self.page = page
        self.navigation = NavigationHelper(self)
        self.home = HomePage(self)

    @step("Screenshot error")
    async def screenshot_and_video(self) -> None:
        url = self.page.url
        screen = await self.page.screenshot()
        with step("Screenshot error"):
            attach(
                screen,
                name=f"{url}|{datetime.now().strftime('%d.%m.%Y %H:%M')}",
                attachment_type=attachment_type.PNG
            )
        with step("Video error"):
            video_path = await self.page.video.path()
            await self.page.context.close() # Recording is finalized
            with open(video_path, "rb") as video_file:
                attach(
                    video_file.read(),
                    name=f"{url}|video",
                    attachment_type=attachment_type.WEBM
                )

    async def delete_video(self) -> None:
        video_path = await self.page.video.path()
        if os.path.exists(video_path):
            os.remove(video_path)
