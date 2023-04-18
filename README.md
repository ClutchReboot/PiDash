# PiDash
This project was created to make navigating tiny Raspberry Pi easier.
The idea is to automate minor to advanced tasks with the click of a button using Django as a web app.

## Setup
Currently, PiDash is just a typical Django application.
Because of this the setup is a pretty standard for Django.

```bash
# Clone the repo
git clone git@github.com:ClutchReboot/PiDash.git
```


Next you'll want to create a python environment.
This helps prevent messing with any OS specific installations.
```bash
cd PiDash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
```

Create a personal `.env` file using the `.env_example` file.
```bash
cd pi_dash
cp .env_example .env
```

Generate Django secret token and replace `SuperSecret` in `.env`.

```python
from django.core.management.utils import get_random_secret_key

# generating and printing the SECRET_KEY
print(get_random_secret_key())
```

A custom command `setup` has been created to make the process easier.
During this process, Django's secret key will be generated when the `.env` file is created.
Towards the end, users will be prompted to fill out user information for the django admin account.
```bash

python3 manage.py setup
```