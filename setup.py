from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pyAGI",
    version="1.0.4",
    author="Sattyam Jain",
    author_email="sattyamjain96@gmail.com",
    description="Autonomous agent for building the python app using OpenAI with AGI concept",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/sattyamjjain/pyAGI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=["agi", "pyagi", "autonomous agent", "code agi", "python agi"],
    python_requires=">=3.9",
    install_requires=requirements,
    project_urls={
        "Bug Reports": "https://github.com/sattyamjjain/pyAGI",
        "Source": "https://github.com/sattyamjjain/pyAGI",
    },
)
