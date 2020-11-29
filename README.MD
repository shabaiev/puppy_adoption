#### Use Cases for Adopt puppy process
+ Adopt Puppy page
    + User should be able to see that every puppy has Name, Breed, Gender, Image on Adopt Puppy page
    + User should be able to see that every puppy has Name, Breed, Gender, Image on Adopt Puppy page
    + By clicking on "View Details" button user navigates to the page with a puppy description and able to see the puppy unique number in the link
+ Puppy Details page
    + User should be able to see Picture, Name, Breed, Description on Puppy details page
    + User should be able to see "Adopt me!" and "Return to List" buttons
    + User should be taken to his cart by clicking Adopt me buttons
+ Cart page
    + User should be able to see "Your Litter" words above the puppy info on the cart page
    + User should be able to see picture, Name, Gender, Breed, and adoption fee for the selected on "Your Litter" page
    + User should be able to see the name of additional products and services and feed for each product or service
    + User should be able to see a price that includes summary of adoptions fee of the puppies(puppies) and additinal product(s) or service(s) in "Total"
    + Each time when the user creates a new cart, the cart should have unique digits at the end of the URL
    + User should be able to adopt a puppy without selecting any additional products and service
    + User should be able to adopt several puppies without selecting any additional products and services
    + User should be able to adopt all existing puppies on a website without selecting any additional products and services
    + User should be able to adopt a puppy by selecting only one item from additional products and service (ex Chew Toy)
    + User should be able to adopt several puppies by selecting only one item from additional products and service (ex Chew Toy) for each puppy
    + User should be able to adopt all existing puppies on a by selecting only one item from additional products and service (ex Chew Toy) for each puppy
    + User should be able to adopt several puppies with selecting different additional products and service for each puppy
    + User should be able to see 3 buttons on "Your Litter" cart page: "Complete the Adoption", "Adopt Another Puppy", "Change Your Mind"
    + User should be able to add another puppy to the cart by clicking on "Adopt Another Puppy" button
    + User should be able to cancel cart by clicking "Change Your Mind" button
    + User should be able to go to the payment details page by "Complete the Adoption" button
+ Customer details page
    + User should be able to see "Please Enter Your Details" words above the all the input fields
    + User should be able to enter required info in the following fields Name, Address, Email on the payment details page
    + User should be able to locate and click on "Pay type" drop-down and select one of the options (Check, Credit Card, Purchase Order)
    + Verify that the name input field should accept only characters (ex "Illia")
    + Verify that the name input field is not case-sensitive and accepts both lowercase and uppercase characters (ex "Bob", "bob")
    + Verify that Address input accepts both digits and characters (ex "123 Main st")
    + Verify that the name input field is not case-sensitive and accepts both lowercase and uppercase characters (ex ex "123 Main st","123 main st", "123 MAIN ST")
    + Verify that the email input field should accept only standard email syntax at the end ex ("@gmail.com")
    + Verify that the email input should accept alphabetic characters or digits before the email syntax 
    + User should be able to complete the adoption process by clicking on "Place order" button

###Bug Report 
######Bug id: #001

###Summary: "Poppy Adoption Agency" home button doesn't function
 
 
####Steps to reproduce:
   1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
   2. Click on "Poppy Adoption Agency" button in left right corner of the main page

####Expected result:
    Button click should refresh the page when user is on the main page or return user on the main page if user is on a different page of the website
####Actual results:
    Button click returns the error “The page you were looking for doesn’t exist” on UI and 404 error for html file

####Screenshots:
screen_shot_1.1
![](https://i.ibb.co/7ncs2CD/1-1.png)
screen_shot_1.2
![](https://i.ibb.co/C8P5ydc/1-2.png)


 
######Bug id: #002

###Summary: All the buttons on the menu are disabled (Besides “Adopt Puppy”)

####Steps to reproduce:
   1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
   2. Click on each button that is located below “Adopt puppy” button

####Expected result:
    Each button should take the user to the url that it was linked with 
####Actual results:
    Click on the button returns “The site can’t be reached” error
####Screenshots:
screen_shot_2
 ![](https://i.ibb.co/sbYMFxx/2.png)
    
######Bug id: #003

###Summary: The "Mail" icon is not functional

Steps to reproduce:
    1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
    2. Locate the “Mail” icon in the right top corner of the main page and click on it

####Expected result:
    Main icon should open your email and create email addressed to the customer support of the website
####Actual results:
    The click on the icon returns “The page you were looking for doesn’t exist”
####Screenshots:
screen_shot_3:
![](https://i.ibb.co/yFVKtCF/3.png)

######Bug id: #004

###Summary: User is not able to enter any input data in a search field

####Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Locate the search field in the right top corner of the main page and enter the word or number in it
3. Click on “magnifying glass” icon located in the search or press the Enter(return) button on your keyboard”.

####Expected result:
    The results of search word or number should be displayed
####Actual results:
    The input data can not be send
####Screenshots:
screen_shot_4
![](https://i.ibb.co/XSQcg6V/4.png)

######Bug id: #005

###Summary:: After selecting additional products, user get incorrect amount for total

Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Locate the list of puppies 
3. Locate “View Details” that locates next to the puppy (can be any puppy)
4. Click on “View Details” button
5. When the detail page opens, click on “Adopt me” button
6. Select one or several items from Additional Products/Service
Expected result:
The price should be accurate (Summary of Adoption price and Additional/Service(s))
Actual results:
The calculation returns incorrect number
Screenshots:
screen_shot_5
![](https://i.ibb.co/TKcLjtz/5.png)

######Bug id: #006

###Summary: After clicking "Change your mind" button, user need to click twice (on either "Cancel" or "OK") in order for pop-up window to disappear

####Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Locate the list of puppies 
3. Locate “View Details” that locates next to the puppy (can be any puppy)
4. Click on “View Details” button
5. When the detail page opens, click on “Adopt me” button
6. Locate and click on “Change your mind” button
7. Click “Cancel” or “Ok” on a pop-up window

####Expected result:
    The pop-up window should disappear after clicking on of the buttons on it (“Cancel” or “Ok”)
####Actual results:
    The window pops up second time after user clicks on a button in a window
####Screenshots:
   screen_shot_6:
 ![](https://i.ibb.co/rwVW04K/6.png)
######Bug id: #007

###Summary: The message above the puppy list on a main page has a typo "Your car is currently empty".

####Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Choose one of the puppies from the list and click on the button “View Details”
3. Click on “Adopt me!” button on the puppy details page
4. Click on “Change your mind button” on “Your Litter” page 
5. Click on “Ok” button in pop-up window 


####Expected result:
    Massage should say “Your cart is currently empty”
####Actual results:
    Massage says “Your car is currently empty”
####Screenshots:
 screen_shot_7:
![](https://i.ibb.co/fdBKph4/7.png)

######Bug id: #008

###Summary: The puppy that is already in a cart does not disappear from the list and error does not pop up when the user selects the same puppy that he already has in his cart

Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Choose specific puppy (ex Hanna2) from the list and click on the button “View Details”
3. Click on “Adopt me!” button on the puppy details page
4. Click on “Adopt another puppy” on “Your Litter” page
5. Choose the same puppy that is already on “Your Litter” page (ex Hanna2) from the list and click on the button “View Details”

####Expected result:
    Selected puppy should disappear from the list or used should ge and error while attempting to select the same puppy second time
####Actual results:
    Selected previously puppy does not disappear from the list and the error dose not pop up while user is selecting the same puppy twice
####Screenshots:
screen_shot_8_1
![](https://i.ibb.co/bP5VFXd/8-1.png)
screen_shot_8_2
![](https://i.ibb.co/NKH6KW4/8-2.png)


######Bug id: #009

###Summary: After the adoption process has been completed, the message always says "Thank you for adopting a puppy!", even if the user adopted several puppies.

####Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Choose any from the list and click on the button “View Details”
3. Click on “Adopt me!” button on the puppy details page
4. Choose another puppy from the list and click on the button “View Details”
3. Click on “Adopt me!” button on the puppy details page
4. Click on “Complete the Adoption” button 
5. Fill up the required field and select one of options from dropdown

####Expected result:
    Message should say “Thank you for adopting the puppies!”
####Actual results:
    Message should say “Thank you for adopting a puppy!”
####Screenshots:
screen_shot_9_1
![](https://i.ibb.co/M2kcyBq/9-1.png)
screen_shot_9_2
![](https://i.ibb.co/593RK6R/9-2.png)

######Bug id: #010

###Summary: The admin access has a very low protection level. Any user can create an account, and then edit info for puppies, delete them from the list, see the amount of orders that have been placed and see the adopter name.

####Steps to reproduce:
1. Navigate to the [puppies_adoption:users](https://puppies.herokuapp.com/users)
2. Click on “New User”
3. Select the required field and click “Create User”
4. Navigate [puppies_adoption:login](https://puppies.herokuapp.com/login) and enter your name and password
5. Click on Puppies button from the menu on a left side of the page 
6. Locate an Edit button on a edge of the puppy list and click on it
7. Locate the Fees field and enter any float number (except 0.00) 
8. Click an “Update Puppy” button
####Expected result:
    User without admin rights should not be able to adjust content on the website
####Actual results:
    User without admin rights is able to change fields and remove puppies from the list
####Screenshots: 
screen_shot_10_1
![](https://i.ibb.co/mqNFCDP/10-1.png)
screen_shot_10_2
![](https://i.ibb.co/Y8VRLmb/10-2.png)
screen_shot_10_3
![](https://i.ibb.co/qCCZbQ1/10-3.png)
screen_shot_10_4
![](https://i.ibb.co/KqyT4W1/10-4.png)
screen_shot_10_5
![](https://i.ibb.co/5j7Bcb0/10-5.png)


######Bug id: #011

###Summary:The cart doesn't have an option to remove one puppy from a list when you added several. The only option is to clean the list with "Change your mind" button.

####Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Choose any from the list and click on the button “View Details”
3. Click on “Adopt me!” button on the puppy details page
4. Choose another puppy from the list and click on the button “View Details”
5. Click on “Adopt me!” button on the puppy details page

####Expected result:
    User should have an option (button) that allows him to remove puppy from the list
####Actual results:
    There is no option for user to delete one of the several puppies from the cart
####Screenshots: 
screen_shot_11
![](https://i.ibb.co/bQ7GffV/11.png)

######Bug id: #012
###Summary: User is able to enter pass non-alphanumeric characters as parameters of all the fields on the payment details page and complete adoption successfully

####Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Choose any from the list and click on the button “View Details”
3. Click on “Adopt me!” button on the puppy details page
4. Choose another puppy from the list and click on the button “View Details”
5. Click on “Adopt me!” button on the puppy details page
6. Click on “Complete the Adoption” button 
7. Fill up the required fields with non-alphanumeric (!, ?, -, $) characters and select one of the options from drop-down

####Expected result:
    User should not be able to pass only non-alphanumeric characters in required fields and complete adoption
####Actual results:
    User is able to pass only non-alphanumeric characters in required fields complete adoption
####Screenshots:
screen_shot_12.1:
![](https://i.ibb.co/JmN8TLZ/12-1.png)
screen_shot_12.2:
![](https://i.ibb.co/L1mSJbP/12-2.png)

######Bug id: #013
###Summary: Some css files return 404 error that potentially causes the design issues on a website

####Steps to reproduce:
1. Navigate to the website [puppies_adoption](https://puppies.herokuapp.com/)
2. Open DevTools in browser
3. Refresh the page
4. Navigate to the Network tab


####Expected result:
    All css files should return 200 status code
####Actual results:
    Some css files return 404 status code
####Screen shots:
screen_shot_13:
![](https://i.ibb.co/ZgPLytb/13.png)



### Installation

To install all needed libraries use: 

```python3 -m pip install -r requirements.txt```

### Usage
###### (python3 used as a programming language)

####To run tests in CLI:
 
 ```python3 -m pytest tests/```

Chrome is default browser, also can be run on Firefox and Opera - can be changed on a line:

```{parser.addoption("--browser", default="chrome")``` in the file conftest.py



**Default browser can be changed in coftest.py**

**Added drivers can be run only on MacOS**



