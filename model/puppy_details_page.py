import re

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement


class PuppyDetails:
    def __init__(self, picture, name, gender, breed, description, fee_to_adopt):
        self.picture = picture
        self.name = name
        self.gender = gender
        self.breed = breed
        self.description = description
        self.fee_to_adopt = fee_to_adopt


class PuppyDetailsPage:
    def __init__(self, browser: RemoteWebDriver):
        self.browser = browser

    def go_to_page(self, puppy_id: int):
        self.browser.get(f"https://puppies.herokuapp.com/puppies/{puppy_id}?")

    def adopt_me(self):
        adopt_me_btn = self.browser.find_element_by_xpath("//input[@value='Adopt Me!']")
        adopt_me_btn.click()

    def return_to_list(self):
        return_to_list_btn = self.browser.find_element_by_xpath("//a[contains(text(), 'Return')]")
        return_to_list_btn.click()

    def get_puppy_details(self):
        picture = self.browser.find_element_by_xpath("//div[@class='fees_line']/parent::div//img")
        name = self.browser.find_element_by_xpath("//div[@class='fees_line']/parent::div/h2")
        gender_and_breed = self.browser.find_element_by_xpath("//div[@class='fees_line']/parent::div/h3").text
        breed = gender_and_breed[gender_and_breed.find(" "):]
        gender = gender_and_breed[0:gender_and_breed.find(" ")]
        fee_to_adopt = self.browser.find_element_by_xpath("//div[@class='fees_line']/span")
        description = self.browser.find_element_by_xpath("//div[@class='fees_line']/parent::div/p")
        fee_to_adopt = re.sub(pattern='[^0-9.]', repl='', string=fee_to_adopt.text)

        puppy_details = PuppyDetails(picture=picture.get_attribute(name="src"), name=name.text, gender=gender,
                                     breed=breed, fee_to_adopt=float(fee_to_adopt), description=description.text)

        return puppy_details
