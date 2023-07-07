# Server Setup for a Social Media Site for Pets

Written and maintained by:   [www.josephlarrivy.com](https://joseph-larrivy-portfolio.herokuapp.com/)


### Features
- Creating users, pets, pet types
- Retrieving data about users and their pets


# Endpoints
This backend has endpoints for users, pets, types of pets
---
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
GET - get all pets for a specific user by id
```
/users/<user_id>/pets
```
