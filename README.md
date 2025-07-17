# My Moose Project 🚀

This is a Django project for managing posts, categories, contact and comments.

## Technologies
- Python
- Django
- SQLite

## Installation

```bash
git clone https://github.com/Ibrohim2006/moose.git
cd moose
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
