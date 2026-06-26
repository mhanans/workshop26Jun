"""
Standalone Hello World — companion to Module 4 (Playwright Core Concepts).
No pytest here, just the raw sync API, so the Browser -> Context -> Page
tiers are visible in the code.

Run with: python hello_world.py
"""
import pathlib
from playwright.sync_api import sync_playwright

APP_URL = "file:///" + (pathlib.Path(__file__).parent / "index.html").as_posix()

with sync_playwright() as p:
    # 1. Launch Browser (Tier 1)
    browser = p.chromium.launch(headless=False)

    # 2. Open Context (Tier 2)
    context = browser.new_context()

    # 3. Open Tab (Tier 3)
    page = context.new_page()

    # 4. Action
    page.goto(APP_URL)
    print(page.title())  # "Demo App — Playwright Workshop"

    # 5. Cleanup (automatic via 'with')
    browser.close()
