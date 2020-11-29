import re

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class Cart:
    def __init__(self, puppies_in_the_cart, total):
        self.puppies_in_the_cart = puppies_in_the_cart
        self.total = total


class AdditionalProductOrService:
    def __init__(self, name: str, price: float, is_selected: bool):
        self.name = name
        self.price = price
        self.is_selected = is_selected


# Assumption: products and services stay the same but their price can change day over day
class AdditionalProductsOrServices:
    def __init__(self, collar_and_leash: AdditionalProductOrService, chew_toy: AdditionalProductOrService,
                 travel_carrier: AdditionalProductOrService, first_vet_visit: AdditionalProductOrService):
        self.collar_and_leash = collar_and_leash
        self.chew_toy = chew_toy
        self.travel_carrier = travel_carrier
        self.first_vet_visit = first_vet_visit

    def reset_to_is_selected_false(self):
        self.collar_and_leash.is_selected = False
        self.chew_toy.is_selected = False
        self.travel_carrier.is_selected = False
        self.first_vet_visit.is_selected = False


class PuppyInCard:

    def __init__(self, picture, name, gender, breed, fee_to_adopt):
        self.picture = picture
        self.name = name
        self.gender = gender
        self.breed = breed
        self.fee_to_adopt = fee_to_adopt


class CartPage:
    def __init__(self, browser: RemoteWebDriver, cart_id: int):
        self.browser = browser
        self.cart_id = cart_id
        self.go_to()
        self.cart = self.__collect_cart_data()

    def go_to(self):
        self.browser.get(f"https://puppies.herokuapp.com/carts/{self.cart_id}")

    def refresh_cart(self):
        self.cart = self.__collect_cart_data()
        return self.cart

    def __collect_cart_data(self):
        total = self.browser.find_element_by_xpath("//tr[@class='total_line']//td[@class='total_cell']//h2").text
        total = float(re.sub(pattern='[^0-9.]', repl='', string=total))
        number_of_lines_in_table_cart = len(
            self.browser.find_elements_by_xpath("//td[@class='item_price']/ancestor::tbody/tr"))
        number_of_puppies_in_table_cart = len(self.browser.find_elements_by_xpath("//td[@class='item_price']"))
        puppies_in_the_cart = []
        if (number_of_puppies_in_table_cart * 6) + 1 == number_of_lines_in_table_cart:
            for puppy_number_in_table_cart in range(1, number_of_puppies_in_table_cart + 1):
                starting_line_for_puppy = CartPage.__get_starting_line_for_puppy(
                    puppy_number=puppy_number_in_table_cart)
                picture = self.browser.find_element_by_xpath(
                    f"//td[@class='item_price']/ancestor::tbody//tr[{starting_line_for_puppy}]//td[1]//img").get_attribute(
                    name="src")
                name = self.browser.find_element_by_xpath(
                    f"//td[@class='item_price']/ancestor::tbody//tr[{starting_line_for_puppy}]//td[2]").text
                name = name.replace(":", "")
                gender_and_breed = self.browser.find_element_by_xpath(
                    f"//td[@class='item_price']/ancestor::tbody//tr[{starting_line_for_puppy}]//td[3]").text
                gender = gender_and_breed.split("-")[0].strip()
                breed = gender_and_breed.split("-")[1].strip()
                fee_to_adopt = self.browser.find_element_by_xpath(
                    f"//td[@class='item_price']/ancestor::tbody//tr[{starting_line_for_puppy}]//td[4]").text
                fee_to_adopt = float(fee_to_adopt.replace("$", "").strip())
                puppy_in_cart = PuppyInCard(picture=picture, name=name, gender=gender, breed=breed,
                                            fee_to_adopt=fee_to_adopt)
                puppies_in_the_cart.append(puppy_in_cart)
            cart = Cart(puppies_in_the_cart=puppies_in_the_cart, total=total)
            return cart
        else:
            raise Exception(
                f"The number of puppies: {number_of_puppies_in_table_cart} in the cart does not match expected number of lines: {number_of_lines_in_table_cart} in a table")

    @staticmethod
    def __get_starting_line_for_puppy(puppy_number: int):
        default_number_of_products_and_services = 6
        if puppy_number == 1:
            return 1
        else:
            return (puppy_number - 1) * default_number_of_products_and_services + 1

    # def get_number_of_puppies_in_the_card(self):
    #      number_of_puppies = self.browser.find_elements_by_xpath("//div[@class = 'puppy_list']")
    #         return len(number_of_puppies)

    def complete_adoption(self):
        complete_adoption_btn = self.browser.find_element_by_xpath("//input[@value='Complete the Adoption']")
        complete_adoption_btn.click()

    def add_another_puppy(self):
        add_another_adoption_btn = self.browser.find_element_by_xpath("//input[@value='Adopt Another Puppy']")
        add_another_adoption_btn.click()

    def change_you_mind(self):
        change_your_mind_btn = self.browser.find_element_by_xpath("//input[@value='Change your mind']")
        change_your_mind_btn.click()

    def get_additional_products_and_services_with_price(self):
        #     return AdditionalProductsOrServices

        collar_and_leash_price = self.browser.find_element_by_xpath(
            xpath="//tbody/tr[3]//input[@type='checkbox']/parent::td").text
        chew_toy_price = self.browser.find_element_by_xpath(
            xpath="//tbody/tr[4]//input[@type='checkbox']/parent::td").text
        travel_carrier_price = self.browser.find_element_by_xpath(
            xpath="//tbody/tr[5]//input[@type='checkbox']/parent::td").text
        first_vet_visit_price = self.browser.find_element_by_xpath(
            xpath="//tbody/tr[6]//input[@type='checkbox']/parent::td").text

        collar_and_leash_price = float(re.sub(pattern='[^0-9.]', repl='', string=collar_and_leash_price))
        chew_toy_price = float(re.sub(pattern='[^0-9.]', repl='', string=chew_toy_price))
        travel_carrier_price = float(re.sub(pattern='[^0-9.]', repl='', string=travel_carrier_price))
        first_vet_visit_price = float(re.sub(pattern='[^0-9.]', repl='', string=first_vet_visit_price))

        collar_and_leash = AdditionalProductOrService(name="Collar & Leash", is_selected=False,
                                                      price=collar_and_leash_price)
        chew_toy = AdditionalProductOrService(name="Chew Toy", is_selected=False, price=chew_toy_price)
        travel_carrier = AdditionalProductOrService(name="Travel Carrier", is_selected=False,
                                                    price=travel_carrier_price)
        first_vet_visit = AdditionalProductOrService(name="First Vet Visit", is_selected=False,
                                                     price=first_vet_visit_price)

        additional_products_and_services = AdditionalProductsOrServices(collar_and_leash=collar_and_leash,
                                                                        chew_toy=chew_toy,
                                                                        travel_carrier=travel_carrier,
                                                                        first_vet_visit=first_vet_visit)
        return additional_products_and_services

    def select_additional_products_and_services(self, puppy_number: int,
                                                additional_products_and_services: AdditionalProductsOrServices):
        # find puppy
        starting_line_for_puppy = self.__get_starting_line_for_puppy(puppy_number=puppy_number)

        if additional_products_and_services.collar_and_leash.is_selected is True:
            line_number: int = starting_line_for_puppy + 2
            self.browser.find_element_by_xpath(xpath=f"//tbody/tr[{line_number}]//input").click()
        if additional_products_and_services.chew_toy.is_selected is True:
            line_number: int = starting_line_for_puppy + 3
            self.browser.find_element_by_xpath(xpath=f"//tbody/tr[{line_number}]//input").click()
        if additional_products_and_services.travel_carrier.is_selected is True:
            line_number: int = starting_line_for_puppy + 4
            self.browser.find_element_by_xpath(xpath=f"//tbody/tr[{line_number}]//input").click()
        if additional_products_and_services.first_vet_visit.is_selected is True:
            line_number: int = starting_line_for_puppy + 5
            self.browser.find_element_by_xpath(xpath=f"//tbody/tr[{line_number}]//input").click()
