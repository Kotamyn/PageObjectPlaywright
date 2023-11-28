import pytest
import allure

@allure.feature('Home')
@pytest.mark.regress
@pytest.mark.home
class TestHome:

    @allure.title("Open docs")
    async def test_open_docs(self, app):
        await app.navigation.open_home()
        await app.home.open_docs()

    @allure.title("Open api")
    async def test_open_api(self, app):
        await app.navigation.open_home()
        await app.home.open_api()

    @allure.title("Open community")
    async def test_open_community(self, app):
        await app.navigation.open_home()
        await app.home.open_community()

    @allure.title("Select language")
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
