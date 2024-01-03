# Deployment Notes

to create the tables for django to use, this command needs to run just prior to deployment

    python manage.py migrate


if using docker locally, the command can be fed directly to a running docker app container:

    docker exec -it ccv1_app_1 python manage.py migrate

 # SQL Reporting of User Traffic
 can be done via View Tracker and SQL Reporting
 in admin panel, create  a query and give it a good name.

 e.g. for 2 fields 'name' and 'query'

 name

    popular

 query

    select url, count(*) from resumeweb_viewtracker group by url;


  then visit the view tracker page, set the 'name' in the url
  e.g.

    http://localhost:8000/viewtracker-report/?name=popular

  query results should show up on the page.



check which DB I am connected to
-----
./manage.py shell
from django import db
db.connections.databases


how to print env variable
---
import os
print os.environ


run python file as shell executable
-----
say I have a file called hello.py with following
#!/usr/bin/env python
print('hello python')

$ chmod +x hello.py
then run it

$ ./hello.py
https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script



how to switch env variables
----
lenv local.env

check the db values
print_active_env



switch to new db
-------
createdb db0217
psql -d db0217
ALTER USER arifulhaqueimac WITH PASSWORD 'hu8jmn3';
ALTER USER arifulhaqueair WITH PASSWORD 'hu8jmn3';
ALTER USER zotismac WITH PASSWORD 'hu8jmn3';





How to handle data migration issue
-----
relation "prof_cand_imgmsg" already exists
-- migrate app1 zero
-- migrate app1 --fake
-- makemigrations app1
-- migrate app1


relation "......" doesnot exists




nothing happends after migration command




============

docker build -t ........

docker run -p 80:80 REPO_NAME_of_DOCKER_IMG


docker ps


docker stop CONTAINER_ID


once you have all your images, do this


>> create repo for all docker images
aws ecr create-repository --repository-name [REPO_NAME_from_docker_image]

>> get the repo urls
aws ecr describe-repositories --query 'repositories[].[repositoryName, repositoryUri]' --output table
output:
storyizer/save 11998811100.dkr.ecr.us-east-1.aws.com/storyizer/save

now push the docker images to repo
step 1
>> login to ecr 
aws cer get-login --no-include-email | /bin/bash


now, complete the mapping
docker tag storyizer/website:latest 11998811100.dkr.ecr.us-east-1.aws.com/storyizer/website:latest
docker tag storyizer/api:latest 11998811100.dkr.ecr.us-east-1.aws.com/storyizer/api:latest
docker tag storyizer/save:latest 11998811100.dkr.ecr.us-east-1.aws.com/storyizer/save:latest

now, visit the ip address to see the app running

remove images & containers
=========
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker system prune -a --volumes


how to run locally
=========
docker-compose -f infra-v5/local/docker-compose.yml up
docker-compose -f infra-v5/local/docker-compose.yml exec -T webapp python manage.py showmigrations
docker-compose -f infra-v5/local/docker-compose.yml exec -T webapp python manage.py makemigrations
docker-compose -f infra-v5/local/docker-compose.yml exec -T webapp python manage.py migrate
docker-compose -f infra-v5/local/docker-compose.yml exec -T webapp python manage.py showmigrations

docker container ls
docker exec -it ccv1_app python manage.py showmigrations
docker exec -it ccv1_app python manage.py createsuperuser


how to read env file from upper directory
>>>docker-compose -f infra-v3/local/docker-compose.yml --project-directory ./ ../ up
This command didnot work last time


docker with rabbitmq and celery worker
>>>docker-compose -f docker-compose.yml up --scale worker=2 --build


# Credit Card
# ==========
Card Type: Visa
Card Number: 4032036292346820
Expiration Date: 09/2027
CVV: 804

cffi problem
sudo apt-get install libffi-dev
pip3 install -vvv cffi 2>&1 | tee pip.log




# Major functionalities / couldnot implement
# ==========
- elastic search
- redis cache
- 

may need to run with sudo
docker exec -it {container_name} /bin/bash
docker exec -it {container_id} bash
