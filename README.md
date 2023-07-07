# Server Setup for a Social Media Site for Pets

Written and maintained by:   [www.josephlarrivy.com](https://joseph-larrivy-portfolio.herokuapp.com/)


### Features
- Creating users, pets, pet types
- Retrieving data about users and their pets


# Endpoints
This backend has endpoints for users, pets, types of pets
---







### USERS endpoints
---
POST - create a new user - accepts a json body in the request
```
/users/
```
```
{
    "email" : "example@email.com",
    "ownerName" : "Example Owner Name",
    "avatar" : "example_avatar",
    "password" : "example_password"
}
```
POST - user login - accepts a json body in the request
```
/users/auth
```
```
{
    "email" : "example@email.com",
    "password" : "example_password"
}
```
DELETE - remove a user from the database
```
/users/<user_id>
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



### PETS endpoints
---
POST - create a new pet - accepts a json body in the request
```
/pets/
```
```
{
    "ownerId" : "user_1",
    "typeId" : "type_3",
    "name" : "Pet One",
    "avatar" : "pet_avatar"
}
```
DELETE - remove a pet from the database
```
/pets/<pet_id>
```
PATCH - update a column in the pets table - accepts a json body
```
/pets/<pet_id>
```
```
{
    "columnName" : "owner_name",
    "newValue" : "Updated Owner Name"
}
```
GET - gets all pets
```
/pets/
```
GET - get information about a pet by its id
```
/pets/<pet_id>
```





### PET TYPES endpoints
---
POST - create a new pet type - accepts a json body in the request with name of the type of pet
```
/types/
```
```
{
    "name" : "lizard"
}
```
DELETE - remove a pet type from the database
```
/types/<type_id>
```
PATCH - update a column in the pet types table - accepts a json body
```
/types/<type_id>
```
```
{
    "columnName" : "type_name",
    "newValue" : "lizard updated"
}
```
GET - gets all pet types
```
/types/
```
GET - get information about a type by its id
```
/types/<type_id>
```