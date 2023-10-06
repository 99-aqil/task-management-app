# Sentiment Analysis API Documentation

## Introduction

The Sentiment Analysis API is a web application that allows users to analyze the sentiment of text input. It leverages a pre-trained machine learning model to determine whether the sentiment is positive, negative, or neutral. This documentation provides an overview of the project's architecture, API endpoints, usage examples, installation instructions, and customization options.

## Table of Contents

- [Architecture](#architecture)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Handling Errors](#handling-errors)
- [Installation](#installation)
- [Customization](#customization)
- [Conclusion](#conclusion)

## Architecture

The Sentiment Analysis API is built using the Django framework, which follows the Model-View-Controller (MVC) architectural pattern. The project structure consists of the following components:

- **Models**: The application does not have any custom models as it mainly focuses on integrating a pre-trained sentiment analysis model.
- **Views**: Contains the logic for handling HTTP requests, processing input, and generating responses.
- **Templates**: Holds HTML templates for rendering frontend views.
- **URLs**: Defines the routing configuration for different endpoints.
- **Static Files**: Stores static assets such as CSS and JavaScript files.

The API integrates a pre-trained sentiment analysis model from the "setfit" library to perform sentiment analysis on the input text.

## API Endpoints

### Analyze Endpoint

- **Endpoint**: `/analyze/`
- **Method**: POST
- **Request Payload**:
  - JSON object with the following structure:
    ```json
    {
        "text": "Text to be analyzed"
    }
    ```
- **Response**:
  - JSON object with the following structure:
    ```json
    {
        "sentiment": "positive/negative/neutral"
    }
    ```

## Usage Examples

Here are a few examples to demonstrate how to use the Sentiment Analysis API:

### Analyzing Sentiment

**Request:**

```http
POST /analyze/ HTTP/1.1
Content-Type: application/json

{
    "text": "I loved the spiderman movie!"
}
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "sentiment": "positive"
}
```

## Handling Errors

If there is an error during the analysis process or if the request payload is invalid, the API will respond with an appropriate error message.

**Request:**

```http
POST /analyze/ HTTP/1.1
Content-Type: application/json

{
    "text": ""
}
```

**Response:**

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "error": "Empty text provided"
}
```
## Installation

To run the Sentiment Analysis API locally, follow these steps:

1.  Clone the project repository from GitHub.
  ```
  git clone https://github.com/99-aqil/spekter-gmbh.git
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
  cd spekter_gmbh
  ```
6.  Run database migrations:
  ```
  python manage.py migrate
  ```
7.  Start the development server:
  ```
  python manage.py runserver
  ```
8.  Open a new terminal while the existing Django server is running and change into the client directory:
  ```
  cd client
  ```
9.  Run the program to test the api and you may customize the input text at payload:
  ```
  python client.py
  ```
10.  Access the landing page at http://localhost:8000/ and the API at http://localhost:8000/analyze/

## Customization

The Sentiment Analysis API can be customized to fit specific requirements. Here are a few customization options:

- **Model Selection**: The API currently uses the "setfit" library's pre-trained sentiment analysis model. You can explore other models and libraries to integrate a different sentiment analysis model.
- **Frontend Design**: The HTML template provided in the project can be customized to match your desired frontend design. You can modify the template or create new templates based on your requirements.
- **Error Handling**: The API currently handles basic errors such as empty text. You can enhance the error handling mechanism to address specific error scenarios and provide more detailed error messages.

Please note that customization options may require additional development and modifications to the existing codebase.

## Conclusion

The Sentiment Analysis API allows users to analyze the sentiment of text input. This documentation provides an overview of the project's architecture, API endpoints, usage examples, installation instructions, and customization options. By following the guidelines provided, users can integrate and utilize the Sentiment Analysis API effectively.
