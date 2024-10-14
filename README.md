# store app

## Overview
A REST API for managing stores and items as it supports CRUD operations.

## Features
* Get all stores
* Get a specific store
* Add a new store
* Update a store
* Delete a store
* Get all items
* Get a specific item
* Add a new item
* Delete an item

## Dependencies
- Python 
- Setting up the virtualenv
- Flask

## Setup Instructions
1. Clone the repository:

```bash
git clone https://github.com/maysam-asser/login-app
```

2. Set up a virtual environment:

```bash
virtualenv venv
venv/Scripts/activate       
```
1. Install dependencies:

```bash
pip install Flask
```

4. Run the application:
    
```bash
flask run
```

5. Access the application: Open your browser and navigate to http://127.0.0.1:5000.



## API Endpoints
### Stores
* Get all stores: `GET /stores`
* Get a specific `store: GET /stores/<int:store_id>`
* Add a new store: `POST /stores/add`
* Update a store: `PUT /stores/update/<int:store_id>`
* Delete a store: `DELETE /stores/delete/<int:store_id>`

### Items
* Get all items: `GET /items`
* Get a specific item: `GET /items/<int:item_id>`
* Add a new item: `POST /items/add`
* Delete an item: `DELETE /items/delete/<int:item_id>`


## Postman
<a href="https://web.postman.co/workspace/abe4d4be-76b7-461b-822e-a13d4b89ab87/overview">postman collection url</a>

## Swagger

<img src="scr\Screenshot 2024-10-14 210305.png" width="400"/>

### Items:

* Get all items: `GET /items`

<img src="scr\Screenshot 2024-10-14 211124.png" width="400"/>

* Add a new item: `POST /items/add`

<img src="scr\Screenshot 2024-10-14 211156.png" width="400"/>

<img src="scr\Screenshot 2024-10-14 211219.png" width="400"/>

### Stores:

* Get all stores: `GET /stores`

<img src="scr\Screenshot 2024-10-14 211235.png" width="400"/>

* Get a specific `store: GET /stores/<int:store_id>`

<img src="scr\Screenshot 2024-10-14 211302.png" width="400"/>

<img src="scr\Screenshot 2024-10-14 211323.png" width="400"/>

* Add a new store: `POST /stores/add`

<img src="scr\Screenshot 2024-10-14 211400.png" width="400"/>

<img src="scr\Screenshot 2024-10-14 211414.png" width="400"/>

* Delete a store: `DELETE /stores/delete/<int:store_id>`

<img src="scr\Screenshot 2024-10-14 211429.png" width="400"/>

<img src="scr\Screenshot 2024-10-14 211443.png" width="400"/>

* Update a store: `PUT /stores/update/<int:store_id>`

<img src="scr\Screenshot 2024-10-14 220625.png" width="400"/>

<img src="scr\Screenshot 2024-10-14 220648.png" width="400"/>




