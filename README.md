## Steps to Setup

**1. Clone the application**

```bash
git clone https://github.com/coma123/Spring-Boot-Blog-REST-API.git
```

**2. install dependencies**

```bash
pip install -r requirements.txt
```

**3. migrate**

```bash
python manage.py migrate
```

**4. Run**

```bash
python manage.py runserver
```

The app will start running at <http://localhost:8080>

## Explore Rest APIs

The app defines following CRUD APIs.

### Auth

| Method | Url      | Description |
|--------|----------|-------------|
| POST   | /logout/ | Sign up     |
| POST   | /login/  | Log in      |

### Users

| Method | Url                                  | Description                                                                   |
|--------|--------------------------------------|-------------------------------------------------------------------------------|
| GET    | /user/                               | Get logged in user profile                                                    |
| GET    | /api/users/{userid}/                 | Get user profile by username                                                  |
| GET    | /api/users/{userid}/posts            | Get posts created by user                                                     |                                                         |
| POST   | /api/users                           | Add user (Only for admins)                                                    |
| PUT    | /api/users/{userid}                  | Update user (If profile belongs to logged in user or logged in user is admin) |
| DELETE | /api/users/{userid}                  | Delete user (For logged in user or admin)                                     |

### Posts

| Method | Url             | Description                           |
|--------|-----------------|---------------------------------------|
| GET    | /api/posts      | Get all posts                         | 
| GET    | /api/posts/{id} | Get post by id                        | 
| POST   | /api/posts      | Create new post (By logged in user)   |
| PUT    | /api/posts/{id} | Update post (If is owner or is admin) |
| DELETE | /api/posts/{id} | Delete post (If is owner or is admin) |

### Comments

| Method | Url                               | Description                                                                                   |
|--------|-----------------------------------|-----------------------------------------------------------------------------------------------|
| GET    | /api/posts/{postId}/comments      | Get all comments which belongs to post with id = postId                                       | 
| GET    | /api/posts/{postId}/comments/{id} | Get comment by id if it belongs to post with id = postId                                      |
| POST   | /api/posts/{postId}/comments      | Create new comment for post with id = postId (By logged in user)                              |
| PUT    | /api/posts/{postId}/comments/{id} | Update comment by id if it belongs to post with id = postId (If is comment owner or is admin) |
| DELETE | /api/posts/{postId}/comments/{id} | Delete comment by id if it belongs to post with id = postId (If is comment owner or is admin) |

## Sample Valid JSON Request Body

##### <a id="signup">User Registration-> /registration</a>

```json
{
  "username": "test_user",
  "password1": "test_pass",
  "password2": "test_pass",
  "email": "test@test.com"
}
```

##### <a id="signin">Log In -> /login</a>

```json
{
  "username": "test_user",
  "password": "test_pass"
}
```

##### <a id="userupdate">Update User -> /api/users/{username}</a>

```json
{
  "firstName": "mohammad",
  "lastName": "mohammadi",
  "username": "test_username",
  "password": "updatedpassword",
  "email": "mohammad.mohammadi@gmail.com"
}
```

##### <a id="postcreate">Create Post -> /api/posts</a>

```json
{
  "title": "test tile",
  "body": " this is a body."
}
```

##### <a id="postupdate">Update Post -> /api/posts/{id}</a>

```json
{
  "title": "updated title",
  "body": "UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED "
}
```

##### <a id="commentcreate">Create Comment -> /api/posts/{postId}/comments</a>

```json
{
  "body": "this is a comment"
}
```

##### <a id="commentupdate">Update Comment -> /api/posts/{postId}/comments/{id}</a>

```json
{
  "body": "UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED UPDATED "
}
```