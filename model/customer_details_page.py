from enum import Enum

from selenium.webdriver.android.webdriver import WebDriver


class PayType(Enum):
    Check = "Check",
    CreditCard = "Credit card",
    PurchaseOrder = "Purchase order"


class CustomerDetails:
    def __init__(self, name: str, address: str, email: str, pay_type: PayType):
        self.name = name
        self.address = address
        self.email = email
        self.pay_type = pay_type


class CustomerDetailsPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def fill_out_the_form(self, customer_details_form: CustomerDetails):
        # set name
        self.browser.find_element_by_xpath("//div[@class = 'puppy_form']//input[@id='order_name']").send_keys(customer_details_form.name)
        # set address
        self.browser.find_element_by_xpath("//div[@class = 'puppy_form']//textarea[@id='order_address']").send_keys(customer_details_form.address)
        # set email
        self.browser.find_element_by_xpath("//div[@class = 'puppy_form']//input[@id='order_email']").send_keys(customer_details_form.email)
        # set payType
        self.browser.find_element_by_xpath("//div[@class = 'puppy_form']//select[@id='order_pay_type']/option[text()='Check']").click()
        # sekect from drop down


        # click Place Order
        self.browser.find_element_by_xpath("//div[@class = 'actions']//input[@name='commit']").click()

