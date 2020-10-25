# Go Out Safe

This is the source code of GoOutSafe application, a
project of *Advanced Software Engineering* course,
University of Pisa.
 
## Team info

- The *squad id* is **4**
- The *team leader* is *TBD*

#### Members

|Name and Surname  | Email                         |
|------------------|-------------------------------|
|Federico Silvestri|f.silvestri10@studenti.unipi.it|
|Leonardo Calamita |                               |
|Chiara Boni       |c.boni5@studenti.unipi.it      |
|Nunzio Lopardo    |n.lopardo@studenti.unipi.it    |
|Paolo Murgia      |p.murgia1@studenti.unipi.it    |
|Usman Shahzad     |u.shahzad1@studenti.unipi.it   |


### Diagrams
We have created the Class Diagram using UML to simplify
and document the project.

[Class Diagram schema](https://app.diagrams.net/#G1fXT6PbLfamFTwbCxVI-jCJrf9b1DjUMB)

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
