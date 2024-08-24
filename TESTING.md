# Testing for MemoVault API

## Overview 

A series of manual and automated testing as well as validation for the MemoVault API were executed. They cover different aspects, endpoints and edge cases.


## Manual Testing

### Posts endpoints

#### /posts/ - GET


An unauthenticated user can see the list of posts, but can't create a post.

Please note that the value for `profile_image` and `image` will be the cloudinary url to which the image was uplaoded or the cloudinary url of the placeholder images

The values for `is_owner` and `is_admin` should be `false` for the unauthenticated user.

![test-1](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-1.png)

RESULT: PASS


#### /posts/ - GET

The value of the `post_like_id` field should be set to the id of the post like if the request user has liked the post.

![test-44](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-44.png)

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

![test-2](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-2.png)

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

![test-3](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-3.png)


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

![test-5](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-5.png)

RESULT: PASS


#### /posts/<id:int>/ - GET 


When an unauthenticated user sends a GET request to this endpoint, details for the specific post should be returned.

`is_owner` and `is_admin` should be set to `false`


![test-7](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-7.png)

RESULT: PASS


When an authenticated user that is the owner but not an admin sends a GET request to this endpoint, details for the specific post should be returned with slight change this time.

`is_owner` should be set to `true` and `is_admin` should be set to `false`


![test-8](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-8.png)

RESULT: PASS


When an authenticated user that is not the owner but is an admin sends a GET request to this endpoint, details for the specific post should be returned with slight change this time.

`is_owner` should be set to `false` and `is_admin` should be set to `true`


![test-9](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-9.png)

RESULT: PASS

When an authenticated user that is both the owner and an admin sends a GET request to this endpoint, details for the specific post should be returned with slight change this time.

`is_owner` should be set to `true` and `is_admin` should be set to `true`


![test-10](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-10.png)
RESULT: PASS


### /posts/<id:int>/ - PUT


- Unauthenticated users cannot send PUT requests to this endpoint.

Screenshot: N/A   

RESULT: PASS

- An authenticated user that is not the owner or the admin cannot send a PUT request to this endpoint.

Screenshot: N/A   

RESULT: PASS

- An authenticated user that is both the owner and an admin can send a PUT request to this endpoint being able to update one or both of the `title` and `content` fields and optionally the image field.

JSON SENT:

```
{
    "title": "admin's first post",
    "content": "This is a post by an admin!",
    "image": "string (optional)" 
}
```

![test-11](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-11.png)

RESULT: PASS

- An authenticated user that is the owner but not an admin can send a PUT request to this endpoint being able to update one or both of the `title` and `content` fields and optionally the image field.


JSON SENT:

```
{
    "title": "norms first post",
    "content": "This is a post by Norm",
    "image": "string (optional)" 
}
```

![test-12](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-12.png)

RESULT: PASS

- An authenticated user that is not the owner but is an admin can send a PUT request to this endpoint being able to update one or both of the `title` and `content` and optionally the image field.

JSON SENT:

```
{
    "title": "norms first post",
    "content": "This is Norm's post !",
    "image": "string (optional)" 
}
```


![test-13](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-13.png)

RESULT: PASS

### /posts/<id:int>/ - DELETE

- An unauthenticated user cannot send a DELETE request to this endpoint.

Screenshot: N/A 

RESULT: PASS  

- An authenticated user that is not the owner or the admin cannot send a DELETE request to this endpoint.

Screenshot: N/A 

RESULT: PASS  


- An authenticated user that is both the owner and an admin can send a DELETE request to this endpoint.


![test-14](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-14.png)


RESULT: PASS


- An authenticated user that is the owner but not an admin can send a DELETE request to this endpoint


![test-15](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-15.png)

RESULT: PASS

- An authenticated user that is not the owner but is an admin can send a DELETE request to this endpoint


![test-16](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-16.png)

RESULT: PASS

### /posts/<id:int>/ GET - 404 Not Found

Any user trying to find a post that doesn't exist, a 404 Not Found should be returned.


![test-17](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-17.png)


RESULT: PASS

### Comments endpoints

#### /comments/ - GET


- An unauthenticated user can see the list of comments, but can't create a comment.


![test-18](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-18.png)

RESULT: PASS


- An authenticated user sending a POST request to this endpoint with the following JSON data should create a comment.

JSON SENT:

```
{
    "post": "1",
    "content": "lovely post"
}
```


![test-19](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-19.png)

RESULT: PASS



#### /comments/ - GET

The value of the `comment_like_id` field should be set to the id of the comment like if the request user has liked the comment.


![test-46](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-46.png)

RESULT: PASS


#### /comments/<id:int>/ - GET 


When an unauthenticated user sends a GET request to this endpoint, details for the specific comment should be returned.

Values for `is_owner` and `is_admin` should be set to `false`



![test-21](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-21.png)

RESULT: PASS


When an autheticated user that is the owner but not an admin sends a GET request to this endpoint, details for the specific comment should be returned with slight change this time.

`is_owner` should be set to `true` and `is_admin` should be set to `false`


![test-22](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-22.png)

RESULT: PASS


When an authenticated user that is not the owner but is an admin sends a GET request to this endpoint, details for the specific comment should be returned with slight change this time.

`is_owner` should be set to `false` and `is_admin` should be set to `true`


![test-23](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-23.png)

RESULT: PASS

When an authenticated user that is both the owner and an admin sends a GET request to this endpoint, details for the specific comment should be returned with slight change this time.

`is_owner` should be set to `true` and `is_admin` should be set to `true`


![test-24](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-24.png)
RESULT: PASS


#### /comments/ - POST

An authenticated user sending a POST request to this endpoint with the following JSON data can create a post.

JSON Sent:

```
{
    "post": "1",
    "content": "awesome post !"
}
```

![test-25](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-25.png)

RESULT: PASS


- When the authenticated user tries to send a POST request to the endpoint with `content` values missing the validation lets the user know.


JSON SENT:

```
{
    "post": "1",
    "content": ""
}
```


![test-20](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-20.png)

RESULT: PASS


#### /comments/<id:int>/ - PUT


- Unauthenticated users cannot send PUT requests to this endpoint.

Screenshot: N/A  

RESULT: PASS

#### /comments/<id:int>/ - PUT


- An authenticated user that is not the owner or the admin cannot send a PUT request to this endpoint.

Screenshot: N/A  

RESULT: PASS

#### /comments/<id:int>/ - PUT

- An authenticated user that is both the owner and an admin can send a PUT request to this endpoint being able to update the `content` field.


JSON Sent:

```
{
    "post": "1",
    "content": "Your first post is awesome! Really well done!",
}
```

![test-27](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-27.png)

RESULT: PASS

#### /comments/<id:int>/ - PUT


An authenticated user that is the owner but not an admin can send a PUT request to this endpoint being able to update the `content` field.


JSON Sent:

```
{
    "post": "1",
    "content": "Amazing post, really!",
}
```

![test-28](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-28.png)

RESULT: PASS


#### /comments/<id:int>/ - PUT


An authenticated user that is not the owner but is an admin can send a PUT request to this endpoint being able to update the `content` field.


JSON Sent:

```
{
    "post": "1",
    "content": "Amazing post!",
}
```

![test-29](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-29.png)

RESULT: PASS


#### /comments/<id:int>/ - DELETE



- An unauthenticated user cannot send a DELETE request to this endpoint.

Screenshot: N/A  

RESULT: PASS

#### /comments/<id:int>/ - DELETE


- An authenticated user that is not the owner or the admin cannot send a DELETE request to this endpoint.

Screenshot: N/A  

RESULT: PASS


#### /comments/<id:int>/ - DELETE


- An authenticated user that is both the owner and an admin can send a DELETE request to this endpoint.


![test-30](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-30.png)

RESULT: PASS

### /comments/<id:int>/ - DELETE


- An authenticated user that is the owner but not an admin can send a DELETE request to this endpoint


![test-31](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-31.png)

RESULT: PASS


### /comments/<id:int>/ - DELETE



- An authenticated user that is not the owner but is an admin can send a DELETE request to this endpoint


![test-32](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-32.png)

RESULT: PASS

### /comments/<id:int>/ GET - 404 Not Found

Any user trying to find a comment that doesn't exist, a 404 Not Found should be returned.


![test-33](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-33.png)

RESULT: PASS

### Post Like endpoints

#### /like/post/ GET

An unauthenticated or authenticated user can see the list of post likes, but can't create a like on a post.


![test-34](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-34.png)

RESULT: PASS


#### /like/post/<id:int>/ GET


When an unauthenticated or authenticated user sends a GET request to this endpoint, details for the specific post like should be returned.

![test-36](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-36.png)

RESULT: PASS

#### /like/post/ POST


An authenticated user sending a POST request to this endpoint with the following JSON data can create a post like.


```
{
    "post": "1"
}
```

![test-35](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-35.png)

RESULT: PASS

#### /like/post/ POST

When a user sends a POST request to this endpoint and the user already likes the post a 400 Bad Request will be returned.

![test-74](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-74.png)

RESULT: PASS


#### /like/post/<id:int>/ DELETE


An authenticated user that is the owner can send a DELETE request to this endpoint.

![test-37](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-37.png)

RESULT: PASS

#### /like/post/<id:int>/ GET - 404 Not Found

Any user trying to find a post like that doesn't exist, a 404 Not Found should be returned.

![test-42](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-42.png)

RESULT: PASS


### Comment Like endpoints



#### /like/comment/ GET

An unauthenticated or authenticated user can see the list of comment likes, but can't create a like on a comment.


![test-38](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-38.png)

RESULT: PASS


#### /like/comment/<id:int>/ GET


When an unauthenticated or authenticated user sends a GET request to this endpoint, details for the specific comment like should be returned.

![test-40](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-40.png)

RESULT: PASS

#### /like/comment/ POST

An authenticated user sending a POST request to this endpoint with the following JSON data can create a comment like.


```
{
    "comment": "10"
}
```

![test-39](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-39.png)

RESULT: PASS

#### /like/comment/ POST

When a user sends a POST request to this endpoint and the user already likes the comment a 400 Bad Request will be returned.

![test-75](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-75.png)

RESULT: PASS


#### /like/comment/<id:int>/ DELETE


An authenticated user that is the owner can send a DELETE request to this endpoint.

![test-41](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-41.png)

RESULT: PASS

#### /like/comment/<id:int>/ GET - 404 Not Found

Any user trying to find a comment like that doesn't exist, a 404 Not Found should be returned.

![test-43](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-43.png)

RESULT: PASS


### Profiles endpoints

#### /profiles/ - GET


An unauthenticated or authenticated user can see the list of profiles.


![test-48](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-48.png)

RESULT: PASS


#### /profiles/<id:int>/ - GET 

When an unauthenticated or authenticated user sends a GET request to this endpoint, details for the specific profile should be returned.


![test-49](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-49.png)

RESULT: PASS


When an authenticated user sends a GET request to this endpoint, details for the specific profile should be returned with slight change in the returned values for some of the fields.

If the user is looking at a different users profile and the owner of the profile is following the requesting user the value of `follows_you` should be set to true and the value of `following_id` should be set to the id of the follow relationship if the requesting user is following the profile's owner otherwise it will be `null`.

Here norm is following admin but admin is not following norm.

![test-50](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-50.png)

RESULT: PASS


Here norm is not following admin and admin is not following norm


![test-51](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-51.png)

RESULT: PASS


Here Norm is not following admin but admin is following norm

![test-52](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-52.png)

RESULT: PASS


### /profiles/<id:int>/ - PUT


- Unauthenticated users cannot send PUT requests to this endpoint.

Screenshot: N/A  

RESULT: PASS

- An authenticated user that is not the owner cannot send a PUT request to this endpoint.

Screenshot: N/A  

RESULT: PASS


### /profiles/<id:int>/ - PUT


The authenticated owner of the profile can update any of the following fields (All optional)

`name` 
`hobbies` 
`bio` 
`image` 


JSON Sent:

```
{
    "name": "nick",
    "hobbies": "working out, music, books",
    "bio" : "Hello from the admin",
    "image: ""
}
```

![test-53](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-53.png)

RESULT: PASS


The bellow example is with every field being empty

JSON Sent:

```
{
    "name": "",
    "hobbies": "",
    "bio" : "",
    "image: ""
}
```



![test-54](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-54.png)

RESULT: PASS


### /profiles/id - DELETE


- Scheduled to be included in future implementations

#### /profiles/<id:int> GET - 404 Not Found

When a user tries to send a GET request to this endpoint with an id of a profile that doesn't exist a 404 Not Found will be returned.

![test-62](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-62.png)

RESULT: PASS


### Reports endpoints


#### /reports/ - GET


Unauthenticated users cannot access this endpoint


![test-55](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-55.png)

RESULT: PASS


#### /reports/ - GET

Authenticated users can access only the reports that they have created.


![test-56](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-56.png)


RESULT: PASS

#### /reports/<id:int>/ - GET

Unauthenticated users cannot access this endpoint

![test-81](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-81.png)

RESULT: PASS

#### /reports/<id:int>/ - GET

When an authenticated user tries to access a report with an id that doesn't belong to them, 404 Not Found will be returned.

![test-57](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-57.png)

RESULT: PASS

#### /reports/<id:int>/ - GET


When an authenticated user tries to access a report with an id that belongs to them, details for the specific report should be returned.

![test-58](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-58.png)

RESULT: PASS


#### /reports/<id:int>/  - GET

When an authenticated user tries to send a GET request to this endpoint with an id of a report that doesn't exist a 404 Not Found will be returned


![test-73](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-73.png)

RESULT: PASS

#### /reports/<id:int>/ - POST

An authenticated user can create a report. If the user selects any of the reasons except 'Other', the custom reason field is optional.


JSON Sent:

```
{
    "post": "7",
    "reason": "spam",
    "custom_reason" : ""
}
```

![test-59](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-59.png)

RESULT: PASS

#### /reports/<id:int>/ - POST

An authenticated user can create a report. If the user selects 'Other' from the reasons dropdown, the custom reason field becomes required and an HTTP status of 400 Bad Request is returned when it is left empty.


JSON Sent:

```
{
    "post": "8",
    "reason": "other",
    "custom_reason" : ""
}
```

![test-60](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-60.png)

RESULT: PASS

#### /reports/<id:int>/ - POST

An owner of a post cant report their own post

![test-80](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-80.png)

RESULT: PASS

#### /reports/<id:int>/  - PUT


An authenticated user can send a PUT request to this endpoint with the id of a report that they own.


JSON Sent:

```
{
    "post": "7",
    "reason": "inappropriate",
    "custom_reason" : ""
}
```

![test-61](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-61.png)

RESULT: PASS


#### /reports/id - DELETE

An authenticted owner of a report can send a DELETE request to this endpoint, deleting the report.



![test-64](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-64.png)

RESULT: PASS


#### /reports/<id:int>/  - GET NOT FOUND

When an authenticated user tries to send a GET request to this endpoint with an id of a report that doesn't exist a 404 Not found is returned.


![test-63](https://github.com/devnickocodes/memovault-api/blob/main/testing_docs/test-63.png)

RESULT PASS