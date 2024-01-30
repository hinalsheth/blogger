from random import randint
from playwright.sync_api import expect


def test_blog_post_form_with_login(page):
    # Login
    page.goto("http://localhost:8000/login/")

    page.get_by_label("Username:").fill("admin")
    page.get_by_label("Password:").fill("admin")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="Logout").wait_for()
    expect(page.get_by_text("Submit New Post")).to_be_visible()

    # Submit new post
    page.goto("http://localhost:8000/submit/")

    title = f"Test Post Title {str(randint(0, 10**10))}"
    content = f"This is test post content {str(randint(0, 10**10))}"

    # Fill the blog post form and submit as before
    page.get_by_label("Title:").fill(title)
    page.get_by_label("Content:").fill(content)
    page.get_by_role("button", name="Submit Post").click()

    # Add assertions to verify the form submission was successful
    assert page.url == "http://localhost:8000/"

    expect(page.get_by_text("Blog Posts")).to_be_visible()
    expect(page.get_by_text(title)).to_be_visible()
    expect(page.get_by_text(content)).to_be_visible()

    # Logout
    page.get_by_role("button", name="Logout").click()

    expect(page.get_by_text("Login")).to_be_visible()
