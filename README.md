# Simple Logging Site using Flask

This is a simple Flask application that allows you to save and retrieve log data and data entries. The application provides endpoints to save log data and data entries via HTTP POST requests and retrieve them via HTTP GET requests.

## Usage

1. Run the Flask application:

   ```bash
   python app.py

- The application will run on http://localhost:5000/.

- Interact with the application using the following endpoints:

    - `POST /logs`: Save log data.
    - `GET /logs`: Retrieve log data.
    - `POST /data`: Save data entries.
    - `GET /data`: Retrieve data entries.
    - `GET /show`: Display contents of log and data files in a web page.

## Customization

- File Names:

    - You can modify the file names by editing the values of the `LOGS_FILE` and `DATA_FILE` variables in the `app.py` file.


## Deploying to a Website

You can easily deploy this Flask application to a website, allowing you to access and use the application through your website's domain. Once deployed, you can access the application by visiting your site's URL, such as http://yoursite.domain.
