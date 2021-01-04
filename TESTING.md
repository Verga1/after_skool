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
4. Choose any club by clicking the image
5. Add Item to bag
6. Side Drawer bag should open
7. Continue shopping by clicking on the main screen or on to the Close button at the top 
8. Bag should Close
9. Choose another club
10. Add Item to bag
11. Side Drawer bag should and last added item should be on top

### Checkout from Side Drawer bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Choose any club by clicking the image
5. Add Item to bag
6. Side Drawer bag should open
7. Press Checkout Button
8. Press Checkout Button on main bag page
9. Checkout Page should open

### Increase Quantity in Fullpage bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Choose any club by clicking the image
5. Add Item to bag
6. Side Drawer bag should open
7. Click checkout button
8. Should be redirected to Fullpage bag
9. Press "+" Button
10. Click update
11. Side drawer bag will open and quantity increased by one

### Decrease Quantity in Fullpage bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Choose any club by clicking the image
5. Add Item to bag
6. Side Drawer bag should open
7. Click checkout button
8. Should be redirect to Fullpage bag
9. Press "-" Button
10. Click update
11. Side drawer bag will open and quantity decreased by one

### Remove Item(s) in Fullpage bag :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Choose any club by clicking the image
5. Add Item to bag
6. Side Drawer bag should open
7. Click checkout button
8. Should be redirected to Fullpage bag
9. Click remove 
10. Side drawer bag will open and item should be removed from bag (if multiple club categories were in bag)
11. No booking page should open (if only 1 club category was in bag)

## 5. Checkout :white_check_mark:

### Checkout AnonymousUser :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click on Book Now
4. Choose any club by clicking the image
5. Add Item to bag
6. Side Drawer bag should open
7. Click Checkout-Button
8. Should be redirected to Fullpage bag
9. Click Checkout-Button
10. Should be redirected to checkout page
11. Form for address details & Order Summary should be displayed
12. Fill in form & use test credit card (4242 4242 4242 4242)
13. Submit order
14. Loading animation should be displayed
15. Checkout success page should be shown

### Checkout registered user :white_check_mark:

1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click Userprofile-icon and login with test@test.com pw: testuser1
4. Click on Book Now
5. Choose any club by clicking the image
6. Add Item to bag
7. Side Drawer bag should open
8. Click Checkout-Button
9. Should be redirected to Fullpage bag
10. Click Checkout-Button
11. Should be redirected to checkout page
12. Form for address details should be prefilled & Order Summary should be displayed
13. Add test credit card (4242 4242 4242 4242)
14. Complete order
15. Loading animation should be displayed
16. Checkout success page should be shown

## 6. Register :white_check_mark:

### Register :white_check_mark:
1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click Userprofile-icon
4. Choose Register
5. Fill out the Form
6. Check if confirmation mail was received
7. Confirm email
8. Login with credentials

## 7. Registered Users: Useraccount :white_check_mark:

1. Open Browser
2. Open [AfterSkool Page](https://afterskool.herokuapp.com)
3. Click Userprofile-icon 
4. Select Login
5. Should see Form 
6. Enter username and password
7. Redirected to home page


## 8. Store/User Management :white_check_mark:

### Club Management :white_check_mark:

#### Create Club :white_check_mark:
#### Read Club :white_check_mark:
#### Update Club :white_check_mark:
#### Delete Club :white_check_mark:

### Profile Management :white_check_mark:

#### Create Profile :white_check_mark:
#### Read Profile :white_check_mark:
#### Update Profile :white_check_mark:
#### Delete Profile :white_check_mark:


# User Testing

Besides running through the extensive test cycles documented above the URL from the Heroku deployment was shared with friends and family. 

Following Improvements/Features/Bugs were identified:
* Feature Requests  
  * 
* Improvement
    * 
* Bugs
    * 
    * 
    * 
    * 

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
* iPhone XR
* HP Envy
* Lenovo Yoga

## Browser Compatibility
The site was tested on the following Browsers:
* [Apple Safari](https://www.apple.com/safari/) 
* [Google Chrome](https://www.google.com/chrome/)
* [Microsoft Edge](https://www.microsoft.com/edge)

On all browsers full site compatibility was identified based on the test cases.

# Bug-Log from Development

The following bugs were identified and mainly fixed during development:
1. 
