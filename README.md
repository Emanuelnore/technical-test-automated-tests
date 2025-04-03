# Technical Test - Automated tests in EcoRegistry

This projects needs to be finished to pass the technical test. Complete "src/scrapers/http/ecoregistry.py" and ""src/scrapers/selenium/ecoregistry.py".
The complete guide was delivered as a Word document.

## Requirements

This project requires Python 3.11.

**Note:** The system must have Chrome/Chromium browser installed to function properly.

**Note:** There is an environment variable `interactive_mode` that switchs interactive mode: opens a browser window for Selenium processes. Is recommended for debugging. There is a `.env_test` included in the repository. Rename it as `.env`.

## Installation (Windows)

### Create and activate a virtual environment

First, install `virtualenv` if you don't have it:

```
pip install virtualenv
```

Then, create a virtual environment:

```
virtualenv -p 3.11 {virtual_environment_name}
```

### Activate the virtual environment

```
source {virtual_environment_name}/Scripts/activate
```

### Install libraries/dependencies

```
pip install -r requirements.txt
```

## Usage (Windows)

Instructions on how to run the project.

Execute:
```
python -m src.main
```

**Note:** If the environment variables are not being set correctly, execute the following commands:
```
- set -a
- source .env
- set +a
```


