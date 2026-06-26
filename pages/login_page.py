from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the demo app's login screen. See Module 7 — locators
    live here, in __init__. Tests call methods, never touch locators directly."""

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.remember_me = page.get_by_label("Remember me")
        self.login_btn = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_role("alert")

    def goto(self, url: str):
        self.page.goto(url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def expect_error(self, text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(text)
