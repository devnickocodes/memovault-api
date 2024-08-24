# MemoVault

## Project Goals

MemoVault is a social media backend API that allows users to register, log in, create posts, follow/unfollow other users, like comments and posts as well as comment on posts, manage their profiles, report posts as well as manage their reports. This project is designed to be the foundation for a social media platform. 

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