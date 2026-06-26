"""
Intentionally-failing test for practicing Module 6's debugging techniques.
This is the one test in this folder that's SUPPOSED to fail — use it to try:

    pytest tests/test_debug_me.py --headed
    pytest tests/test_debug_me.py --tracing=on   (then: playwright show-trace trace.zip)

Or open this file and drop `page.pause()` on the line right before the
failing click to step through it live in the Playwright Inspector.
"""
import pathlib

from playwright.sync_api import Page

APP_URL = "file:///" + (pathlib.Path(__file__).parent.parent / "index.html").as_posix()


def test_login_with_wrong_button_name_fails_on_purpose(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    # Deliberately wrong accessible name — no button on this page is called
    # "Sign In", so this times out. Use the techniques above to find out why.
    page.get_by_role("button", name="Sign In").click()
