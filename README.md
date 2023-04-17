# PiDash

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

Finally, you'll start create the Django DB for users and run the server.
```bash

./manage.py makemigrations && ./manage.py migrate
./manaeg.py createsuperuser
# Enter your user and password when prompted.

# Run the server
./manage.py runserver
```