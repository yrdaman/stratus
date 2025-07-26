# README for the Flask Backend Server

This is a Flask backend server for the project. It provides the necessary API endpoints to interact with the client application.

## Project Structure

- **app/**: Contains the main application code.
  - **\_\_init\_\_.py**: Initializes the Flask application and sets up the configuration.
  - **routes.py**: Defines the routes for the application.
  - **models.py**: Contains the data models for the application.

- **venv/**: Contains the virtual environment for the project.

- **.gitignore**: Specifies files and directories to be ignored by Git.

- **requirements.txt**: Lists the dependencies required for the project.

- **run.py**: The entry point for running the Flask application.

## Getting Started

To set up the project, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd server
   ```

2. **Install the dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```
   python run.py
   ```

The server will start running on `http://localhost:5000`.

## Usage

You can interact with the API endpoints defined in `routes.py`. Refer to the documentation within that file for details on available routes and their usage.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.