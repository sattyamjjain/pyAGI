# pyAGI
**pyAGI** is a Python package designed to create an autonomous agent for your Python application. It interfaces with OpenAI models and uses a chain of prompts to guide the AI in generating a variety of content, including application descriptions, architecture outlines, user experience flows, and even example code. This is accomplished using the langchain framework for creating chains of language models.

## Features
1. Supports several OpenAI models, including a range of GPT-3 and Davinci models.
2. Provides functionality for generating:

## Application descriptions
1. Software architecture outlines
2. User experience flows
3. Code flow descriptions
4. Coding steps
5. Application code

## Installation

To install pyAGI, use pip:

`pip install pyAGI`

## Usage
After installing, you can use pyAGI to generate content for your application as follows:

`python main.py "Objective of your app" "OpenAI Model"`

For example:

`python main.py "Build a weather app" "text-davinci-003"`

## Available Models

### Currently supported models:

- "text-davinci-002",
- "text-davinci-003",
- "gpt-3.5-turbo",
- "gpt-3.5-turbo-0301",
- "text-curie-001",
- "text-babbage-001",
- "text-ada-001"

### Upcoming models:

- "gpt-4",
- "gpt-4-0314",
- "gpt-4-32k",
- "gpt-4-32k-0314"

Please note that upcoming models will not be supported until released.

## Contributing
Contributions are welcome! Please open an issue if you encounter a bug, or a pull request if you have improvements to the existing code.

## License
This project is licensed under the MIT License.