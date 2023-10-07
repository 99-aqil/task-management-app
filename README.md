# Task Manager with REST API

## Introduction

This task management web application was created with a REST API using Django. The application allows multiple users to create, view, update, and delete tasks. It also utilizes Django templates for rendering views, PostgreSQL for the database, and Django ORM for managing database relations. Additionally, virtual environment and Git was used for proper development practices.

## Table of Contents

- [Architecture](#architecture)
- [API Endpoints](#api-endpoints)
- [Handling Errors](#handling-errors)
- [Installation](#installation)
- [Customization](#customization)
- [Conclusion](#conclusion)

## Architecture

The task management web application is built using the Django framework, which follows the Model-View-Template (MVT) architectural pattern. The project structure consists of the following components:

- **Models**: The project defines a Django model named Task representing tasks in a task management system. It includes fields for user assignment, task title, description, due date, priority level, completion status, creation and update timestamps, an optional task image, and a corresponding thumbnail image. The model also offers several methods: formatted_due_date, formatted_created_at, and formatted_updated_at for formatting date and time information; get_image and get_thumbnail to retrieve image URLs with optional thumbnail generation; and make_thumbnail to create thumbnails from the associated image.
- **Views**: Contains the logic for handling HTTP requests, processing input, and generating responses.
- **Templates**: Holds HTML templates for rendering frontend views.
- **URLs**: Defines the routing configuration for different endpoints.
- **Static Files**: Stores static assets such as CSS and JavaScript files.

## API Endpoints

### Analyze Endpoint

- **Endpoint**: `/`
- **Method**: GET
- **Response**:
  - JSON object with the following structure:
    ```json
    {
      {
          "user": 1,
          "id": 16,
          "title": "Arek Task",
          "description": "Kono akta description",
          "due_date": "2023-10-28T23:59:00Z",
          "priority": "high",
          "completed": false,
          "created_at": "2023-10-07T02:59:37.975472Z",
          "updated_at": "2023-10-07T02:59:38.105893Z",
          "image": "/uploads/uploads/antique7.jpg",
          "get_image": "http://127.0.0.1:8000/uploads/uploads/antique7.jpg",
          "get_thumbnail": "http://127.0.0.1:8000/uploads/uploads/uploads/antique7.jpg",
          "formatted_due_date": "October 28, 2023 11:59 PM",
          "formatted_created_at": "October 07, 2023 02:59 AM",
          "formatted_updated_at": "October 07, 2023 02:59 AM"
      },
      {
          "user": 1,
          "id": 13,
          "title": "something",
          "description": "wmd wd",
          "due_date": "2023-10-27T21:30:00Z",
          "priority": "low",
          "completed": true,
          "created_at": "2023-10-06T12:29:35.746601Z",
          "updated_at": "2023-10-07T03:46:27.415431Z",
          "image": "/uploads/uploads/art9.jpg",
          "get_image": "http://127.0.0.1:8000/uploads/uploads/art9.jpg",
          "get_thumbnail": "http://127.0.0.1:8000/uploads/uploads/uploads/antique6_OWhcGkC.jpg",
          "formatted_due_date": "October 27, 2023 09:30 PM",
          "formatted_created_at": "October 06, 2023 12:29 PM",
          "formatted_updated_at": "October 07, 2023 03:46 AM"
      },...
    ```
  
- **Endpoint**: `/viewTask/16/`
- **Method**: GET
- **Response**:
  - JSON object with the following structure:
    ```json
    {
        {
            "user": 1,
            "id": 16,
            "title": "Arek Task",
            "description": "Kono akta description",
            "due_date": "2023-10-28T23:59:00Z",
            "priority": "high",
            "completed": false,
            "created_at": "2023-10-07T02:59:37.975472Z",
            "updated_at": "2023-10-07T02:59:38.105893Z",
            "image": "/uploads/uploads/antique7.jpg",
            "get_image": "http://127.0.0.1:8000/uploads/uploads/antique7.jpg",
            "get_thumbnail": "http://127.0.0.1:8000/uploads/uploads/uploads/antique7.jpg",
            "formatted_due_date": "October 28, 2023 11:59 PM",
            "formatted_created_at": "October 07, 2023 02:59 AM",
            "formatted_updated_at": "October 07, 2023 02:59 AM"
        }
    }
    ```

- **Endpoint**: `/add/`
- **Method**: POST
- **Request Payload**:
  - JSON object with the following structure: Form Dara
- **Response**:
  - JSON object with the following structure:
    ```json
    HTTP 201 Created
    Allow: POST, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "user": 1,
        "id": 19,
        "title": "New Title",
        "description": "Description for new title",
        "due_date": "2023-10-07T12:16:00Z",
        "priority": "medium",
        "completed": false,
        "created_at": "2023-10-07T06:15:02.801727Z",
        "updated_at": "2023-10-07T06:15:02.801727Z",
        "image": "/uploads/uploads/antique2_O14m8Zs.jpg",
        "get_image": "http://127.0.0.1:8000/uploads/uploads/antique2_O14m8Zs.jpg",
        "get_thumbnail": "http://127.0.0.1:8000/uploads/uploads/uploads/antique2_O14m8Zs.jpg",
        "formatted_due_date": "October 07, 2023 12:16 PM",
        "formatted_created_at": "October 07, 2023 06:15 AM",
        "formatted_updated_at": "October 07, 2023 06:15 AM"
    }
    ```

- **Endpoint**: `/search/?search=New+Title`
- **Method**: GET
- **Response**:
  - JSON object with the following structure:
    ```json
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    [
        {
            "user": 1,
            "id": 19,
            "title": "New Title",
            "description": "Description for new title",
            "due_date": "2023-10-07T12:16:00Z",
            "priority": "medium",
            "completed": false,
            "created_at": "2023-10-07T06:15:02.801727Z",
            "updated_at": "2023-10-07T06:15:02.852632Z",
            "image": "/uploads/uploads/antique2_O14m8Zs.jpg",
            "get_image": "http://127.0.0.1:8000/uploads/uploads/antique2_O14m8Zs.jpg",
            "get_thumbnail": "http://127.0.0.1:8000/uploads/uploads/uploads/antique2_O14m8Zs.jpg",
            "formatted_due_date": "October 07, 2023 12:16 PM",
            "formatted_created_at": "October 07, 2023 06:15 AM",
            "formatted_updated_at": "October 07, 2023 06:15 AM"
        }
    ]
    ```
- **Endpoint**: `/filter/?filter_options=in_progress&priority=high&completed=`
- **Method**: GET
- **Response**:
  - JSON object with the following structure:
    ```json
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    [
        {
            "user": 1,
            "id": 16,
            "title": "Arek Task",
            "description": "Kono akta description",
            "due_date": "2023-10-28T23:59:00Z",
            "priority": "high",
            "completed": false,
            "created_at": "2023-10-07T02:59:37.975472Z",
            "updated_at": "2023-10-07T02:59:38.105893Z",
            "image": "/uploads/uploads/antique7.jpg",
            "get_image": "http://127.0.0.1:8000/uploads/uploads/antique7.jpg",
            "get_thumbnail": "http://127.0.0.1:8000/uploads/uploads/uploads/antique7.jpg",
            "formatted_due_date": "October 28, 2023 11:59 PM",
            "formatted_created_at": "October 07, 2023 02:59 AM",
            "formatted_updated_at": "October 07, 2023 02:59 AM"
        }
    ]
    ```

## Handling Errors

If there is an error during the analysis process or if the request payload is invalid, the APIs will respond with an appropriate error message.

**Request:**

```http
POST /add/ HTTP/1.1
Content-Type: application/json

{

}
```

**Response:**

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "error": "Invalid Data"
}
```
## Installation

To run the Task Management app locally, follow these steps:

1.  Clone the project repository from GitHub.
  ```
  git clone https://github.com/99-aqil/mediusware-coding-test.git
  ```
3.  Create a virtual environment:
  ```
  python -m venv venv
  ```
3.  Activate the virtual environment:
  ```
  venv\Scripts\activate
  ```
4.  Install the required dependencies:
  ```
  pip install -r requirements.txt
  ```
5.  Change into the project directory:
  ```
  cd TaskManagement
  ```
6.  Run database migrations:
  ```
  python manage.py migrate
  ```
7.  Start the development server:
  ```
  python manage.py runserver
  ```
8.  Access the landing page at http://localhost:8000/ 

## Customization

The Task Management App can be customized to fit specific requirements. Here are a few customization options:

- **Task Categories and Tags**: Implement task categorization or tagging to help users organize tasks. Allow users to filter and search tasks by categories or tags.
- **Task Sharing and Collaboration**: Add the ability to share tasks with other users. Enable real-time collaboration on shared tasks.
- **Task Reminders and Notifications**: Implement task reminders with email or push notifications. Send notifications for approaching due dates or task updates.
- **Task Comments and Discussions**: Add a comments or discussion section to tasks for communication. Allow users to discuss tasks and collaborate on them.
- **Task Attachments and Links**: Extend task attachments to support various file types (e.g., documents, spreadsheets). Include links or references to external resources or related tasks.
- **Mobile and Cross-Platform Compatibility**: Ensure the application is responsive and works well on mobile devices. Consider developing native mobile apps or progressive web apps (PWAs).

Please note that customization options may require additional development and modifications to the existing codebase.

## Conclusion

In conclusion, the task management project discussed here represents a versatile foundation for creating an efficient and user-friendly task management system. By implementing a range of customizations and enhancements, you can tailor the application to meet the unique needs of your users and organization. Prioritizing user experience, security, performance, and scalability will contribute to a successful and well-received application. Furthermore, maintaining open lines of communication with users, conducting regular testing, and staying vigilant about emerging technologies and best practices will ensure the project's continued growth and success. With a commitment to continuous improvement and a keen focus on user satisfaction, this project has the potential to evolve into a highly effective and indispensable tool for task management and productivity.
