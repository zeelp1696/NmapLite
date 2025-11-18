#!/bin/bash

# This script sets up the nmaplite project environment.

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Inform the user that the setup is complete
echo "nmaplite environment setup complete. Activate the virtual environment with 'source venv/bin/activate'."