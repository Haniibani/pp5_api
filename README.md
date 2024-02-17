# Caption of the day - API

## Project Description
Caption of the day is a dynamic social media platform designed for users to engage and share their experiences. This platform allows users to create profiles and posts, follow other profiles, like posts, and much more, providing a rich and interactive user experience.

## Epics and User Stories
Our application is built with the following user experiences in mind:

#### Epic: User Management
- **User Story**: Profile Creation for New Users [#2](https://github.com/Haniibani/pp5_api/issues/2)
- **User Story**: Secure Authentication System [#3](https://github.com/Haniibani/pp5_api/issues/3)
- **User Story**: Registration and Personalized Access [#4](https://github.com/Haniibani/pp5_api/issues/4)

#### Epic: Content Management
- **User Story**: Post Creation and Sharing [#5](https://github.com/Haniibani/pp5_api/issues/5)
- **User Story**: Post Management [#6](https://github.com/Haniibani/pp5_api/issues/6)
- **User Story**: Data Record Interactions [#7](https://github.com/Haniibani/pp5_api/issues/7)

#### Epic: Social Interactions
- **User Story**: Liking Posts to Show Appreciation [#8](https://github.com/Haniibani/pp5_api/issues/8)
- **User Story**: Engaging with Community Through Comments [#9](https://github.com/Haniibani/pp5_api/issues/9)
- **User Story**: Following Users for Updates [#10](https://github.com/Haniibani/pp5_api/issues/10)

#### Epic: User Notifications
- **User Story**: Content Interaction Notifications [#11](https://github.com/Haniibani/pp5_api/issues/11)

#### Epic: Content Discovery
- **User Story**: Tagging Posts for Categorization [#12](https://github.com/Haniibani/pp5_api/issues/12)
- **User Story**: Enhanced Post Searchability [#13](https://github.com/Haniibani/pp5_api/issues/13)
- **User Story**: Tag-Based Post Filtering [#14](https://github.com/Haniibani/pp5_api/issues/14)

#### Epic: Platform Compatibility
- **User Story**: Cross-Environment Accessibility [#15](https://github.com/Haniibani/pp5_api/issues/15)

#### Epic: Security and Authentication
- **User Story**: Secure Session Management [#16](https://github.com/Haniibani/pp5_api/issues/16)
- **User Story**: Ensuring Authorized Content Modification [#17](https://github.com/Haniibani/pp5_api/issues/17)

## Entity Relationship Diagram
![Alt Text](/assets/Lucidchart.png)

## Models and CRUD Breakdown
A detailed breakdown of models within the backend:

| Model         | Endpoints                      | Create | Retrieve | Update | Delete | Filter                   | Text Search |
| ------------- | ------------------------------ | ------ | -------- | ------ | ------ | ------------------------ | ----------- |
| User          | /users                         | Yes    | Yes      | Yes    | No     | -                        | -           |
| Profile       | /profiles                      | Yes    | Yes      | Yes    | No     | -                        | Yes         |
| Post          | /posts                         | Yes    | Yes      | Yes    | Yes    | Tags, Likes, Follows     | Yes         |
| Tag           | /tags                          | No     | Yes      | No     | No     | -                        | -           |
| Comment       | /comments                      | Yes    | Yes      | Yes    | Yes    | Post                     | -           |
| Like          | /likes                         | Yes    | No       | No     | Yes    | -                        | -           |
| Follow        | /follows                       | Yes    | Yes      | No     | Yes    | Follower, Followed       | -           |
| Notification  | /notifications                 | Yes    | Yes      | Yes    | No     | User                     | -           |

## Technology Stack
Our backend is powered by a robust stack that ensures efficiency and scalability:
- **Framework**: Django and Django REST Framework for robust API development.
- **Database**: PostgreSQL for reliable and scalable data storage.
- **Authentication**: Utilizes Django's built-in authentication system for secure user authentication.
- **Caching**: Redis for enhancing application performance.
- **Task Queue**: Celery for handling asynchronous tasks and scheduled jobs.

## API Endpoints

### User Endpoints
- **Create User (`POST /users`)**: Register a new user.
- **Retrieve User (`GET /users/{id}`)**: Get details of a specific user.

### Profile Endpoints
- **Create Profile (`POST /profiles`)**: Create a new profile.
- **Retrieve Profile (`GET /profiles/{id}`)**: Get details of a specific profile.
- **Update Profile (`PUT /profiles/{id}`)**: Update an existing profile.

### Post Endpoints
- **Create Post (`POST /posts`)**: Create a new post.
- **Retrieve Post (`GET /posts/{id}`)**: Get details of a specific post.
- **Update Post (`PUT /posts/{id}`)**: Update an existing post.
- **Delete Post (`DELETE /posts/{id}`)**: Remove a specific post.

### Tag Endpoints
- **Retrieve Tag (`GET /tags/{id}`)**: Get details of a specific tag.

### Comment Endpoints
- **Create Comment (`POST /comments`)**: Add a new comment to a post.
- **Retrieve Comment (`GET /comments/{id}`)**: Get details of a specific comment.
- **Update Comment (`PUT /comments/{id}`)**: Update an existing comment.
- **Delete Comment (`DELETE /comments/{id}`)**: Remove a specific comment.

### Like Endpoints
- **Create Like (`POST /likes`)**: Like a post.
- **Delete Like (`DELETE /likes/{id}`)**: Unlike a post.

### Follow Endpoints
- **Create Follow (`POST /follows`)**: Follow a user.
- **Retrieve Follow (`GET /follows/{id}`)**: Get follow details.
- **Delete Follow (`DELETE /follows/{id}`)**: Unfollow a user.

### Notification Endpoints
- **Create Notification (`POST /notifications`)**: Create a new notification.
- **Retrieve Notification (`GET /notifications/{id}`)**: Get details of a specific notification.
- **Update Notification (`PUT /notifications/{id}`)**: Update an existing notification.

## Error Handling
Our API uses standard HTTP status codes to indicate the success or failure of an API request:
- `200 OK`: Successful request.
- `201 Created`: Resource created successfully.
- `400 Bad Request`: The server cannot process the request due to client error.
- `401 Unauthorized`: Authentication is required and has failed or not been provided.
- `403 Forbidden`: The user does not have the necessary permissions.
- `404 Not Found`: The requested resource is not found.
- `500 Internal Server Error`: Unexpected condition encountered on the server.

## Tests
Our testing suite is comprehensive, ensuring that each module functions correctly and as expected. Below are the tests performed for each app within the project:

### Posts App:
- Logged out users can list posts.
- Logged in users can create a post.
- Logged out users can't create a post.
- Logged out users can retrieve a post with a valid ID.
- Logged out users can't retrieve a post with an invalid ID.
- Logged in users can update a post they own.
- Logged in users can't update a post they don't own.

### Comments App:
- Logged in users can create a comment on a post.
- Logged out users can't create a comment.
- Users can retrieve a list of comments for a specific post.
- Logged in users can update their own comment.
- Logged in users can't update comments they don't own.
- Logged in users can delete their own comment.
- Logged in users can't delete comments they don't own.

### Likes App:
- Logged in users can like a post.
- Logged out users can't like a post.
- Users can retrieve a list of likes.
- Logged in users can unlike a post they previously liked.
- Logged in users can't like the same post twice.

### Followers App:
- Logged in users can follow another user.
- Logged out users can't follow users.
- Users can retrieve a list of followers.
- Logged in users can unfollow a user they are following.
- Logged in users can't follow the same user twice.

### Notifications App:
- Notifications are created when a user's post is commented on.
- Notifications are created when a user's post is liked.
- Notifications are created when a user gains a new follower.
- Users can retrieve a list of their notifications.
- Users can mark a notification as read.

### Tags App:
- Users can list predefined tags.
- The API returns a list of predefined tags with pagination.
- Creating a new tag via POST request results in a 403 Forbidden.
- Serializer correctly serializes tag instances with valid data.
- Serializer raises validation errors with empty data.

### Profiles App:
- A profile is automatically created for each new user.
- Profile string representation is correct (username's profile).
- Profile serializer correctly serializes data with valid input.
- Users can list all profiles with pagination.
- Users can retrieve a specific profile.
- Authenticated users can update their own profile.
- Unauthenticated or unauthorized users cannot update profiles they don't own.

Each of these tests are designed to verify the integrity and security of the application, ensuring a reliable and user-friendly experience.

## Future Improvements
We are constantly striving to improve our application. Here are some of the enhancements we plan to implement:
- **Security Enhancements**: Implementing advanced encryption and secure data storage practices.
- **Performance Optimization**: Enhancing server response times and optimizing database queries.
- **Scalability Solutions**: Developing a scalable architecture for growing user numbers and data.
- **User Analytics**: Integrating tools for insights into user behavior.
- **Content Moderation Tools**: Creating tools for maintaining a healthy community environment.
- **Accessibility Support**: Ensuring usability for people with disabilities.
- **Internationalization Support**: Preparing for multi-language and regional settings.
- **API Development**: Building and documenting a robust API for third-party integrations.
- **Data Backup and Recovery**: Establishing backup mechanisms and recovery protocols.
- **User Behavior Insights**: Implementing tracking for feature usage patterns.
- **Role-Based Access Control**: Managing access rights and securing sensitive operations.
- **Automated Testing and QA**: Setting up a framework for maintaining high code quality.
- **Smooth Deployment Pipeline**: Creating a CI/CD pipeline for streamlined deployments.
- **Support System Implementation**: Developing a system to assist users promptly.
- **Regular Maintenance and Updates**: Keeping the system optimized and secure.
- **API Versioning**: Implementing API versioning to manage changes and maintain compatibility.
- **Contribution Framework**: Developing guidelines and processes to encourage and manage community contributions.


## Deployment Steps
To deploy the backend of YourAppName, follow these steps:

- Configure environment variables for database access, secret keys, and other settings.
- Utilize libraries like `psycopg2` and `dj-database-url` for database connections.
- Set up authentication and permissions according to project requirements.
- Configure allowed hosts and CORS settings for secure cross-origin requests.
- Implement JSON as the default renderer for API responses.
- Prepare a `Procfile` for deployment platforms like Heroku, including necessary commands.
- Exclude sensitive configuration files using `.gitignore`.
- Generate a `requirements.txt` file to document project dependencies.
- Proceed with deployment on a platform like Heroku, ensuring all environment variables and configurations are set.

---

We hope you enjoy using Caption of the day!
