# After Skool

[View the live app here.](https://after-skool.herokuapp.com/)

![home](/static/images/screenshot_1.png)


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

#### Booking/Club page

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

This section is available only for admin. This is a dropdown button in the navbar, when clicked it takes you to: 
1. Add a club page - To add a new club to the Shop section
2. All clubs can be edited or deleted form the booking/club page

### Other features
Scroll to top button added which is a convenience especially when viewing fom tablet or mobile
Message success/alert/error/warning toasts depending on the function. These can be closed or will be closed automatically after 3 secs

### Surface

The website is created in an easily navigatable manner with sections added in the navbar. When user is not logged in, the login/register page shows. When the user is logged in, My Profile appears and Login link turns to Logout. Superuser has an extra nav called management.<br>
The buttons and links - the information architecture is placed logically depending on the page <br>
The website is using a clean, minimalistic approach where a visually pleasing color scheme is used,<br>

The color scheme followed are:

The font used was Roboto.

### Skeleton

You can see the wireframes saved as pdf below:

[Wireframe for desktop](/assets/wireframes/desktop_wireframe.pdf)<br>


# Technologies Applied
The following technologie were used during the development of the project.

## Databases
- [Sqlite3](https://www.sqlite.org/index.html)
- [postgresSQL](https://www.postgresql.org/)
## Languages
- [CSS](https://www.w3.org/Style/CSS/)
- [HTML](https://html.spec.whatwg.org/multipage/)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
## Frameworks
- [Bootstrap](https://www.bootstrapcdn.com/)
- [Django](https://www.djangoproject.com/)
- [jQuery](https://jquery.com/)
## Libraries, Tools 
- [Google Fonts](https://fonts.google.com/)
- [Gitpod](https://www.gitpod.io/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/)
- [Dj-Database-URL](https://pypi.org/project/dj-database-url/)
- [Django-Countries](https://pypi.org/project/django-countries/)
- [Django-Heroku](https://pypi.org/project/django-heroku/)
- [Django-Storages](https://django-storages.readthedocs.io/en/latest/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Gunicorn](https://pypi.org/project/gunicorn/)
- [Jigsaw – CSS Validation](https://jigsaw.w3.org/css-validator/)
- [JS Hint](https://jshint.com/)
- [PEP8](http://pep8online.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Stripe](https://stripe.com/gb)
- [W3C – HTML Validation](https://validator.w3.org/)
## Hosting
- [Heroku](https://www.heroku.com/)
- [AWS S3 Bucket](https://aws.amazon.com/)


# Testing

A detailed description about the testing process and results can be found in the [TESTING.md](https://github.com/Verga1/after_skool/blob/master/TESTING.md). To give a brief overlook of the feature testing this table gives a codensed overview of the tested, features, devices, browsers and results:

| Test Case                     |    iPhone Safari   |    iPhone Chrome   |     iPhone Edge    |  Thinkpad Chrome   |   Thinkpad Edge    |    Yoga Chrome     |    Yoga Edge       |
|-------------------------------|:------------------:|:------------------:|:------------------:|:------------------:|:------------------:|:------------------:|--------------------|
| Test Navbar                   | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Landing Page                  | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Booking/Club                  | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Bag                           | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Checkout                      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Register                      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Registered Users: Useraccount | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |


# Deployment

This site is deployed to heroku and the versioning was done with git and the Repository is hosted on Github.


## Prerequisites to work with this Site

This project can be used for development with the following tools:

- IDE of Choice (I prefer Gitpod)
- Python3, PIP & Git should be installed

Furthermore accounts with the following services are used in this project:

- [Stripe](https://stripe.com/gb)
- [AWS S3 Bucket](https://aws.amazon.com/)
- [Gmail](www.gmail.com)

## Local Deployment: Step-by-Step Instructions

Official Github Documentation on cloning a repositiory: [Github - Cloning Repos](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

1. Navigate to Mainpage of the repository
2. Click on "Code" button
3. Choose "Clone with HTTPs" & copy URL
4. Open Terminal
5. Change the current working directory to prefered location
6. Type git clone and paste copied URL ```git clone https://github.com/Verga1/after_skool.git```
7. Press Enter to create local Clone - Make sure your environment supports python3 -
8. Type ```pip3 install -r requirements.txt``` into Terminal
9. Setup the environment variables. This process is differnet depending on the used IDE. Gitpod supports global Environments for the development process. Therefore they were stored in the settings. The following variables are needed:
    ```
    DEVELOPMENT=True   
    STRIPE_PUBLIC_KEY = <YOUR STRIPE_PUBLIC_KEY>
    STRIPE_SECRET_KEY = <YOUR STRIPE_SECRET_KEY>
    STRIPE_WH_SECRET = <YOUR STRIPE_WH_SECRET>
    ```
10. Migrate the models and create the database by typing the following commands into the terminal:
    1. ```python3 manage.py makemigrations```  
    2. ```python3 manage.py migrate```
11. Import the provided fixtures in the following order (copy&paste if you like): 
    1. ```python3 manage.py loaddata categories```
    2. ```python3 manage.py loaddata productline```
    3. ```python3 manage.py loaddata products```
    4. ```python3 manage.py loaddata proudctsize```
    5. ```python3 manage.py loaddata productvariants```
    6. ```python3 manage.py loaddata blog ```
    7. ```python3 manage.py loaddata faq ```
12. Create a superuser for accessing the django admin view with the following command:
    ```python3 manage.py createsuperuser``` You will be asked for an email address, username and password.
13. You should be all set and when using the command ```python3 manage.py runserver``` the project should run.
14. You can access the django admin view by adding ```~/admin``` to the end of your (local) URL.

## Deployment to Heroku: Step-by-Step Instructions

This project is deployed to Heroku. For the deployment the following steps were/are necessary:

1. Create/Log in to your Heroku account and create a new App.
2. Install Heroku Add-on Heroku Postgres from the Resources tab. The free ```Hobby Dev``` version is fine. Now click the Provision button to add it to your project.
3. Create requirements.txt from your project with the help of ```pip3 freeze --local > requirements.txt``` (already provided within the repository)
4. Create a Procfile ```echo web: gunicorn puffins.wsgi:application > Procfile``` (already provided within the repository)
5. Commit changes to Git ```git add .``` followed by ```git commit -m "Deploy: Updated Procfile"``` (already provided within the repository)
6. Set the environment variables in Heroku Settings > Reveal Config Variables
    The following Variables must be set:
    ```
    USE_AWS = TRUE
    AWS_ACCESS_KEY_ID = <YOUR AWS_ACCESS_KEY_ID>
    AWS_SECRET_ACCESS_KEY = <YOUR AWS_SECRET_ACCESS_KEY>
    DATABASE_URL = <YOUR DATABASE_URL> (Set by Heroku Postgres)
    EMAIL_HOST_USER = <YOUR EMAIL_HOST_USER>
    EMAIL_HOST_PASSWORD = <YOUR EMAIL_HOST_PASSWORD>
    DEFAULT_FROM_EMAIL = <YOUR DEFAULT_FROM_EMAIL>
    STRIPE_PUBLIC_KEY = <YOUR STRIPE_PUBLIC_KEY>
    STRIPE_SECRET_KEY = <YOUR STRIPE_SECRET_KEY>
    STRIPE_WH_SECRET = <YOUR STRIPE_WH_SECRET>
    ```
7. Extract the DATABASE_URL Value from the Heroku Settings and set it up in your IDE or local .env file. Make sure to keep this DATABASE_URL a secret and definitly don't commit it to Github.
8. To test if the Postgres database is connected to your IDE you can make use of the command ```python3 manage.py showmigrations```. This should show undone migrations for all models.
9. Now migrate the models and create the postgres database on heroku by typing the following commands into the terminal:
    1. ```python3 manage.py makemigrations```  
    2. ```python3 manage.py migrate```
10. To setup the data in the database import the provided fixtures in the following order (copy&paste if you like): 
    1. ```python3 manage.py loaddata categories```
    2. ```python3 manage.py loaddata productline```
    3. ```python3 manage.py loaddata products```
    4. ```python3 manage.py loaddata proudctsize```
    5. ```python3 manage.py loaddata productvariants```
    6. ```python3 manage.py loaddata blog ```
    7. ```python3 manage.py loaddata faq ```
11. Create a superuser for the Postgres database for accessing the django admin view with the following command:
    ```python3 manage.py createsuperuser``` You will be asked for an email address, username and password.
12. Log in to heroku from your terminal ```heroku login```
13. Add exisitng repository to Heroku heroku ```git:remote -a <your repository>```
14. Push changes to Heroku ```git push heroku master```
15. Now go to your S3 account. There bucket should already contain a folder called ```static```. To upload the product images create a new folder called ```media```. And add the files to this folder. Make sure to grant public read access to these objects. 
15. Finally, visit the app url from heroku and check out your great site!

# References & Acknowledgment

## Media

Category Images: 
* All images used on the site were taken from google images

## Acknowledgements

Special Thanks to...

* ... my Code-Institute Mentor
* ... the Tutors from [Code Institute](www.codeinstitute.net)


## References 
* Project was developed by following the [Code Institute](www.codeinstitute.net) Boutique Ado-Poject lessons and was extended and modified to personal needs


# Fair use disclaimer

This is for educational use