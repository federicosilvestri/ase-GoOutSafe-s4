# ASE - GoOutSafe

### Members

|Name and Surname  | Email                         |
|------------------|-------------------------------|
|Federico Silvestri|f.silvestri10@studenti.unipi.it|
|Leonardo Calamita |l.calamita@studenti.unipi.it   |
|Chiara Boni       |c.boni5@studenti.unipi.it      |
|Nunzio Lopardo    |n.lopardo@studenti.unipi.it    |
|Paolo Murgia      |p.murgia1@studenti.unipi.it    |
|Usman Shahzad     |u.shahzad1@studenti.unipi.it   |


### Instructions

#### Initialization

To setup the project initially you have to run these commands
inside the project's root.

`virtualenv -p python3 venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

#### Run the project

To run the project you have to setup the flask application name,
you can do it by executing the following command:

`export FLASK_APP=monolith/app.py`

and now you can run the application

`flask run`

To **run application** without executing the previous command you can
run the bash script named `run.sh` 
