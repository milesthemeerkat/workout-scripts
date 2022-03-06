# workout-scripts

A simple set of scripts for computing data from work outs. Coming soon!

### Installation
This project is built with Python 3.7. It's recommended you create a virtual environment of Python 3.7 to install the project.

### Docker setup

1) Install docker on your system
2) `docker build -t workout-scripts .` in the main directory.
3) `docker run -it --rm workout-scripts` to launch the application.

### Local build
Install the requirements:
`pip install -r requirements.txt`

After installing the requirements, it's recommended to setup commit hooks:
`pre-commit install`

This will run each added or changed file with every commit through linters. If all goes well, you should see the following after a good commit:
```
black....................................................................Passed
Flake8...................................................................Passed
pylint...................................................................Passed
```
If `black` detects necessary changes, it will update the file automatically!

Finally, you can launch the main script:
`python main.py`

### Running unit tests
`python -m unittest discover -s tests` in the main directory.