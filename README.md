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

# Manual Testing Guide for "Caption of the Day" Application

## Posts App Test Cases

### TC1: List Posts as Logged Out User
- **Description**: Verify that logged-out users can list all posts.
- **Preconditions**: User is not logged in.
- **Steps**:
  1. Navigate to the posts listing page.
- **Expected Result**: The user can see a list of posts without being prompted to log in.
- **Actual Result**: The user sees a list of posts without login requirements.

### TC2: Create Post as Logged In User
- **Description**: Verify that logged-in users can create a new post.
- **Preconditions**: User is logged in.
- **Steps**:
  1. Navigate to the create post page.
  2. Fill in the required fields for creating a post.
  3. Submit the form to create a new post.
- **Expected Result**: The post is created successfully, and the user is redirected to a confirmation page or the post's detail view.
- **Actual Result**: The post creation is successful, and user sees a confirmation message.

### TC3: Attempt Post Creation as Logged Out User
- **Description**: Verify that logged-out users cannot create a post.
- **Preconditions**: User is not logged in.
- **Steps**:
  1. Attempt to navigate to the create post page.
- **Expected Result**: The user is redirected to the login page or receives a message indicating that login is required.
- **Actual Result**: The user is redirected to the login page.

### TC4: Retrieve Post with Valid ID as Logged Out User
- **Description**: Verify that logged-out users can retrieve a post using a valid ID.
- **Preconditions**: User is not logged in. Have a valid post ID.
- **Steps**:
  1. Navigate to the detail view of a post using its valid ID.
- **Expected Result**: The user can view the post details without being prompted to log in.
- **Actual Result**: The post details are visible to the user without login.

### TC5: Attempt Retrieval of Post with Invalid ID as Logged Out User
- **Description**: Verify that logged-out users cannot retrieve a post using an invalid ID.
- **Preconditions**: User is not logged in. Have an invalid post ID.
- **Steps**:
  1. Attempt to navigate to the detail view of a post using an invalid ID.
- **Expected Result**: The user receives a 404 Not Found error.
- **Actual Result**: The user encounters a 404 Not Found error.

### TC6: Update Own Post as Logged In User
- **Description**: Verify that logged-in users can update a post they own.
- **Preconditions**: User is logged in and owns at least one post.
- **Steps**:
  1. Navigate to the edit page of a post owned by the user.
  2. Make changes to the post's content.
  3. Submit the updates.
- **Expected Result**: The post is updated successfully, and the user is redirected to a confirmation page or the post's updated detail view.
- **Actual Result**: The post update is successful, and the changes are reflected.

### TC7: Attempt Update on Post Not Owned by Logged In User
- **Description**: Verify that logged-in users cannot update posts they do not own.
- **Preconditions**: User is logged in and does not own the post they attempt to edit.
- **Steps**:
  1. Attempt to navigate to the edit page of a post not owned by the user.
- **Expected Result**: The user is prevented from accessing the edit page or receives a message indicating they do not have permission to edit the post.
- **Actual Result**: The user is denied access to edit the post.

## Comments App Test Cases

### TC1: Create Comment as Logged In User
- **Description**: Verify that logged-in users can create a comment on a post.
- **Preconditions**: User is logged in.
- **Steps**:
  1. Navigate to a post detail view.
  2. Enter a comment in the comment form.
  3. Submit the comment.
- **Expected Result**: The comment is posted successfully, and appears under the post.
- **Actual Result**: The comment is successfully added to the post.

### TC2: Attempt Comment Creation as Logged Out User
- **Description**: Verify that logged-out users cannot create a comment.
- **Preconditions**: User is not logged in.
- **Steps**:
  1. Attempt to navigate to a post and enter a comment.
- **Expected Result**: The user wont see the comment box.
- **Actual Result**: The user does not see a way to comment.

### TC3: Retrieve Comments for a Specific Post
- **Description**: Verify that users can retrieve a list of comments for a specific post.
- **Preconditions**: At least one post with comments exists.
- **Steps**:
  1. Navigate to the detail view of a post.
- **Expected Result**: All comments associated with the post are displayed.
- **Actual Result**: The comments for the post are displayed as expected.

### TC4: Update Own Comment as Logged In User
- **Description**: Verify that logged-in users can update their own comment.
- **Preconditions**: User is logged in and has previously commented on a post.
- **Steps**:
  1. Navigate to the post containing the user's comment.
  2. Find the user's comment and select the option to edit it.
  3. Make changes to the comment and submit the update.
- **Expected Result**: The comment is updated successfully, and the changes are reflected immediately.
- **Actual Result**: The user's comment is updated, and the new content is visible.

### TC5: Attempt Update on Comment Not Owned by Logged In User
- **Description**: Verify that logged-in users cannot update comments they do not own.
- **Preconditions**: User is logged in and attempts to edit a comment not authored by them.
- **Steps**:
  1. Attempt to navigate to a post and edit a comment not authored by the user.
- **Expected Result**: The user is prevented from editing the comment.
- **Actual Result**: The user cannot edit the comment.

### TC6: Delete Own Comment as Logged In User
- **Description**: Verify that logged-in users can delete their own comment.
- **Preconditions**: User is logged in and has previously commented on a post.
- **Steps**:
  1. Navigate to the post containing the user's comment.
  2. Select the option to delete the user's own comment.
- **Expected Result**: The comment is deleted successfully.
- **Actual Result**: The comment is successfully deleted from the post.

### TC7: Attempt Deletion of Comment Not Owned by Logged In User
- **Description**: Verify that logged-in users cannot delete comments they do not own.
- **Preconditions**: User is logged in and attempts to delete a comment not authored by them.
- **Steps**:
  1. Attempt to delete a comment not authored by the user.
- **Expected Result**: The user is prevented from deleting the comment.
- **Actual Result**: The user is unable to delete the comment.

## Likes App Test Cases

### TC1: Like a Post as Logged In User
- **Description**: Verify that logged-in users can like a post.
- **Preconditions**: User is logged in.
- **Steps**:
  1. Navigate to a post.
  2. Click the "Like" button on the post.
- **Expected Result**: The post is liked successfully, and the like count increases.
- **Actual Result**: The like is registered successfully, and the like count for the post increases.

### TC2: Attempt to Like a Post as Logged Out User
- **Description**: Verify that logged-out users cannot like a post.
- **Preconditions**: User is not logged in.
- **Steps**:
  1. Attempt to like a post.
- **Expected Result**: There is no option to like a post as a logged-pout user.
- **Actual Result**: The user cannot like a post if not logged in.

### TC3: Retrieve List of Likes
- **Description**: Verify that users can retrieve a list of likes for a post.
- **Preconditions**: A post with one or more likes exists.
- **Steps**:
  1. Navigate to the detail view of a post.
  2. View the section displaying the likes.
- **Expected Result**: All likes associated with the post are displayed.
- **Actual Result**: The list of likes for the post is correctly displayed.

### TC4: Unlike a Post Previously Liked by Logged In User
- **Description**: Verify that logged-in users can unlike a post they previously liked.
- **Preconditions**: User is logged in and has previously liked a post.
- **Steps**:
  1. Navigate to a post the user has liked.
  2. Click the "Unlike" button.
- **Expected Result**: The post is unliked successfully, and the like count decreases.
- **Actual Result**: The post is successfully unliked, and the decrease in like count is reflected.

### TC5: Prevent Multiple Likes on Same Post by Logged In User
- **Description**: Verify that logged-in users cannot like the same post twice.
- **Preconditions**: User is logged in and has already liked a post.
- **Steps**:
  1. Attempt to like the same post again.
- **Expected Result**: The system prevents a second like or indicates the post is already liked.
- **Actual Result**: The system prevents the user from liking the post again.

## Followers App Test Cases

### TC1: Follow Another User as Logged In User
- **Description**: Verify that logged-in users can follow another user.
- **Preconditions**: User is logged in.
- **Steps**:
  1. Navigate to another user's profile page.
  2. Click the "Follow" button.
- **Expected Result**: The user successfully follows the other user, and the follower count increases.
- **Actual Result**: The user successfully follows the other user, and the follower count increases.

### TC2: Attempt to Follow Users as Logged Out User
- **Description**: Verify that logged-out users cannot follow other users.
- **Preconditions**: User is not logged in.
- **Steps**:
  1. Attempt to follow a user.
- **Expected Result**: The user is not able to follow unless signed in.
- **Actual Result**: The user is not able to follow unless signed in.

### TC3: Retrieve List of Followers
- **Description**: Verify that users can retrieve a list of followers for a user.
- **Preconditions**: A user with one or more followers exists.
- **Steps**:
  1. Navigate to a user's profile page.
  2. View the section displaying the followers.
- **Expected Result**: All followers of the user are displayed.
- **Actual Result**: All followers of the user are displayed.

### TC4: Unfollow a User Previously Followed by Logged In User
- **Description**: Verify that logged-in users can unfollow a user they are following.
- **Preconditions**: User is logged in and is following at least one other user.
- **Steps**:
  1. Navigate to the profile of a user they are following.
  2. Click the "Unfollow" button.
- **Expected Result**: The user successfully unfollows the other user, and the follower count decreases.
- **Actual Result**: The user successfully unfollows the other user, and the follower count decreases.

### TC5: Prevent Following the Same User Twice by Logged In User
- **Description**: Verify that logged-in users cannot follow the same user twice.
- **Preconditions**: User is logged in and is already following a user.
- **Steps**:
  1. Attempt to follow the same user again.
- **Expected Result**: The system prevents a second follow or indicates the user is already followed.
- **Actual Result**: The system prevents the user from following the same user twice.

## Notifications App Test Cases

### TC1: Receive Notification for Post Comment
- **Description**: Verify that notifications are created when a user's post is commented on.
- **Preconditions**: User A's post exists. User B is logged in and comments on User A's post.
- **Steps**:
  1. User B comments on User A's post.
  2. User A checks for notifications.
- **Expected Result**: User A receives a notification about the new comment on their post.
- **Actual Result**: User A receives a notification about the new comment on their post.

### TC2: Receive Notification for Post Like
- **Description**: Verify that notifications are created when a user's post is liked.
- **Preconditions**: User A's post exists. User B is logged in and likes User A's post.
- **Steps**:
  1. User B likes User A's post.
  2. User A checks for notifications.
- **Expected Result**: User A receives a notification about the new like on their post.
- **Actual Result**: User A receives a notification about the new like on their post.

### TC3: Receive Notification for New Follower
- **Description**: Verify that notifications are created when a user gains a new follower.
- **Preconditions**: User A and User B exist. User B is logged in and follows User A.
- **Steps**:
  1. User B follows User A.
  2. User A checks for notifications.
- **Expected Result**: User A receives a notification about the new follower.
- **Actual Result**: User A receives a notification about the new follower.

### TC4: Retrieve List of Notifications
- **Description**: Verify that users can retrieve a list of their notifications.
- **Preconditions**: User has one or more notifications.
- **Steps**:
  1. Navigate to the notifications page.
- **Expected Result**: All notifications for the user are displayed.
- **Actual Result**: All notifications for the user are displayed.

### TC5: Mark Notification as Read
- **Description**: Verify that users can mark a notification as read.
- **Preconditions**: User has one or more unread notifications.
- **Steps**:
  1. Navigate to the notifications page.
  2. Click the "Mark as Read" button for a notification.
- **Expected Result**: The notification is marked as read, and this status is reflected in the interface.
- **Actual Result**: The notification is marked as read, and this status is reflected in the interface.


## Tags App Test Cases

### TC1: List Predefined Tags
- **Description**: Verify that users can list predefined tags.
- **Preconditions**: Predefined tags exist in the system.
- **Steps**:
  1. Navigate to the tags listing page.
- **Expected Result**: The list of predefined tags is displayed.
- **Actual Result**: The list of predefined tags is displayed.

### TC2: API Returns List of Tags with Pagination
- **Description**: Verify that the API returns a list of predefined tags with pagination.
- **Preconditions**: A significant number of predefined tags exist, necessitating pagination.
- **Steps**:
  1. Make an API request to retrieve tags, including pagination parameters if applicable.
- **Expected Result**: The API returns a paginated list of tags.
- **Actual Result**: The API returns a paginated list of tags.

### TC3: Attempt Creating New Tag via POST Request
- **Description**: Verify that attempting to create a new tag via POST request results in a 403 Forbidden.
- **Preconditions**: User is logged in.
- **Steps**:
  1. Attempt to create a new tag by making a POST request to the tags API endpoint.
- **Expected Result**: The request is denied, and a 403 Forbidden status is returned.
- **Actual Result**:  The request is denied, and a 403 Forbidden status is returned.

## Profiles App Test Cases

### TC1: Automatic Profile Creation for New User
- **Description**: Verify that a profile is automatically created for each new user.
- **Preconditions**: A new user registers on the platform.
- **Steps**:
  1. Complete the registration process for a new user.
  2. Check for the creation of a new profile associated with the user.
- **Expected Result**: A new profile is automatically created upon user registration.
- **Actual Result**:  A new profile is automatically created upon user registration.

### TC2: Retrieve Specific Profile
- **Description**: Verify that users can retrieve a specific profile.
- **Preconditions**: Multiple user profiles exist.
- **Steps**:
  1. Navigate to the profile page of a specific user.
- **Expected Result**: The details of the specified user's profile are displayed.
- **Actual Result**: The details of the specified user's profile are displayed.

### TC3: Update Own Profile as Authenticated User
- **Description**: Verify that authenticated users can update their own profile.
- **Preconditions**: User is logged in.
- **Steps**:
  1. Navigate to the user's profile edit page.
  2. Make changes to the profile information.
  3. Submit the updates.
- **Expected Result**: The profile is updated successfully with the new information.
- **Actual Result**: The profile is updated successfully with the new information.

### TC4: Attempt Profile Update by Unauthenticated or Unauthorized User
- **Description**: Verify that unauthenticated or unauthorized users cannot update profiles they don't own.
- **Preconditions**: User is not logged in or attempts to edit another user's profile.
- **Steps**:
  1. Attempt to navigate to the profile edit page of another user.
- **Expected Result**: The user is prevented from accessing the edit page.
- **Actual Result**: The user is prevented from accessing the edit page.


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
