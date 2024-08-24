# Testing for MemoVault API

## Overview 

A series of manual and automated testing as well as validation for the MemoVault API were executed. They cover different aspects, endpoints and edge cases.


## Manual Testing

### Posts endpoints

#### /posts/ - GET


An unauthenticated user can see the list of posts, but can't create a post.

Please note that the value for `profile_image` and `image` will be the cloudinary url to which the image was uplaoded or the cloudinary url of the placeholder images

The values for `is_owner` and `is_admin` should be `false` for the unauthenticated user.

![test-1]()

RESULT: PASS


#### /posts/ - GET

The value of the `post_like_id` field should be set to the id of the post like if the request user has liked the post.

![test-44]()

RESULT: PASS


#### /posts/ - POST

An authenticated user sending a POST request to this endpoint with the following JSON data can create a post.

Please note that the value of `image` will be the cloudinary url to which the image was uplaoded if no image was chosen it will be the cloudinary url of the placeholder image.

```
{
    "title": "New Test Post",
    "content": "This is a test post.",
    "image": "string (optional)" 
}
```

![test-2]()

Please note now that since the user is authenticated, the owner of the post as well as being the admin both values for `is_owner` and `is_admin` are set to `true` and the `post_like_id` should remain `null` as the admin hasn't liked the post.


RESULT: PASS

#### /posts/ - POST 

When the authenticated user tries to send a POST request to the endpoint with either `title` or `content` values missing the validation lets the user know.


```
{
    "title": "",
    "content": "",
    "image": "string (optional)" 
}
```

![test-3]()


RESULT: PASS

#### /posts/ - POST 

when authenticated user tries to send a POST request to the endpoint with the size of the image being larger than the permitted the validation lets the user know.

The `image`'s size is greater than the permitted.

```
{
    "title": "New Post",
    "content": "This is a new post",
    "image": "string (optional)" 
}
```

![test-5]()

RESULT: PASS


#### /posts/<id:int>/ - GET 


When an unauthenticated user sends a GET request to this endpoint, details for the specific post should be returned.

`is_owner` and `is_admin` should be set to `false`


![test-7]()

RESULT: PASS


When an authenticated user that is the owner but not an admin sends a GET request to this endpoint, details for the specific post should be returned with slight change this time.

`is_owner` should be set to `true` and `is_admin` should be set to `false`


![test-8]()

RESULT: PASS


When an authenticated user that is not the owner but is an admin sends a GET request to this endpoint, details for the specific post should be returned with slight change this time.

`is_owner` should be set to `false` and `is_admin` should be set to `true`


![test-9]()

RESULT: PASS

When an authenticated user that is both the owner and an admin sends a GET request to this endpoint, details for the specific post should be returned with slight change this time.

`is_owner` should be set to `true` and `is_admin` should be set to `true`


![test-10]()

RESULT: PASS

#### /posts/<id:int>/ - GET 

The value of the `post_like_id` field should be set to the id of the post like if the request user has liked the post.

SCREENSHOT test-45

RESULT: PASS