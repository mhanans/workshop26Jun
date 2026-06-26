"""
POM-based refactor of the login tests — see pages/login_page.py and
pages/inventory_page.py. Compare to tests/test_login.py: same behavior,
no inlined locators. Module 7.
"""
import pathlib

from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

APP_URL = "file:///" + (pathlib.Path(__file__).parent.parent / "index.html").as_posix()


def test_valid_login_pom(page: Page):
    login_page = LoginPage(page)
    login_page.goto(APP_URL)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart("Backpack")
    inventory_page.expect_cart_count("1")


def test_locked_out_login_pom(page: Page):
    login_page = LoginPage(page)
    login_page.goto(APP_URL)
    login_page.login("locked_out_user", "secret_sauce")
    login_page.expect_error("Sorry, this user has been locked out.")
