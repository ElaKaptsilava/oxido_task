# Article HTML Generator

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies and Tools](#technologies-and-tools)
- [Installation](#installation)
- [Usage](#usage)


## Project Overview
This project generates an HTML file from an article and a prompt using OpenAI's API. The output is saved to a file, 
and the file name can be customized via command-line arguments.

## Features
- Reads input files (prompt.txt and article.txt).
- Uses **OpenAI's API** to generate HTML content.
- Saves the HTML output to a specified file or a default location.

## Technologies and Tools
- **Python**: Backend development with Django.
- **OpenAI API**: For generating messages and insights.
- **HTML/CSS/JavaScript**: Frontend development.

## Installation
1. **Ensure you have Python installed**
2. **Create a .env file and fill in the variables**
   - On Unix-based systems (Linux/macOS)
   ```bash
       cp .env.dist .env
    ```
   - On Windows:
      ```bash
      copy .env.dist .env
      ```
     
3. **Install Dependencies**
   - Follow the instructions on the Poetry installation page.

4. **Set Up Dependencies**
   ```bash
   poetry install
   ```
   ```bash
   poetry shell
   ```
   - Ensure you have Poetry installed correctly and all dependencies are exist (openai, python-dotenv)
   ```bash
   poetry show
   ```
5. **API Key**
   - Update the OpenAI API key in the configuration file (.env)
   ```dotenv
    OPENAI_API_KEY="YOUR-OPENAI_API_KEY"
   ```
## Installation

1. **Running the Script**
   - Run the script run_generator.py from the command line. Use the path argument to specify the output file path
   ```bash
   python run_generator.py -path /path/to/template.html
   ```