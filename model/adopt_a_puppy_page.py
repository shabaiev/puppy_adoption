from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
import re


class PuppyBasicDetails(object):
    def __init__(self, picture, name, breed, gender, view_details_btn: WebElement, puppy_found_on_page_number=None, puppy_id=None):
        self.picture = picture
        self.name = name
        self.breed = breed
        self.gender = gender
        self.view_details_btn = view_details_btn
        self.puppy_found_on_page_number = puppy_found_on_page_number
        self.puppy_id = puppy_id

class AdoptPuppy:
    def __init__(self, browser: RemoteWebDriver):
        self.browser = browser
        self.go_to()
        self.puppy_list = self.collect_puppies()

    def get_puppy_by_name(self, name: str):
        for puppy in self.puppy_list:
            if puppy.name.lower() == name.lower():
                return puppy

    def go_to(self):
        self.browser.get("https://puppies.herokuapp.com/")

    def go_to_page_number(self, page_number: int):
        url = "https://puppies.herokuapp.com/agency/index?page="
        self.browser.get(url + str(page_number))

    def collect_puppies(self):
        number_of_pages = int(self.get_number_of_pages())
        # brook = PuppyBasicDetails(picture="/assets/Brook-ed6c0be3a8830921c5a954d1bc283354.jpg", name="Brook",
        #                           breed="Golden Retriever", gender="Female", view_details="")
        puppies = []
        for page_number in range(1, number_of_pages + 1):
            self.go_to_page_number(page_number)
            number_of_puppies_on_the_page = self.get_number_of_puppies_on_the_page()
            for puppy_number in range(1, number_of_puppies_on_the_page + 1):
                puppy = self.get_puppy(puppy_number=puppy_number)
                puppy.puppy_found_on_page_number = page_number
                puppy_id = self.get_puppy_id(view_details_btn=puppy.view_details_btn)
                puppy.puppy_id = puppy_id
                puppies.append(puppy)
        return puppies

    def get_puppy_id(self, view_details_btn: WebElement):
        view_details_btn.click()
        url = self.browser.current_url
        url = re.sub(pattern='[^0-9]', repl='', string=url)
        self.browser.back()
        return int(url)

    def get_number_of_pages(self):
        last_page = self.browser.find_element_by_xpath(
            "//*[contains(text(),'Next')]/parent::div/a[position() = (last()-1)]")
        return last_page.text

    def get_number_of_puppies_on_the_page(self):
        number_of_puppies = self.browser.find_elements_by_xpath("//div[@class = 'puppy_list']")
        return len(number_of_puppies)

    def get_puppy(self, puppy_number):
        picture = self.browser.find_element_by_xpath(f"//div[@class = 'puppy_list'][{puppy_number}]//img")
        name = self.browser.find_element_by_xpath(f"//div[@class = 'puppy_list'][{puppy_number}]//div[@class='name']")
        breed = self.browser.find_element_by_xpath(
            f"//div[@class = 'puppy_list'][{puppy_number}]//div[@class='details']/h4[1]")
        gender = self.browser.find_element_by_xpath(
            f"//div[@class = 'puppy_list'][{puppy_number}]//div[@class='details']/h4[2]")
        view_details = self.browser.find_element_by_xpath(
            f"//div[@class = 'puppy_list'][{puppy_number}]//div[@class='view']//input")

        puppy = PuppyBasicDetails(picture=picture.get_attribute(name="src"), name=name.text, breed=breed.text,
                                  gender=gender.text, view_details_btn=view_details)

        return puppy
