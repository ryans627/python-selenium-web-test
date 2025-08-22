from playwright.sync_api import Page, expect


def test_login_pw(page: Page) -> None:
    page.goto("https://www.baidu.com")
    page.screenshot(path="baidu.png")
    expect(page).to_have_title("百度一下，你就知道") # exact match
