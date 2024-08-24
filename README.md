# MemoVault

## Project Goals

MemoVault is a social media backend API that allows users to register, log in, create posts, follow/unfollow other users, like comments and posts as well as comment on posts, manage their profiles, report posts as well as manage their reports. This project is designed to be the foundation for a social media platform. The API is also used for the 
[MemoVault React Web App](https://github.com/devnickocodes/memovault-app)

## Planning

The planning phase for MemoVault began with outlining the key features and creating user stories for the backend API. These user stories were instrumental in shaping the design and functionality of the API, ensuring all necessary functionality was covered.

### Data Models

The data models were planned using an entity relationship diagram.

![ERD](https://github.com/devnickocodes/memovault-api/blob/main/readme_docs/ERD.png)

The diagram was created with [draw.io](https://app.diagrams.net/).


#### **Profile**

A profile is created and assigned to the user upon user registration using a one-to-one relationship to Django's AllAuth user model.
The users can edit the following fields of their profiles.

`name`
`hobbies`
`bio`
`image`

#### **Post**

A post is created and associated with a user through a one-to-many relationship using the `owner` field, which links each post to a specific user. This allows each user to create multiple posts where a user can have many posts, but each post has only one owner.
The owner can edit the following fields of their post.

`title`
`content`
`image`

#### **Comment**

A comment is created by a user on a specific post, and it is associated with both the user and the post through foreign key one-to-many relationships. Each comment is linked to the user who created it and a post on which it was made. A user can make multiple comments, but each comment has only one owner. Each comment is associated with a single post on which it is made. A post can have multiple comments, but each comment is linked to only one post.
The owner can edit the `content` field of their comment.

#### **PostLike**

The model captures two one-to-many relationships between users and posts where users can "like" posts. Each like is associated with a specific user and a specific post. A user can like multiple posts, and each like is linked to one specific user. A post can have many likes, and each like is linked to one specific post.

#### **CommentLike**

The model captures the relationship between users and comments, where users can "like" comments. Each like is associated with a specific user and a specific comment. Each like is associated with a single user who liked the comment. A user can like multiple comments, and each like is linked to one specific user. A comment can have multiple likes, and each like is linked to one specific comment.

#### **Follower**

The Follower model manages the follow relationships between users. It tracks which users are following which other users within the system. One user can have multiple follow relationships as a follower and one user can be followed by multiple other users.


#### **Report**

The Report model is used to record user reports for posts. This allows users to report inappropriate or problematic content. Each report is linked to both a user and a post.Each Report entry is linked to one specific user who made the report. Thus, a single user can be responsible for many reports. Each report is associated with one user. Each Report entry is linked to one specific post that is being reported. A single post can have multiple reports associated with it. Each report is associated with exactly one post.
The users can edit the following fields of their reports.

`reson`
`custom_reason` (where applicable)


## API endpoints


| **URL** | **Notes** | **HTTP Method** | **CRUD operation** | **View type** | **POST/PUT data format** |
|---|---|---:|---|---:|---|
|  |  |  |  |  |  |
| **Post endpoints** |  |  |  |  |  |
| /posts/ | Lists all posts with options to filter, search, and order the results. Authenticated users can create new posts. | GET | Read | List | N/A |
| /posts/ | Creates a new post. The authenticated user is set as the owner of the post. | POST | Create | List | {<br> "title": "string",<br> "content": "string",<br> "image": "string (optional)"<br>} |
| /posts/id | Retrieves details of a specific post. | GET | Read | Detail | N/A |
| /posts/id | Updates details of a specific post. Restricted to the owner or admin. | PUT | Update | Detail | {<br> "title": "string",<br> "content": "string",<br> "image": "string (optional)"<br>} |
| /posts/id | Deletes a specific post. Restricted to the owner or admin. | DELETE | Delete | Detail | N/A |
| **Comment endpoints** |  |  |  |  |  |
| /comments/ | Lists all comments with options to filter and order the results. Authenticated users can create new comments. | GET | Read | List | N/A |
| /comments/ | Creates a new comment associated with a specific post. The authenticated user is set as the owner of the comment. | GET | Read | List |{<br> "post": "integer",<br> "content": "string"<br>} |
| /comments/id | Retrieves details of a specific comment. | GET | Read | List | N/A |
| /comments/id | Updates details of a specific comment. Restricted to the owner or admin. | PUT | Update | Detail | {<br> "content": "string"<br>} |
| /comments/id | Deletes a specific comment. Restricted to the owner or admin. | DELETE | Delete | Detail | N/A |
| **Follower endpoints** |  |  |  |  |  |
| /followers/ | Lists all followers. | GET | Read | List | N/A |
| /followers/ | Creates a new follower relationship. Restricted to authenticated users. | POST | Create | List | {<br> "followed": "integer"<br>}|
| /followers/id | Retrieves details about a specific follower relationship. | GET | Read | Detail | N/A |
| /followers/id | Deletes a specific follower relationship. Restricted to the owner. | DELETE | Delete | Detail | N/A |
| **Post Like endpoints** |  |  |  |  |  |
| /like/post/ | Lists all post likes with options to filter and order the results. | GET | Read | List | N/A |
| /like/post/ | Creates a new post like associated with a specific post. Authenticated users are set as the owner of the post like. | POST | Create | List | {<br> "post": "integer" <br>} |
| /like/post/id | Retrieves details of a specific post like. | GET | Read | Detail | N/A |
| /like/post/id | Deletes a specific post like. | DELETE | Delete | Detail | N/A |
| **Comment Like endpoints** |  |  |  |  |  |
| /like/comment/ | Lists all comment likes. | GET | Read | List | N/A |
| /like/comment/ | Creates a new comment like associated with a specific comment. Authenticated users are set as the owner of the comment like. | POST | Create | List | {<br> "comment": "integer" <br>} |
| /like/comment/id | Retrieves details of a specific comment like. | GET | Read | Detail | N/A |
| /like/comment/id | Deletes a specific comment like. | DELETE | Delete | Detail | N/A |
| **Profile endpoints** |  |  |  |  |  |
| /profiles/ | Lists all profiles or filters/searches through existing profiles. | GET | Read | List | N/A |
| /profiles/id | Retrieves detailes about a specific profile. | GET | Read | Detail | N/A |
| /profiles/id | Updates a specific profile. Restricted to the owner. | PUT | Update | Detail | {<br> "name": "string (optional)",<br> "bio": "string (optional)",<br> "hobbies": "string (optional)",<br> "image": "string (optional)"<br>} |
| **Report endpoints** |  |  |  |  |  |
| /reports/ | Lists all reports submitted by the authenticated user. | GET | Read | List | N/A |
| /reports/ | Creates a new report. The authenticated user is automatically set as the owner of the report. | POST | Create | List | {<br> "post": "integer",<br> "reason": "string",<br> "custom_reason": "string (optional unless 'other' is chosen from the 'reason' dropdown)"<br>} |
| /reports/id | Retrieves details of a specific report submitted by the authenticated user. | GET | Read | Detail | N/A |
| /reports/id | Updates details of a specific report. Restricted to the owner. | PUT | Update | Detail | {<br> "reason": "string",<br> "custom_reason": "string (optional unless 'other' is chosen from the 'reason' dropdown)"<br>} |
| /reports/id | Deletes a specific report. Restricted to the owner. | DELETE | Delete | Detail | N/A |
| /reports/admin/ | Lists all reports for administrators. | GET | Read | List | N/A |
| /reports/admin/id | Retrieves details of a specific report for administrators. | GET | Read | List | N/A |
| /reports/admin/id | Deletes a specific report for administrators. | DELETE | Delete | Detail | N/A |


## Frameworks, libraries and dependencies

The MemoVault API is developed in Python, using [Django](https://www.djangoproject.com) and [Django Rest Framework](https://www.django-rest-framework.org/).

Find all utilities, apps, and modules that were also used bellow:


### django-cloudinary-storage
https://pypi.org/project/django-cloudinary-storage/

Enables Cloudinary integration for managing and storing media files in the cloud.


### dj-allauth
https://django-allauth.readthedocs.io/en/latest/

Provides comprehensive user authentication, registration, and account management functionalities. Future updates may include social authentication via this package.


### dj-rest-auth
https://dj-rest-auth.readthedocs.io/en/latest/introduction.html

Provides ready-to-use REST API endpoints for user authentication processes, including login, logout, password reset, and user registration.


### djangorestframework-simplejwt
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

Facilitates JSON web token authentication for securing API endpoints and user sessions.


### dj-database-url
https://pypi.org/project/dj-database-url/

Enables easy configuration of the database connection using environment variables.


### psycopg2
https://pypi.org/project/psycopg2/

A PostgreSQL database adapter for Python, enabling seamless interaction with PostgreSQL databases.

### python-dateutil
https://pypi.org/project/python-dateutil/

Provides powerful extensions to the standard datetime module.

### asgiref

https://pypi.org/project/asgiref/

Provides an asynchronous server gateway interface (ASGI) reference implementation for Python web servers and frameworks.


### cloudinary
https://pypi.org/project/cloudinary/

A Python client library for integrating with Cloudinary, a cloud service for managing media.


### cryptography
https://pypi.org/project/cryptography/

A package designed to provide cryptographic recipes and primitives to Python developers.


### django
https://www.djangoproject.com/

A high-level Python web framework that encourages rapid development and clean, pragmatic design.

### django-cors-headers
https://pypi.org/project/django-cors-headers/

Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).


### django-filter
https://django-filter.readthedocs.io/en/stable/

Facilitates the addition of dynamic query sets to Django REST Framework views by allowing complex filtering.


### djangorestframework
https://www.django-rest-framework.org/

A powerful and flexible toolkit for building Web APIs in Django.

### gunicorn 
https://gunicorn.org/

A Python WSGI HTTP server for UNIX, useful for running Django applications.


### oauthlib
https://oauthlib.readthedocs.io/en/latest/

A thorough implementation of the OAuth request-signing logic for Python.


### Pillow
https://pillow.readthedocs.io/en/stable/

This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

### PyJWT
https://pyjwt.readthedocs.io/en/latest/

Python library which allows you to encode and decode JSON Web Tokens (JWT)


### python3-openid
https://pypi.org/project/python3-openid/

A set of Python packages to support use of the OpenID decentralized identity system in your application.

### pytz
https://pypi.org/project/pytz/

Enables accurate and cross-platform timezone calculations


### requests-oauthlib

Requests-OAuthlib uses the Python Requests and OAuthlib libraries to provide an easy-to-use Python interface for building OAuth1 and OAuth2 clients.

### sqlparse
https://pypi.org/project/sqlparse/

A non-validating SQL parser for Python, used for splitting, formatting, and parsing SQL statements.

### urllib3
https://urllib3.readthedocs.io/en/latest/

A powerful, user-friendly HTTP client for Python

## Testing

You can find the testing and validation [here](TESTING.md).

## Bugs

- When trying to implement validation in the serializer for the followers app that a user can't follow themselves I got a KeyError, because the 'owner' key was missing.


![KeyError](https://github.com/devnickocodes/memovault-api/blob/main/readme_docs/error_1.png)


- FIX: The issue was fixed by adding a check that ensures that the owner field is present in the input data. If it is missing, it sets the owner to the user making the request
  
    ```python
    if 'owner' not in data:
        data['owner'] = self.context['request'].user
    ```




- There was another issue trying to install `dj-rest-auth[with_social]`

![dj-rest-auth Issue](https://github.com/devnickocodes/memovault-api/blob/main/readme_docs/error_2.png)


- FIX: The issue was fixed by changing the versions of some of the dependacies.



- An AssertionError arose during development that a FollowerList should either include `queryset` attribute, or override the `get_queryset()` method.

![AssertionError](https://github.com/devnickocodes/memovault-api/blob/main/readme_docs/error_3.png)


- FIX: A `get_queryset()` method was added. 

    ```python
    def get_queryset(self):
        return Follower.objects.all()
    ```



- Another error that occurred was a TypeError. When trying to create a post by filling everything in the form except choosing an image and sticking with the default one, the post would be created, but when trying to create a post and choose a custom image to upload the error would occur.

![TypeError](https://github.com/devnickocodes/memovault-api/blob/main/readme_docs/error_3.png)

- FIX: The issue was fixed by fixing mismatched versions for the cloudinary dependancy with `pip3 install cloudinary==1.32.0`


## Deployment

The MemoVault API is deployed on Heroku, using a PostgreSQL database provided by ElephantSQL. For deployment follow the steps bellow:


- Fork or clone this repository from GitHub

- Configure Cloudinary

    - A Cloudinary account is needed for managing media files.
    - Create and log in to your Cloudinary account.
    - Access the 'Dashboard' section and click on 'Go to API Keys'
    - Find and copy the 'API Environment variable' starting with cloudinary:// and change '<your_api_key>' with your API Key and '<your_api_secret>' with your API Secret (reveal it by clicking the eye icon if necessary). Store it secretly for later.

- Set Up Heroku Application

    - Create and log into your Heroku account.
    - Click on 'New' in the top-right corner and select 'Create new app'.
    - Provide a name for your app and select a region.
    - Click 'Create app' to initialize it.

- Configure PostgreSQL with ElephantSQL

    - Create and log in to your ElephantSQL account.
    - Click 'Create new instance' on the dashboard.
    - Name your instance and select the 'Tiny Turtle (free)' plan.
    - Choose the data center region that is closest to you.
    - Click 'Review' and then 'Create Instance'.
    - Copy the database URL (beginning with postgres://) from the ElephantSQL dashboard.

- Set Environment Variables on Heroku

    - Return to the Heroku dashboard for your application.
    - Go to the 'Settings' tab and click on 'Reveal Config Vars'.
    - Enter the following environment variables:
    
      - `CLOUDINARY_URL` : Paste the Cloudinary URL you saved earlier.
      - `DATABASE_URL` : Insert the PostgreSQL database URL from ElephantSQL.
      - `SECRET_KEY`: Generate your own secret key.
      - `LOCAL_HOST`: The host address for local development.
      - `HEROKU_HOST`: The host address of your Heroku deployment.
      - `HEROKU_URL`: The base URL for your Heroku application which is used for the CSRF_TRUSTED_ORIGINS.
      - `LOCAL_URL`: URL for local development access which is used for the CSRF_TRUSTED_ORIGINS.
      - `DEV`: A development flag used to indicate if the environment is in development mode.

- Deploy the MemoVault API

    - In the Heroku dashboard, navigate to the 'Deploy' tab.
    - Choose 'GitHub' as your deployment method. Authorize Heroku to connect to GitHub if needed.
    - Search for your repository and click 'Connect'.
    - Optionally, enable 'Automatic Deploys' to redeploy the app automatically when changes are pushed to GitHub.
    - For a manual deployment, select 'main' as the branch and click 'Deploy Branch'.

- Verify Deployment

    - After the deployment process completes, Heroku will provide a link to the deployed application. Monitor the build logs for any errors and ensure the application runs as expected.