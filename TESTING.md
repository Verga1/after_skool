# Introduction

All the links have been manually tested. <br>
Tested if there are any problems in the coding or code styling using pylint<br>

# Manual Test Cycles

## 1. Test Navbar :white_check_mark:

### General Functionalities :white_check_mark:

1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click every nav item
4. Ensure all links work correctly for clubs

### Logged in and non-logged in users see different options :white_check_mark:

1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Check if navbar contains  
   Home logo  
   Club links 
   Userprofile-icon  
   Bag-icon  
   Search-icon  
4. Click Userprofile-icon and login 
5. Check the Userprofile-icon and check the following are present  
   Product Management Link (for admin only)  
   My Profile
   Log Out  

## 2. Landing Page :white_check_mark

1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Check that   
   Club page is opened by clicking the Book Now Button 

## 3. Booking/Club Page 

### Club Categories :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Click all sorting options
5. Toggle the Sort switch through all options and check that sorting works accordingly  
    ...Age :white_check_mark:  
    ...Price :white_check_mark:  
    ...Rating :white_check_mark:  
    ...Name :white_check_mark: 
    ...Category :white_check_mark: 

### Get Club Details :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Choose any club by clicking the image
6. New page should open
7. Page should contain  
   Club image
   Age details 
   Descripton 
   Teacher
   Rating 
   Add to bag Button  
   Quantity field
   Return to Club button

## 4. Bag :white_check_mark:

### Check empty bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on bag-Icon
4. No booking page should open
5. Placeholder "You have no bookings" should be displayed 
6. View Clubs button should direct you back to Clubs page

### Add item to bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Choose any club by clicking the image
5. Add Item to bag
6. Side Drawer bag should open
7. Chosen Club should be inside the bag view

### Open Fullpage bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Choose any club by clicking the image
5. Add Item to bag
6. Side Drawer bag should open
7. Click below checkout button on bag
8. Fullpage bag should open

### Add two items to bag and check Position :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
5. Choose any club by clicking the image
6. Add Item to bag
7. Side Drawer bag should open
8. Continue shopping by clicking on the main screen or on to the Close button at the top 
9. Bag should Close
10. Choose another club
11. Add Item to bag
12. Side Drawer bag should and last added item should be on top

### Checkout from Side Drawer bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
5. Choose any club by clicking the image
6. Add Item to bag
7. Side Drawer bag should open
8. Press Checkout Button
8. Press Checkout Button on main bag page
9. Checkout Page should open

### Increase Quantity in Fullpage bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
5. Choose any club by clicking the image
6. Add Item to bag
7. Side Drawer bag should open
8. Click checkout button
9. Should be redirected to Fullpage bag
10. Press "+" Button
10. Click update
11. Side drawer bag will open and quantity increased by one

### Decrease Quantity in Fullpage bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
5. Choose any club by clicking the image
6. Add Item to bag
7. Side Drawer bag should open
8. Click checkout button
9. Should be redirect to Fullpage bag
10. Press "-" Button
10. Click update
11. Side drawer bag will open and quantity decreased by one

### Remove Item(s) in Fullpage bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
5. Choose any club by clicking the image
6. Add Item to bag
7. Side Drawer bag should open
8. Click checkout button
9. Should be redirected to Fullpage bag
10. Click remove 
11. Side drawer bag will open and item should be removed from bag (if multiple club categories were in bag)
11. No booking page should open (if only 1 club category was in bag)

## 5. Checkout :white_check_mark:

### Checkout AnonymousUser :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
5. Choose any club by clicking the image
6. Add Item to bag
7. Side Drawer bag should open
8. Click Checkout-Button
8. Should be redirected to Fullpage bag
9. Click Checkout-Button
9. Should be redirected to checkout page
10. Form for address details & Order Summary should be displayed
11. Fill in form & use test credit card (4242 4242 4242 4242)
12. Submit order
13. Loading animation should be displayed
14. Checkout success page should be shown

### Checkout registered user :white_check_mark:

1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click Userprofile-icon and login with test@test.com pw: testuser1
4. Click on Book Now
6. Choose any club by clicking the image
7. Add Item to bag
8. Side Drawer bag should open
9. Click Checkout-Button
8. Should be redirected to Fullpage bag
9. Click Checkout-Button
10. Should be redirected to checkout page
10. Form for address details should be prefilled & Order Summary should be displayed
11. add test credit card (4242 4242 4242 4242)
12. Submit order
13. Loading animation should be displayed
14. Checkout success page should be shown

## 10. Sign Up :white_check_mark:

### Sign Up :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click Userprofile-icon
4. Choose Sign Ups
5. Fill out the Form
6. Check if confirmation mail was received
7. Confirm email
8. Login with credentials

## 11. Registered Users: Useraccount :white_check_mark:

1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on UserAccount-icon
5. Should see Form 
6. Should see Order History

## Registered Users: Wishlist :white_check_mark:

### Show empty wishlist :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on Heart-icon
5. Should show empty wishlist

### Add product to wishlist :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Login with 
4. Click on Book Now
5. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any club by clicking the image
6. Click Heart below Add to bag-Button
7. Heart should change from outline to filled

### Show wishlist :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on Heart-icon
5. Should show wishlist with one liked item

## 12. Store Management :white_check_mark:

### Product Management :white_check_mark:

#### Create Product :white_check_mark:
#### Read Product :white_check_mark:
#### Update Product :white_check_mark:
#### Delete Product :white_check_mark:

### Order Management :white_check_mark:

#### Create Order :white_check_mark:
#### Read Order :white_check_mark:
#### Update Order :white_check_mark:
#### Delete Order :white_check_mark:

### Blog Management :white_check_mark:

#### Create Post :white_check_mark:
#### Read Post :white_check_mark:
#### Update Post :white_check_mark:
#### Delete Post :white_check_mark:

# User Testing

Besides running through the extensive test cycles documented above the URL from the Heroku deployment was shared with friends and family. The following feedback was collected:

- "Great products"
- "Beautiful design"
- "Footer looks a little too full"

Following Improvements/Features/Bugs were identified:
* Feature Requests  
  * Feature request: I wish i could increase/decrease quantity within the sidedrawer bag :white_check_mark:
* Improvement
    * bag on Mobile view hidden. As an idea for a later release the logo and text logo would move to the center. Moving the Burger-Menu to the left side of the screen and adding the bag symbol to the right top corner. :toolbox:
* Bugs
    * Quantity not shown in Side Drawer bag :white_check_mark:
    * Buttons on Carrousel not inline with button box :white_check_mark:
    * bag Mobile Fullpage not in view :white_check_mark:
    * Info Toast behind Navbar :white_check_mark:
    * Adding a Product to the bag and using the back button in browser or the implemented backbutton does not refresh the page. Therefor the bag does not signal that the user has something in the bag. Couple of solutions found on Stackoverflow were tested but none could solve the issue. This bug is still pending and should be fixed in the next release. :toolbox:

# Automatic Tests & Continious Integration

A basic set of test using the Django TestCase integration were created to support the testing and development process and gain practical knowledge in this field. Test were written for the following apps:

- About (Views) - 100% Coverage
- Blog (Models & Views) - 100% Coverage
- Contact (Forms 100%, Models 100%, Views 54%)
- Useraccount (Forms 81%, Models 100%, Views 65%)
- Wishlist (Models 100% & Views 58%)

More test need to be written to reach a 100% test coverage. Furthermore, [Travis CI](https://travis-ci.org/github/p0wen/puffins) used to allow continious integration patterns in combination with Heroku. Travis CI is an open source software for continious integration.

Build Status:

[![Build Status](https://travis-ci.org/p0wen/puffins.svg?branch=master)](https://travis-ci.org/p0wen/puffins)

# Validation Services

## Validation Tools
### [W3C Markup Validation Service](https://validator.w3.org)
All pages incl. sub-pages were processed through the [W3C Markup Validation Service](https://validator.w3.org). The validation revealed some missing ```alt=""``` statements, stray ```<div>```'s and conventions regarding the use of ```<span>``` in combination with ```<hr>```. The findings were all resolved and no more issues were found by the [W3C Markup Validation Service](https://validator.w3.org).
### [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/)
The whole css file ran through the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). After taking care of some minor errors and cleaning up the css 5 Errors are still reported. These Errors were accepted since they mark the use of the javascript injected dynamic ```--vh``` variable in combination with the ```calc()``` operation. Furthermore 18 Warnings were accepted. The 10 of the 18 warnings also relate to the dynmic height view-height variable. And the other 8 warnings inform about same colors on 2 classes ```.allauth-form-inner-content button``` and ```.allauth-form-inner-content input[type="submit"]``` which was also accepted in this case.
### [JS Hint](https://jshint.com)
All *.js files were checked with the service of [JS Hint](https://jshint.com). By using this service some bugs like wrong use of ```&&``` in if functions and missing `;` were identified and solved.
### [PEP8 Online](http://pep8online.com)
All *.py files were checked with the service of [PEP8 Online](http://pep8online.com). The files looked all good and no error was reported.
## Responsiveness & Rendering
The site was created with the mobile first approach in mind. The following devices / device sizes were used for testing the responsiveness:
* iPhone 11 Pro 
* iPad 10,2"
* MacBook Pro 13"

## Browser Compatibility
The site was tested on the following Browsers:
* [Apple Safari](https://www.apple.com/safari/) 
* [Google Chrome](https://www.google.com/chrome/)
* [Brave Broser](https://brave.com/)
* [Microsoft Edge](https://www.microsoft.com/edge)

On all browsers full site compatibility was identified based on the test cases.

# Peer-Code-Review

The project was peer-reviewed by students from code institute. Feedback was given on the readme files and the code. 

# Bug-Log from Development

The following bugs were identified and mainly fixed during development:
1. Updating userprofile even if checkbox is unchecked on Checkout form:  

   This issue was identified during the extensive testing protocoll and took a while to solve. The problem was that the used JavaScript call to check if the checkbox is checked or unchecked always returned true. Furthermore, the python code didn't identify the javascript `true`/`false` response as `True` or `False`. Therefore the functions did not process the given information as intended. The following lines were introduce to make the function work as intended:
   ```
   stripe_elements.js
   var saveInfo = $('#id-save-info').is(':checked');
   ```
   ```
   webhook_handler.py
   if save_info == "true":
   ```
2. Webhooks for orders  without the optional streetaddressline2 filled out were failing. Therefore customers who didn't provide a line2 street address were not receiving their order confirmation. The problem laid in the model definition. By allowing `null` to be `true` on `street_address2` the webhooks were processed without problems.
3. Adding products to a wishlist if no item was added before on a fresh user failed in the beginning. The solution was to use the `get_or_create` method and check if the object was created or already existed.  
4. Product images were not displayed when using the `{{MEDIA_URL}}` template tag. This was solved by extensivly checking the settings.py and by realizing that the ```django.template.context_processors.media``` was missing in the templates setup. 
5. Importing fixtures to postgres db led to some troubles. This was solved by making sure the charfields are set correct and that especially on long descriptions it makes sense to use TextField.
