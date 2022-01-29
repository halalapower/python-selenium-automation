
from behave import given, then
from behave import when
from selenium.webdriver.common.by import By

HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.main_page.open_main_page()


@when('Input {search_word} into Amazon search')
def input_search(context, search_word):
    context.app.header.input_search(search_word)

@when('Click on Amazon search icon')
def click_on_amazon_search_icon(context):
    context.app.header.click_search()


@then('Verify hamburger menu is present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_ICON)

@given ('Open Amazon product {product_id} page')
def open_amazon_product(context,product_id):
    context.driver.get('https://www.amazon.com/Paitluc-Womens-Blouse-Blouses-Women/dp/B08ZSG769Z')

@then ('Verify user can click through color')
def verify_can_loop_through_colors(context):
    expected_color = []
    color_web_elements = context.driver.find_element(By.CSS_SELECTOR, ".a-form-label")


@then('Verify {expected_result} text is shown')
def verify_text_is_shown(context, expected_result):
    context.app.search_results_page.verify_search_result_text(expected_result)