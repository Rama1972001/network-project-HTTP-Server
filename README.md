# network project HTTP Server
This is a simple HTTP server written in Python that uses the socket library to listen on a specified port (in this case, 9000) for incoming connections.

## Getting Started
* To use this code, you will need to have Python installed on your machine.
* You will also need to have a web browser installed to test the server.
## Installation
1. Download the code files to your machine.
2. Open a terminal and navigate to the directory where the files are located.
## Usage
* Run the server by executing the command python server.py in your terminal
* Open your web browser and navigate to http://localhost:9000/
* You will see the contents of the main_en.html file displayed in your browser.
* You can also navigate to http://localhost:9000/en to see the contents of the main_en.html file
* You can also navigate to http://localhost:9000/ar to see the contents of the main_ar.html file
* you can also navigate to http://localhost:9000/StyleSheet1.css to see the contents of the StyleSheet1.css file
* you can also navigate to http://localhost:9000/StyleSheet2.css to see the contents of the StyleSheet2.css file
* you can also navigate to http://localhost:9000/P2.jpg to see the image P2.jpg file
## File Structure
* This code uses two HTML files, two CSS files and one image file.
* The HTML files are "main_en.html" and "main_ar.html" for english and arabic languages respectively.
* The CSS files are "StyleSheet1.css" and "StyleSheet2.css" for styling.

## Features
* When the client requests the root URL ("/") or the "/en" URL, the server sends the "main_en.html" file.
* Similarly, when the client requests the "/ar" URL, the server sends the "main_ar.html" file.
* If the client requests a file with a ".css" extension, the server sends the corresponding CSS file.
* If the client requests an image with a ".jpg" extension, the server sends the corresponding image.
* In case of any other file, it sends the appropriate response.
## Built With
* Python
* socket library
## Notes
In addition to the socket library, the code also imports the re and webbrowser libraries, but they are not used in this code.
This is a basic HTTP server and it should not be used in production environments.
