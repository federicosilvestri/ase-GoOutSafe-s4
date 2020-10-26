# Go Out Safe

This is the source code of GoOutSafe application, self
project of *Advanced Software Engineering* course,
University of Pisa.
 
## Team info

- The *squad id* is **4**
- The *team leader* is *TBD*

#### Members

|Name and Surname  | Email                         |
|------------------|-------------------------------|
|Federico Silvestri|f.silvestri10@studenti.unipi.it|
|Leonardo Calamita |l.calamita@studenti.unipi.it   |
|Chiara Boni       |c.boni5@studenti.unipi.it      |
|Nunzio Lopardo    |n.lopardo@studenti.unipi.it    |
|Paolo Murgia      |p.murgia1@studenti.unipi.it    |
|Usman Shahzad     |u.shahzad1@studenti.unipi.it   |


## Diagrams
We have created the Class Diagram using UML to simplify
and document the project.

[Class Diagram schema](https://app.diagrams.net/#G1fXT6PbLfamFTwbCxVI-jCJrf9b1DjUMB)

## Instructions

#### Initialization

To setup the project initially you have to run these commands
inside the project's root.

`virtualenv -p python3 venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

#### Run the project

To run the project you have to setup the flask application name,
you can do it by executing the following command:

`export FLASK_APP=dev`

and now you can run the application

`flask run`

To **run application** without executing the previous command you can
run the bash script named `run.sh` 

### Apply migrations

If you change something in the models package or you create a new model,
you have to run these commands to apply the modifications:

`flask db migrate -m '<message>'`

and
 
`flask db upgrade`

### Run tests

To run all tests, you execute the following command:

`python -m pytest`

You can also specify a specific test file, in order to run only those specific test.
In case you also want to see the overall coverage of the test, execute the following command:

`python -m pytest --cov=gooutsafe`


## Conventions

- Name of files must be snake_cased
- Name of methods, properties, variables must be snake_cased
- Name of classes must be PascalCased 
- Name of constants must be UPPERCASE 