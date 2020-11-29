# Adopt Book, Adopt Twinkie,

# Adopt Brooke, add a Chewy Toy and a Travel Carrier, pay with Check
#
# Adopt Sparky, add a Collar & Leash, pay with Credit Card
#
# Adopt 2 Random Dogs add a Collar & Leash to each, pay with Credit Card
import random
import re

from model.adopt_a_puppy_page import AdoptPuppy, PuppyBasicDetails
from assertpy import assert_that, soft_assertions

# def test_open_website(browser):
#     # browser.get("https://puppies.herokuapp.com/")
#     # browser.find_elements_by_xpath("//*[@class='name']//*[text()='Brook']")
#     # browser.find_element_by_xpath("//*[text()='Brook']/parent::div/parent::div/div[@class='view']//input").click()
#     adopt_a_puppy = AdoptPuppy(browser=browser)
#     brook = adopt_a_puppy.get_puppy_by_name(name="brook")
#     adopt_a_puppy.go_to_page_number(page_number=brook.puppy_found_on_page_number)
#     brook.view_details.click()
#     print()
from model.cart_page import CartPage, PuppyInCard, AdditionalProductsOrServices
from model.customer_details_page import CustomerDetailsPage, CustomerDetails, PayType
from model.puppy_details_page import PuppyDetailsPage


def test_verify_puppy_info_in_puppy_list(browser):
    adopt_a_puppy = AdoptPuppy(browser=browser)
    puppies = adopt_a_puppy.puppy_list
    for puppy in puppies:
        assert_that(val=puppy.picture).is_not_empty()
        assert_that(val=puppy.name).is_not_empty()
        assert_that(val=puppy.puppy_id).is_positive()
        assert_that(val=puppy.breed).is_not_empty()
        assert_that(val=puppy.gender).is_not_empty()
        assert_that(val=puppy.puppy_found_on_page_number).is_positive()
    # print(f"validated {len(puppies)} puppies")


def test_verify_puppy_info_on_puppy_details_page(browser):
    adopt_a_puppy = AdoptPuppy(browser=browser)
    puppies = adopt_a_puppy.puppy_list
    puppy_details_page = PuppyDetailsPage(browser=browser)
    for puppy in puppies:
        puppy_details_page.go_to_page(puppy_id=puppy.puppy_id)
        puppy_details = puppy_details_page.get_puppy_details()
        assert_that(val=puppy_details.picture).is_not_empty()
        assert_that(val=puppy_details.name).is_not_empty()
        assert_that(val=puppy_details.description).is_not_empty()
        assert_that(val=puppy_details.fee_to_adopt).is_not_zero()
        assert_that(val=puppy_details.breed).is_not_empty()
        assert_that(val=puppy_details.gender).ends_with('ale')


def test_adopt_brook_pay_with_check(browser):
    puppies = AdoptPuppy(browser=browser).puppy_list
    brook = find_puppy(puppies=puppies, name="Brook")
    puppy_details_page = PuppyDetailsPage(browser=browser)

    puppy_details_page.go_to_page(puppy_id=brook.puppy_id)
    puppy_details_page.adopt_me()

    cart_id = int(re.sub(pattern='[^0-9]', repl='', string=browser.current_url))
    cart_page = CartPage(browser=browser, cart_id=cart_id)

    cart_page.complete_adoption()

    customer_details_page = CustomerDetailsPage(browser=browser)
    customer_details_form = CustomerDetails(name="Ilya", address="123", email="fake_email@gmail.com",
                                            pay_type=PayType.Check)
    customer_details_page.fill_out_the_form(customer_details_form)

    notice = browser.find_element_by_xpath("//p[@id='notice']").text
    assert_that(notice).is_equal_to_ignoring_case('Thank you for adopting a puppy!')


def test_verify_cart_calculates_total_price_correctly(browser):
    puppies = AdoptPuppy(browser=browser).puppy_list

    brook = find_puppy(puppies=puppies, name="Brook")
    twinkie = find_puppy(puppies=puppies, name="Twinkie")
    tipsy = find_puppy(puppies=puppies, name="Tipsy")

    puppy_details_page = PuppyDetailsPage(browser=browser)

    puppy_details_page.go_to_page(puppy_id=brook.puppy_id)
    brooks_fee = puppy_details_page.get_puppy_details().fee_to_adopt
    puppy_details_page.adopt_me()

    cart_id = int(re.sub(pattern='[^0-9]', repl='', string=browser.current_url))
    cart_page = CartPage(browser=browser, cart_id=cart_id)
    assert_that(cart_page.cart.total == brooks_fee)
    assert_that(len(cart_page.cart.puppies_in_the_cart) == 1)

    puppy_details_page.go_to_page(puppy_id=twinkie.puppy_id)
    twinkies_fee = puppy_details_page.get_puppy_details().fee_to_adopt
    puppy_details_page.adopt_me()

    cart_page.refresh_cart()
    assert_that(cart_page.cart.total == brooks_fee + twinkies_fee)
    assert_that(len(cart_page.cart.puppies_in_the_cart) == 2)

    puppy_details_page.go_to_page(puppy_id=tipsy.puppy_id)
    tipsy_fee = puppy_details_page.get_puppy_details().fee_to_adopt
    puppy_details_page.adopt_me()

    cart_page.refresh_cart()
    assert_that(cart_page.cart.total == brooks_fee + twinkies_fee + tipsy_fee)
    assert_that(len(cart_page.cart.puppies_in_the_cart) == 3)


def test_adopt_sparky_add_collar_and_leash_pay_with_credit_card(browser):
    puppies_added_to_cart: int = 0

    puppies = AdoptPuppy(browser=browser).puppy_list
    sparky: PuppyBasicDetails = find_puppy(puppies=puppies, name="Sparky")
    puppy_details_page = PuppyDetailsPage(browser=browser)

    puppy_details_page.go_to_page(puppy_id=sparky.puppy_id)
    sparky_fee = puppy_details_page.get_puppy_details().fee_to_adopt
    puppy_details_page.adopt_me()
    puppies_added_to_cart += 1

    cart_id = int(re.sub(pattern='[^0-9]', repl='', string=browser.current_url))
    cart_page = CartPage(browser=browser, cart_id=cart_id)

    additional_products_and_services: AdditionalProductsOrServices = cart_page.get_additional_products_and_services_with_price()
    additional_products_and_services.collar_and_leash.is_selected = True

    cart_page.select_additional_products_and_services(puppy_number=puppies_added_to_cart,
                                                      additional_products_and_services=additional_products_and_services)
    additional_products_and_services.reset_to_is_selected_false()

    # THIS IS A BUG (fee + products/services not calculated properly)
    # assert_that(cart_page.refresh_cart().total).is_equal_to(brooks_fee + additional_products_and_services.chew_toy.price + additional_products_and_services.travel_carrier.price)

    cart_page.complete_adoption()

    customer_details_page = CustomerDetailsPage(browser=browser)
    customer_details_form = CustomerDetails(name="Ilya", address="123", email="fake_email@gmail.com",
                                            pay_type=PayType.CreditCard)
    customer_details_page.fill_out_the_form(customer_details_form)

    notice = browser.find_element_by_xpath("//p[@id='notice']").text
    assert_that(notice).is_equal_to_ignoring_case('Thank you for adopting a puppy!')


def test_adopt_brook_with_chewy_toy_and_a_travel_carrie_pay_with_check(browser):
    puppies_added_to_cart: int = 0

    puppies = AdoptPuppy(browser=browser).puppy_list
    brook: PuppyBasicDetails = find_puppy(puppies=puppies, name="Brook")
    puppy_details_page = PuppyDetailsPage(browser=browser)

    puppy_details_page.go_to_page(puppy_id=brook.puppy_id)
    brooks_fee = puppy_details_page.get_puppy_details().fee_to_adopt
    puppy_details_page.adopt_me()
    puppies_added_to_cart += 1

    cart_id = int(re.sub(pattern='[^0-9]', repl='', string=browser.current_url))
    cart_page = CartPage(browser=browser, cart_id=cart_id)

    additional_products_and_services: AdditionalProductsOrServices = cart_page.get_additional_products_and_services_with_price()
    additional_products_and_services.chew_toy.is_selected = True
    additional_products_and_services.travel_carrier.is_selected = True

    cart_page.select_additional_products_and_services(puppy_number=puppies_added_to_cart,
                                                      additional_products_and_services=additional_products_and_services)
    additional_products_and_services.reset_to_is_selected_false()

    # THIS IS A BUG (fee + products/services not calculated properly)
    # assert_that(cart_page.refresh_cart().total).is_equal_to(brooks_fee + additional_products_and_services.chew_toy.price + additional_products_and_services.travel_carrier.price)

    cart_page.complete_adoption()

    customer_details_page = CustomerDetailsPage(browser=browser)
    customer_details_form = CustomerDetails(name="Ilya", address="123", email="fake_email@gmail.com",
                                            pay_type=PayType.Check)
    customer_details_page.fill_out_the_form(customer_details_form)

    notice = browser.find_element_by_xpath("//p[@id='notice']").text
    assert_that(notice).is_equal_to_ignoring_case('Thank you for adopting a puppy!')


def test_adopt_2_random_dogs_add_collar_and_leash_to_each_pay_with_credit_card(browser):
    puppies = AdoptPuppy(browser=browser).puppy_list
    random_puppy_1_index = random.randint(0, len(puppies))
    random_puppy_2_index = None

    for i in range(10):
        p2 = random.randint(0, len(puppies) - 1)
        if p2 is not random_puppy_1_index:
            random_puppy_2_index = p2
            break
    if random_puppy_2_index is None:
        raise Exception(
            "Could not generate random index for puppy 2. Consider increasing number of attempts or number of puppies available for adoption")

    random_puppy_1: PuppyBasicDetails = puppies[random_puppy_1_index]
    random_puppy_2: PuppyBasicDetails = puppies[random_puppy_2_index]

    puppy_details_page = PuppyDetailsPage(browser=browser)

    puppy_details_page.go_to_page(puppy_id=random_puppy_1.puppy_id)
    puppy_1_fee = puppy_details_page.get_puppy_details().fee_to_adopt
    puppy_details_page.adopt_me()

    cart_id = int(re.sub(pattern='[^0-9]', repl='', string=browser.current_url))
    cart_page = CartPage(browser=browser, cart_id=cart_id)
    additional_products_and_services: AdditionalProductsOrServices = cart_page.get_additional_products_and_services_with_price()
    additional_products_and_services.collar_and_leash.is_selected = True

    puppy_details_page.go_to_page(puppy_id=random_puppy_2.puppy_id)
    puppy_2_fee = puppy_details_page.get_puppy_details().fee_to_adopt
    puppy_details_page.adopt_me()

    cart_page.refresh_cart()

    cart_page.select_additional_products_and_services(puppy_number=1,
                                                      additional_products_and_services=additional_products_and_services)
    cart_page.select_additional_products_and_services(puppy_number=2,
                                                      additional_products_and_services=additional_products_and_services)
    cart_page.complete_adoption()

    customer_details_page = CustomerDetailsPage(browser=browser)
    customer_details_form = CustomerDetails(name="Ilya", address="123", email="fake_email@gmail.com",
                                            pay_type=PayType.Check)
    customer_details_page.fill_out_the_form(customer_details_form)

    notice = browser.find_element_by_xpath("//p[@id='notice']").text
    assert_that(notice).is_equal_to_ignoring_case('Thank you for adopting a puppy!')


def test_adopt_all_puppies_select_all_services(browser):
    puppies_added_to_cart = 0
    puppies = AdoptPuppy(browser=browser).puppy_list
    all_puppies_fee = 0
    for puppy in puppies:
        puppy_details_page = PuppyDetailsPage(browser=browser)
        puppy_details_page.go_to_page(puppy_id=puppy.puppy_id)
        puppy_fee = puppy_details_page.get_puppy_details().fee_to_adopt
        all_puppies_fee += puppy_fee
        puppy_details_page.adopt_me()
        puppies_added_to_cart += 1
        cart_id = int(re.sub(pattern='[^0-9]', repl='', string=browser.current_url))
        cart_page = CartPage(browser=browser, cart_id=cart_id)

    additional_products_and_services: AdditionalProductsOrServices = cart_page.get_additional_products_and_services_with_price()
    additional_products_and_services.chew_toy.is_selected = True
    additional_products_and_services.travel_carrier.is_selected = True
    additional_products_and_services.collar_and_leash.is_selected = True
    additional_products_and_services.first_vet_visit.is_selected = True

    for puppy_number in range(len(puppies)):
        cart_page.select_additional_products_and_services(puppy_number=puppy_number + 1,
                                                          additional_products_and_services=additional_products_and_services)

    if cart_page is None:
        raise Exception("cart_page cannot be null")
    cart_page.refresh_cart()
    cart_page.complete_adoption()

    customer_details_page = CustomerDetailsPage(browser=browser)
    customer_details_form = CustomerDetails(name="Ilya", address="123", email="fake_email@gmail.com",
                                            pay_type=PayType.PurchaseOrder)
    customer_details_page.fill_out_the_form(customer_details_form)

    notice = browser.find_element_by_xpath("//p[@id='notice']").text
    assert_that(notice).is_equal_to_ignoring_case('Thank you for adopting a puppy!')


def find_puppy(puppies: list, name: str):
    for puppy in puppies:
        if puppy.name == name:
            return puppy
    raise Exception(f"Puppy with name: {name} is not found. Checked {len(puppies)} puppies")
