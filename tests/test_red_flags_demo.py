"""
Side-by-side demonstrations of Module 5's three red flags, run against the
SAME app. Every 'bad' test below still passes today — that's the whole
danger: it looks fine until the markup changes or the timing shifts.
"""
import pathlib
import re

from playwright.sync_api import Page, expect

APP_URL = "file:///" + (pathlib.Path(__file__).parent.parent / "index.html").as_posix()


def _login(page: Page):
    page.goto(APP_URL)
    page.get_by_label("Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()


# ---------------------------------------------------------------------------
# Red Flag #1 — Brittle XPath
# ---------------------------------------------------------------------------
def test_red_flag_1_bad_brittle_css_path(page: Page):
    """BAD: walks the exact wrapper-<div> structure around the Backpack
    button. Delete one of those wrapper divs in index.html and this breaks —
    nothing else here needs to change for that to happen."""
    _login(page)
    btn = page.locator(
        "#product-list li:nth-child(1) div div section div span button"
    )
    btn.click()
    expect(page.get_by_test_id("cart-badge")).to_have_text("1")


def test_red_flag_1_good_get_by_role(page: Page):
    """GOOD: targets role + accessible name. Survives any wrapper change."""
    _login(page)
    page.get_by_role("button", name="Add Backpack to cart").click()
    expect(page.get_by_test_id("cart-badge")).to_have_text("1")


# ---------------------------------------------------------------------------
# Red Flag #2 — Hardcoded Sleep
# ---------------------------------------------------------------------------
def test_red_flag_2_bad_hardcoded_sleep(page: Page):
    """BAD: blind 2-second wait, even though the page reacts instantly."""
    _login(page)
    page.wait_for_timeout(2000)  # never do this — see Module 5
    page.get_by_role("button", name="Add Backpack to cart").click()
    expect(page.get_by_test_id("cart-badge")).to_have_text("1")


def test_red_flag_2_good_web_first_assertion(page: Page):
    """GOOD: waits only as long as actually needed (milliseconds here)."""
    _login(page)
    btn = page.get_by_role("button", name="Add Backpack to cart")
    expect(btn).to_be_visible()
    btn.click()
    expect(page.get_by_test_id("cart-badge")).to_have_text("1")


# ---------------------------------------------------------------------------
# Red Flag #3 — Missing Assertion
# ---------------------------------------------------------------------------
def test_red_flag_3_bad_no_assertion(page: Page):
    """BAD: clicks Login but never checks it actually worked. This 'test'
    passes whether login succeeds, fails, or the page is broken."""
    _login(page)
    # ... test ends here. No expect(). No assert.


def test_red_flag_3_good_explicit_assertion(page: Page):
    """GOOD: states exactly what success means — fails loudly if it isn't true."""
    _login(page)
    expect(page).to_have_url(re.compile(r"#/inventory\.html$"))
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
