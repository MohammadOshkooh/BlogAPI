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