from playwright.sync_api import sync_playwright

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.error_message = self.page.locator("[data-test='error']")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

#test-cases:
#Positive
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in page.url, f"Pass URL: {page.url}"
    #late
    page.wait_for_timeout(3000)

#negative:
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.saucedemo.com/')
    login_page = LoginPage(page)
    login_page.login("standard_user", "password")
    assert login_page.error_message.is_visible(), "Neggative pass!."
    #late
    page.wait_for_timeout(3000)