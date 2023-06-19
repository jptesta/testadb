# testadb

just a small learning project

# Install requirements
python -m venv venv
source venv/bin/activate
pip install -r requiriments.txt


# Migrations
cd src/
flask db init
flask db migrate
flask db upgrade


# Run Application
flask run
