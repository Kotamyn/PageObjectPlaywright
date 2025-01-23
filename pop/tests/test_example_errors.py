import pytest
from allure import (
    feature
)

@feature('Example of test case logging with failde status')
class TestErrors:

    @pytest.mark.parametrize("language", [
            "python",
            "node.js"
        ]
    )
    async def test_example_failed_status(self, app, language):
        await app.navigation.open_home()
        await app.home.select_language(language)
        assert 1 == 2, "example"