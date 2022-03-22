#!/bin/bash
eval "$(pyenv init -)"
pyenv activate workout-scripts
pytest tests/