import pytest
import allure
from allure import (
    title,
    feature,
    tag,
    severity,
    severity_level
)

@feature('Home')
@pytest.mark.regress
@pytest.mark.home
class TestHome:

    @title("Open docs")
    @tag("positive")
    @severity(severity_level.NORMAL)
    async def test_open_docs(self, app):
        await app.navigation.open_home()
        await app.home.open_docs()

    @title("Open api")
    @tag("positive")
    @severity(severity_level.NORMAL)
    async def test_open_api(self, app):
        await app.navigation.open_home()
        await app.home.open_api()

    @title("Open community")
    @tag("positive")
    @severity(severity_level.NORMAL)
    async def test_open_community(self, app):
        await app.navigation.open_home()
        await app.home.open_community()

    @title("Select language -> {language}")
    @tag("positive")
    @severity(severity_level.NORMAL)
    @pytest.mark.parametrize("language", [
            "python",
            "node.js",
            "java",
            ".net"
        ]
    )
    async def test_select_language(self, app, language):
        await app.navigation.open_home()
        await app.home.select_language(language)
