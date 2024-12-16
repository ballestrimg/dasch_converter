# DaSCH Converter

DaSCH Converter is a lightweight application designed to convert images in `.jpg`, `.jpeg`, and `.png` formats into more optimized and lightweight versions. The app is built using Python's Flask framework and is structured for ease of use, maintainability, and extensibility.

## Features

- Converts `.jpg`, `.jpeg`, and `.png` image formats into lightweight versions.
- User-friendly interface built with Flask and Flask-Bootstrap.
- Modular folder structure for better organization and maintainability.
- Designed to run seamlessly on Ubuntu Linux systems.

## Folder Structure

The application is organized as follows:

```
dasch_converter-main/
|
├── app/            # Main application folder
│   ├── __pycache__/ # Compiled Python files
│   ├── routes/      # Contains Flask route definitions
│   ├── statics/     # Static files such as CSS, JavaScript, and images
│   ├── templates/   # HTML templates for the web interface
│   ├── tests/       # Unit tests for the application
│   ├── __init__.py  # Initializes the Flask application
│   ├── app.py       # Main application logic
│   └── config.py    # Configuration settings for the application
├── LICENSE.md       # MIT License file
├── README.md        # Project documentation
├── requirements.txt # Lists required libraries and dependencies
└── run.py           # Script to start the Flask server
```

## Requirements

To run DaSCH Converter, you need the following dependencies installed:

```
blinker==1.8.1
click==8.1.7
dominate==2.9.1
Flask==3.0.3
Flask-Bootstrap==3.3.7.1
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
numpy==1.26.4
pillow==10.3.0
python-dotenv==1.0.1
visitor==0.1.3
Werkzeug==3.0.3
```

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ballestrimg/dasch_converter.git
   cd dasch_converter
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

5. **Access the App:**
   Open your browser and go to `http://127.0.0.1:5000`.

## Usage

1. Upload an image in `.jpg`, `.jpeg`, or `.png` format via the web interface.
2. The app will process the image and provide a lightweight version for download.

## Running Tests

To ensure the application is functioning correctly, you can run the tests provided in the `tests/` folder:

```bash
pytest tests/
```

## Contribution

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request. Ensure your changes pass all tests before submitting.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ballestrimg/dasch_converter/blob/main/LICENCE.md) file for more details.

