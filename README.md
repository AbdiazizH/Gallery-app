Gallery-app

# Description
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.

Live Link
Click to visit the webite

User Story
View different photos that interest them
Click a single image to expand it and view the details of that photo
Search for different categories
View photos based on the location they were taken.
Setup and Installation
To get the project .......

1.Cloning the repository:

git clone :https://github.com/AbdiazizH/Gallery-app.git

2.Navigate into the folder and install requirements
cd Gallery-app pip install -r requirements.txt   
3.Install and activate Virtual

python3 -m venv virtual - source virtual/bin/activate
Install Dependencies
4.pip install -r requirements.txt

5.Setup Database
SetUp your database User,Password, Host then make migrate
python manage.py makemigrations app

Now Migrate

python manage.py migrate

6.Run the application
python manage.py runserver

7.Running the application
python manage.py server 

8. Testing the application

python manage.py test

Technology used
Python3.8
Django 1.11.17
Heroku

Author
Abd Hussein

License
Copyright (c) 2021 AbdiazizH