from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.by import By
from behave import given, then

HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.Amazon.com/')


@when('Input coffee into Amazon search')
def input_search(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys()


@when('Click on Amazon search icon')
def click_on_amazon_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


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

