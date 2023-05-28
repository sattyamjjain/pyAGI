# pyAGI
**pyAGI** is a Python package that functions as an autonomous agent for your Python application. By interfacing with OpenAI models, it utilizes a sequence of prompts to instruct the AI in generating various outputs such as application descriptions, architecture outlines, user experience flows, and even code samples. All these are achieved using the **langchain** framework to construct chains of language models.

## Features
1. Supports several OpenAI models, including a range of GPT-3 and Davinci models.
2. Provides functionality for generating:
   1. Application descriptions
      1. Software architecture outlines
      2. User experience flows
      3. Code flow descriptions
      4. Coding steps
      5. Application code

## Setup
To use pyAGI, you need to have an [OpenAI account](https://www.openai.com/) and obtain your API key. Once you have your OpenAI API key, set it as an environment variable OPENAI_API_KEY in your system.

`export OPENAI_API_KEY='your-api-key-here'`

## Installation

To install pyAGI, use pip:

`pip install pyAGI`

The package is available at PyPI pyAGI (https://pypi.org/project/pyAGI/).

## Usage
After installing, you can use pyAGI to generate content for your application as follows:

```
from pyAGI.pyagi import PyAGI

Create a PyAGI instance with a selected OpenAI model
py_agi = PyAGI.create_llm_chain(selected_model="text-davinci-003")

# Run the PyAGI instance with the objective
py_agi({"objective": "Your Objective", "selected_model": "text-davinci-003"})
```

# Usage without installing the pip package

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

### Upcoming models (https://openai.com/waitlist/gpt-4-api):

- "gpt-4",
- "gpt-4-0314",
- "gpt-4-32k",
- "gpt-4-32k-0314"

Please note that upcoming models will not be supported until released.

## Contributing
Contributions are welcome! Please open an issue if you encounter a bug, or a pull request if you have improvements to the existing code.

## License
This project is licensed under the MIT License.