import configparser
import os
from typing import List, Dict, Any

from langchain import LLMChain
from langchain import OpenAI
from langchain.chains.base import Chain
from langchain.prompts.prompt import PromptTemplate
from pydantic import BaseModel

config = configparser.ConfigParser()
config.read('config.ini')
os.environ["OPENAI_API_KEY"] = config.get('API_KEYS', 'OPENAI-API_KEY')
