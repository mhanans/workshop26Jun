from playwright.sync_api import Page, expect


class InventoryPage:
    """Page Object for the demo app's Products page."""

    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Products")
        self.cart_badge = page.get_by_test_id("cart-badge")
        self.search_input = page.get_by_label("Search products")
        self.sort_select = page.get_by_label("Sort by")
        self.logout_btn = page.get_by_role("button", name="Logout")

    def add_to_cart(self, product_name: str):
        self.page.get_by_role("button", name=f"Add {product_name} to cart").click()

    def search(self, term: str):
        self.search_input.fill(term)
        self.search_input.press("Enter")

    def sort_by(self, label: str):
        self.sort_select.select_option(label=label)

    def expect_cart_count(self, count: str):
        expect(self.cart_badge).to_have_text(count)
