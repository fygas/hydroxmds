source activate djansdmx
cd /home/al459/anaconda3/envs/djansdmx/src/sdmx
python manage.py runserver

###Flush database and resete migrations
#sudo su postgres
#psql
#drop database djansdmx;
#create database djansdmx with owner djansdmxuser;
#\q
#exit
#find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
#find . -path "*/migrations/*.pyc" -delete

