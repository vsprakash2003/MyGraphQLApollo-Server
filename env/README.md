# Myapp
My application to record daily reading log

## Requirements
This repo requires python 3 and pip.  To ensure you have python 3 installed, run
```bash
python --version
# You should see "Python 3.6.3" or something similar.
```
### setting up Myapp
Run these commands to install the necessary python packages:
```bash
pip install venv

pip install -r requirements.txt
```

### Initializing the environment
Ensure you have your python virtual environment activated
```bash
. env/bin/activate
or
venv env
cd Myapp
source env/bin/activate
```
```
export FLASK_APP=app.py
export DATABASE_URL="sqlite:///database.sqlite3"
or
update the following in config.py
os.environ['DATABASE_URL'] = 'sqlite:///database.sqlite3
```

### Run migration
```bash
alembic init migration
```

### update alembic.ini to update the database
Update the sqlalchemy.url variable to blank

### update env.py
import os
import sys
sys.path.append(os.getcwd())


config.set_main_option('sqlalchemy.url', os.environ.get('DATABASE_URL'))

from database.database import Base

### Generate alembic revision. This is for manually updating migration scripts
```bash
alembic revision -m "baseline"
```

### To do migration
```bash
alembic upgrade head
```

### Auto-generate migration after changes to the database. If you want alembic to generate migration scripts, use this
```bash
alembic revision --autogenerate -m "{comment}"
```

### To generate alembic script with SQL
```bash
alembic upgrade head --sql
```
### To detect column changes
in env.py, add compare_type=True in context.configure

### For errors while running migration
delete existing version files in __pycache__ and delete relevant files in versions folder

### To insert mock data
python3 data_Setup.py

### Start the application
```bash
python3 ./app.py
```
## Add gitignore file 
   `touch .gitignore`

## Git commands
### for master branch
`git init`
`git add .`
`git commit -m "first commit"`
`git remote add https://github.com/vsprakash2003/MyGraphQLApollo-Server.git`
`git push -u origin master` 

### for coding branch
`git checkout -b origin/c/{branch name}`
`git add .`
`git commit -m "second commit"
`git push -u origin origin/c/{branch name}`

### for merging code branch to master
`git checkout master`
`git pull origin master`
`git merge origin/c/{branch name}`
`git push -u origin master`

## for creating docker container
1. Add gunicorn to requirements.txt (gunicorn is the http server for flask applications)
2. Create dockerfile, .dockerignore and gunicorn_config.py files
3. Create a docker bridge (if not already exists and only if needed. This is to connect 2 containers)
4. Do docker build (this will install all packages from requirements.txt)
5. Run docker container and add to bridge

`docker network create -d bridge Myappbridge`
`docker build . -t python-docker`
`docker run --rm --network=Myappbridge -d -p 5000:5000 --name Myserverdocker python-docker`