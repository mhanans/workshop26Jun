"""
Basic functional tests for index.html — companion to Modules 4-6 of the
"Playwright for Everyone" workshop.

Run with:
    pip install -r requirements.txt
    playwright install chromium
    pytest tests/test_login.py --headed
"""
import pathlib
import re

from playwright.sync_api import Page, expect

APP_URL = "file:///" + (pathlib.Path(__file__).parent.parent / "index.html").as_posix()


def test_login_success(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(re.compile(r"#/inventory\.html$"))
    expect(page.get_by_role("heading", name="Products")).to_be_visible()


def test_login_locked_out_shows_error(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("locked_out_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Sorry, this user has been locked out.")).to_be_visible()
    expect(page.get_by_role("heading", name="Products")).not_to_be_visible()


def test_login_invalid_credentials_shows_error(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("nobody")
    page.get_by_label("Password").fill("wrong-password")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Username and password do not match.")).to_be_visible()


def test_add_to_cart_updates_badge(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="Add Backpack to cart").click()
    expect(page.get_by_test_id("cart-badge")).to_have_text("1")

    page.get_by_role("button", name="Add Bike Light to cart").click()
    expect(page.get_by_test_id("cart-badge")).to_have_text("2")


def test_logout_resets_cart_and_returns_to_login(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Add Backpack to cart").click()

    page.get_by_role("button", name="Logout").click()

    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page).to_have_url(re.compile(r"#/login\.html$"))
