from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@when('Input {search_word} into search field1')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f"Expected query not in {context.driver.current_url.lower()}"


@then('Verify user can click through color')
def verify_can_click_through_color(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i, color in enumerate(colors[:len(expected_colors)]):
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_colors[i], \
            f'Expected color {expected_colors[i]}, got {current_color}'