"""
Exercises every action from Module 6's cheat-sheet (Click, Fill, Check,
Select, Press key) against the demo app.
"""
import pathlib

from playwright.sync_api import Page, expect

APP_URL = "file:///" + (pathlib.Path(__file__).parent.parent / "index.html").as_posix()


def _login(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()


def test_click(page: Page):
    _login(page)
    page.get_by_role("button", name="Add Backpack to cart").click()
    expect(page.get_by_test_id("cart-badge")).to_have_text("1")


def test_fill(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("standard_user")
    expect(page.get_by_label("Username")).to_have_value("standard_user")


def test_check(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Remember me").check()
    expect(page.get_by_label("Remember me")).to_be_checked()


def test_select_option(page: Page):
    _login(page)
    page.get_by_label("Sort by").select_option(label="Name (Z–A)")
    first_item = page.locator("#product-list li").first
    expect(first_item).to_contain_text("Bike Light")


def test_press_enter_to_search(page: Page):
    _login(page)
    page.get_by_label("Search products").fill("Bike")
    page.get_by_label("Search products").press("Enter")

    expect(page.get_by_text("Bike Light", exact=True)).to_be_visible()
    expect(page.get_by_text("Backpack", exact=True)).to_be_hidden()
