# Octopus Energy technical challenge :

Using Django framework created a management command that can be called with the path of the file to import data from .csv file .

### Requirements :-
    Python>=3.6\
    Django>=3.2\

### Process to Set up Project locally 

Go to the project directory

 * ##### Create virtual environment

   `python version = python3.8 or greater -m venv env`

 * #### Activate environment
    `. env/bin/activate`

 * #### Install requirements
    `pip install -r requirements.txt`

 * #### Run migrations
    `python manage.py makemigrations`

 * #### Migrate the models
    `python manage.py migrate`

* #### To access the django admin site, run the command from terminal and create superuser
  `python manage.py createsuperuser`

* #### Start the server
  `python manage.py runserver`

#### For Local server
Now go to the [localhost:8000](http://127.0.0.1:8000  "localhost")


#### For Admin Panel

Now go to this [localhost:8000/admin/](http://127.0.0.1:8000/admin/  "localhost") and login with the superuser credentials


### Management command
To import and process the records from a csv file, a management command need to be triggered given below.

- `python manage.py import_meterdata --url 'file path'`
 
#### To run the test cases
- `python manage.py test`
