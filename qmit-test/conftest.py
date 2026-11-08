import pytest

@pytest.fixture(scope="session", autouse=True)
def set_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-cy")