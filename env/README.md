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

## for creating docker container (production)
1. Create dockerfile, .dockerignore and nginx.conf files
2. Create the build file (this avoids running npm install in docker)
3. Create docker-compose.yml file (this will run dockerfile)
4. Create launch.sh shell script to bring up docker-compose file

`sh launch.sh`

## for deploying docker containers in google cloud using Kubernetes
1. Setup account in google app engine
2. Create a project and a bucket
3. Install google cloud SDK
4. Set default configurations like project code and zone in the CLI
5. Login to docker from CLI
6. Tag the 2 images (client and server)
7. Push the images to docker hub with updated tags
8. Create clusters with 2 nodes using glcoud CLI
9. Provide Kubernetes with your docker hub user id and password credentials to pull images
10.Upload the my-graphql-server-pod.yaml using Kubernetes CLI from where this file resides
11.Curl the LoadBalancer Ingress (external ip) IP and verify it is working

## commands for installing and setting up docker images in google cloud
### {} braces refer to your instances like projects, user id, naming etc.
`xcode-select —install`
`glcoud init`
`gcloud config set project {your google cloud project id}`
`gcloud config set compute/zone {google cloud region you selected}`
`gcloud auth configure-docker`
`docker login`
`docker tag mydocker_client:latest {your docker user name}/dockerhub:{myfirstclientimagepush}`
`docker push {your docker user name}/dockerhub:{myfirstclientimagepush}`
`docker tag mydocker_server:latest {your docker user name}/dockerhub:{myfirstserverimagepush}`
`docker push {your docker user name}/dockerhub:{myfirstserverimagepush}`
`gcloud container clusters create mygraphql-cluster --num-nodes=2`
`kubectl create secret docker-registry {provide a credential name here}` `--docker-server=https://index.docker.io/v1/ --docker-username={your docker user name}` `--docker-password={your dockerhub password} --docker-email={email id used for dockerhub}`
`kubectl create -f my-graphql-server-pod.yaml`

## some additional commands for viewing, deleting stuff
`gsutil acl get gs://{your google cloud project url}` to get access control list
`docker rmi {your docker user name}/dockerhub:{myfirstimagepush}` to delete an existing image
`cat ~/.docker/config.json` to view config file from docker. This file has good details
`kubectl get secret {credential name you gave} --output=yaml` to view credentials imported
`kubectl get secret {credential name you gave} --output="jsonpath={.data.\.dockerconfigjson}" | base64 --decode` to decode the base 64 encoded output from previous command
`kubectl delete service mygraphql-service --grace-period=30` to delete a service
`kubectl delete pod mygraphql-container --grace-period=30` to delete a pod
`kubectl get pods` to get details on a pod
`kubectl get service {service name}` to get details on the service
`kubectl describe pods` to get more indepth information on the pod
`kubectl get service mygraphql-service` to view the external ip
`curl {external ip}` to view response

## for deploying application in google app engine
1. Setup account in google app engine
2. Create a project and a bucket
3. Install google cloud SDK
4. Update the app.yaml file
5. Deploy the application 
6. Browse the deployed application using the URL which you can obtain from the terminal after the app is deployed

## commands for deploying the application in google app engine
`gcloud app deploy`
`gcloud app browse `
### some points to note while deploying to google app engine
1. Specify runtime as 'custom' and env as 'flex'
2. When runtime is specified as 'custom', google app engine will look for a dockerfile or docker-compose file to build and run docker
3. App engine is like a 'PaaS' layer while compute engine is a 'IaaS'