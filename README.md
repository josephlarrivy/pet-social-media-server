# Server Setup for a Social Media Site for Pets

Written and maintained by:   [www.josephlarrivy.com](https://joseph-larrivy-portfolio.herokuapp.com/)


### Features
- Creating users, pets, pet types
- Retrieving data about users and their pets


# Endpoints
This backend has endpoints for users, pets, types of pets
##### USERS endpoints
---
POST - create a new user - accepts a json body in the request
```
/users/
```
```
{
    "email" : "test7@email.com",
    "ownerName" : "Test Owner Name",
    "avatar" : "test_avatar",
    "password" : "test_password"
}
```
POST - user login - accepts a json body in the request
```
/users/auth
```
```
{
    "email" : "test7@email.com",
    "password" : "test_password"
}
```
PATCH - update a column in the users table - accepts a json body
```
/users/<user_id>
```
```
{
    "columnName" : "owner_name",
    "newValue" : "Updated Name"
}
```
DELETE - remove a user from the database
```
/users/<user_id>
```
GET - get all information except passwords for all users
```
/users/
```
GET - get all information except password for a specific user by id
```
/users/<user_id>
```


<!-- ##### CATEGORIES endpoints
---
GET - get all categories
```
/categories/
```
GET - get information on a caregory by its id
```
/categories/:id
```
POST - create a new category - accepts a json body in the request
```
/categories/
```
```
{
    "name" : "New Category Name"
}
```
PATCH - updates the name of a category by its id - accepts a json body in the request
```
/categories/:id
```
```
{
    "name" : "Category Name Updated"
}
```
DELETE - remove a category from the database
```
/categories/:id
```


##### TAGS endpoints
---
GET - get all tags
```
/tags/
```
GET - get information on a tag by its id
```
/tags/:id
```
POST - create a new tag - accepts a json body in the request
```
/tags/
```
```
{
    "name" : "New Tag"
}
```
PATCH - updates the name of a tag by its id - accepts a json body in the request
```
/tags/:id
```
```
{
    "name" : "Tag Name Updated"
}
```
DELETE - remove a tag from the database
```
/tags/:id
```

##### QUESTIONS endpoints
---
GET - get all questions
```
/questions/
```
GET - get a question by its id
```
/questions/:id
```
GET - get all questions written by a user
```
/questions/user/:id
```
GET - get all questions in a category
```
/questions/category/:id
```
POST - create a new question - accepts a json body in the request
```
/questions/
```
The json body for a new question must include the question's text, four options in an array, which of the options is the correct answer, the points that the question is worth (as an integer), the id of the creator of the question, and the id of the category to which the question belongs.
```
{
  "text": "Which animal is known as the 'king of the jungle'?",
  "options": [
    "Lion",
    "Tiger",
    "Elephant",
    "Giraffe"
  ],
  "solution": "Lion",
  "points": 10,
  "creator_id": "6493589e86634452bf44bfd1",
  "category_id": "64974bb3709be30cdad26b71"
}
```
PATCH - updates a question by its id - accepts a json body in the request
```
/questions/:id
```
This endpoint is set up so that all fields are required in the request body when any part of the question is going to be changed.
```
{
  "text": "Which animal is known as the 'king of the jungle'?",
  "options": [
    "Lion",
    "Tiger",
    "Elephant",
    "Giraffe"
  ],
  "solution": "Lion",
  "points": 20,
  "creator_id": "6493589e86634452bf44bfd1",
  "category_id": "64974bb3709be30cdad26b71"
}

```
DELETE - remove a question from the database
```
/questions/:id
```

##### QUESTIONTAGS endpoints
---
POST - connects a tag to a question - accepts a json body in the request
```
/questiontags/
```
Include the id of the question and the id of the tag as "questionId" and "tagId" respectively. The database table that the endpoint repesents is a many-to-many relationship where a question can be associated with multiple tags and any given tag can be associated with multiple questions.
```
{
    "questionId" : "649758baae2a8873d89c465e",
    "tagId" : "649751e5796c9e634492529f"
}
```
GET - gets all tags (returning their ids) that are associated with a given question using the question's id
```
/tags/:questionId
```
GET - gets all questions (returning their ids) that are associated with a given tag using the tag's id
```
/questions/:tagId
```
DELETE - remove the association between a tag and a question. Tags and questions will not be affected, only the remationship between them is removed
```
/:questionId/:tagId
``` -->
