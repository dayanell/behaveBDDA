from behave import given, when, then
from page_objects.signin_page import SignInPage
from page_objects.user_home_page import UserHomePage


@given('the user navigate to conduit sign-in page')
def step_impl(context):
    context.signin = SignInPage(context.driver)
    context.signin.open_url()


@given('The user validate the page title')
def step_impl(context):
    title = context.driver.title
    assert "Conduit" in title, "The title is incorrect"


@when('the user fills in the form with "{email}" "{password}"')
def step_impl(context, email, password):
    context.signin.type_email(email)
    context.signin.type_password(password)
    context.signin.click_submit_button()


@then('the user should see "{username}" on the page')
def step_impl(context, username):
    context.user_home = UserHomePage(context.driver)
    username_element = context.user_home.user_identification()
    assert username_element == username, f"Expected username: {username}, Actual username: {username_element}"


@then('the user should see error message on the page')
def step_impl(context):
    error_message = context.signin.error_message_is_displayed()
    assert error_message is True, "The error message was not displayed"
