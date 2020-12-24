


# UXD Considerations

## Purpose and Aim of the Project

The aim of this project is to create an ecommerce shop for a primary school that is targeted towards kids and families in the local area. The goal is to create this shop as an interactive fullstack website that allows customers to browse the available clubs, make bookings by credit card and if registered manage their orderhistory. These goals should be supported by providing a clean and easy to use website that allows seamless navigation and has a low bounce rate.

## Design process
Before laying out the project and creating an initial design market research was done. During this research phase the following questions were also acknowledged: 
* Do other schools provide this service?
* How do their stores look?
* What are typical design patterns used across stores?
* Which sites are appealing to me?
* Which kind of stores fit to my business idea? 

There are very few schools running this type of service or an ecommerce site so I looked across other sites for inspiration. Most retail sites fit the needs of the school site, exchanging products for clubs.


## Target group

The shop is targeted to parents and kids alike. The typical age of a shopper is estimated to be between 25 and 45 years but may be influenced by the child who may want to join a particular club. The families usually have 1-2 children in the age of 4 years up to 12 years. The clubs have a diverse spread of activities to entice as many children to participate in their preferred field. The income of the target group is an average mid to high household income. Furthermore the target group has a passion for engaging in extra curricular activites. 

## User Stories
Before the start of the Project the Epics and User Stories were defined and written out to have complete set of necessary features to get the site going. In total 5 Epics were defined and user stories were broken down into 3 user groups:
* regular __site visitors__
* __registered users__
* the __club teacher/owner__.

### EPIC: Browse Site
As a __site visitor__, i want to...
* ... __access the website__ with any device (smartphone, tablet, desktop), so that i am able to visit the shop anytime and anywhere.
* ... have __easy navigation__, to quickly solve the reason for my visit.
* ... have __information about the brand__, to get to know the clubs and understand their mission and story.

### Epic: Browse Products
As a __site visitor__, i want to...
* ... browse clubs by __category and activity type__, so that i quickly find what i am looking for.
* ... __sort clubs_, to adjust the order according to my needs.
* ... be able to __search for specific clubs__, to quickly get what i need.
* ... to __access club details__, to get more information on an item.
* ... be able to __choose a club__, to order the necessary items according to my needs.

### Epic: Manage Cart & Make Booking
As a __site visitor__, i want to...
* ... see all my __items in a cart__, so that i have an overview of my potential booking.
* ... be able to __reduce / increase quantity__, so that i can order my prefered amount.
* ... be able to __remove an item from my cart__, so that i can manage my cart efficiently.
* ... be able to __checkout from the cart__ view, so that i can quickly finish my booking.
* ... be able to __pay a booking by credit card__, so that i don't have to deal with an invoice and money transfer.
* ... __receive an booking confirmation__, so that i know my booking was completed.

As a __registered user__, i want to...
* ... have my __details prefilled from my profile__, so that i quickly can finish my booking

### Epic: Registration & Useraccount

As a __site visitor__, i want to...
* ... be able to __sign up to the site__, so that i can track bookings and have my data prefilled in the order form.

As a __registered user__, i want to...
* ... be __able to login__, so that i can access my useraccount.
* ... be able to __see my order history__, so that i know what i've booked in the past.
* ... __manage my personal details__, so that i can quickly update my data if something changes.

### Epic: Site Management
As a __site owner__, i want to...
* ... be able to __manage the clubs, categories, price and availability__, so that i have an overview of all club details.
* ... __manage customer queries__, so that i can quickly update the site when required

## Layout, Styling & Wireframes

### Structure

There are 6 main pages including the home page and a login/registration page. Other than these, there is a base page which serves as the base for all the other pages. 

#### The home page
The home page gives a quick glance at the brand of the site and a link to the booking page.  

#### Booking page

This page provides a list of clubs which users can purchase. There are filters and a sort functionality to aid in the search. Once they click into a club, it takes them to a page which provides a bit more information about the club. From here, they can add this to the shopping bag. 

#### Shopping bag page

They can add this to cart and go to checkout or keep adding more clubs. There is a cart which shows the total which is calculated automatically based on the clubs they add. They can delete the club if no longer required or if they want to add more clubs, there is a button which takes them to the Shop page to book more clubs. Once they have added all the clubs to the cart, they can go to the Checkout page by clicking on the Cart. <br>
NB: Shopping cart is added only in the Shop and shopping bag pages as they are only part of the site and not the main focus.

#### Checkout page

Here the user can enter their billing details to complete the checkout. If they need to update the cart at any point before billing, they have the option to go back to the Shop by clicking on a button. In this page, the users are provided with an option to save their details by logging into the site. If they don't want that option, they can click on Complete Order button to complete the transaction which triggers an automatic mail to their email address provided with the necessary details. If they want to save the details for future, they can register or login from the page or from the navbar. 

#### Login page

The users are provided with the option to register/login to create an account. For new users, they can redirect to the Sign up page from here. They need to include their email address, name and password to sign up. Once that is done, a confirmation link will be sent to their email address. Once the email is confirmed, they can login to the site. Logged in users have the ability to navigate to the Profile page. 

#### Profile page

The logged in users can update their billing details from this page. If they have made any previous bookings, those details are also shown in this page. 

#### Logout page

For users logged in, they can click on the logout button which takes them to this page to confirm that they need to logout. Clicking on the Sign out button logs them out from the site. 

#### Management section

This section is available only for admin. This is a dropdown button in the navbar, when clicked on provides with three options 
1. Add a club - To add a new club to the Shop section

### Surface

The website is created in an easily navigatable manner with sections added in the navbar. When user is not logged in, the login/register page shows. When the user is logged in, My Profile appears and Login link turns to Logout. Superuser has an extra nav called management.<br>
The buttons and links - the information architecture is placed logically depending on the page <br>
The website is using a clean, minimalistic approach where a visually pleasing color scheme is used,<br>

The color scheme followed are:

The font used was Roboto.

### Skeleton

You can see the wireframes saved as pdf below:

[Wireframe for desktop](/assets/wireframes/desktop_wireframe.pdf)<br>

### Existing Features
1. Responsive layout: Site is accessable and scalable across devices
2. Users can book club from the shop. Filter added in this page to filter the clubs. 
3. Shopping cart updates total automatically based on booking of clubs. Shopping cart is added only in the Shop and shopping bag pages as they are only part of the site and not the main focus.
4. Option to delete club from shopping bag
5. Portfolio can be viewed from their pages
6. Registration/login: Users can register or login with a username and password. 
7. Billing details can be updated from the profile page for logged in users
8. CRUD: Superuser can add clubs and portfolio. Superuser have the functionality to edit or delete any of them as well. 
9. Scroll to top button added which is a convenience especially when viewing fom tablet or mobile
10. Message success/alert/error/warning toasts depending on the function. These can be closed or will be closed automatically after 3 secs

