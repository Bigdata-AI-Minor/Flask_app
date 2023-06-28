# Flask_app

This is a proof of contest application for litter detection that is coupled on the 'Stadjutters' program. This repo contain the material prediction of litter pictures in jpg or png format.

The platform of this repo is created in a Linux environment with pip and python3.9 version installed. Below are the commands for installing the dependencies and virtual environment with database. There will be test user with the username and password 'test' for testing purposes if your are making a migration. The model for prediction is not delivered with this repository and it is advised to use a YOLOv5 model with it.

There are 2 ways for setting up the environment, by docker or individual stack. 
# Docker
https://www.docker.com/products/docker-desktop/ You can download docker from the link and after creating an account, you need to open the a terminal. That can be the CMD or VSCode terminal (shortkey: ctrl + `) where you can download from here https://code.visualstudio.com/download. after that open the project from the root and type into the terminal: 

```sh
docker-compose up --build
```

after the build you would see in docker a new container called 'flask_app' with 2 

```sh
http://localhost:5000/
```
# Individual stack

For running this back-end application you need Python3.9 and Pip. For installing that here:
```sh
pip
https://pip.pypa.io/en/stable/installation/
python3.9 
https://www.youtube.com/watch?v=uDbDIhR76H4
https://www.python.org/downloads/
```

When both are working you can download the repository and run the application by setting the virtual environment and installing the packages for the application. 

Create from the root folder of this project a virtual environment: 
```sh
virtualenv env
```

Activate the environment: 
```sh
source ./env/bin/activate
```
You should now be inside (venv)

Install dependencies:
```sh
python3.9 -m pip install -r requirements.txt
```

Start the flask application: 
```sh
flask run
```

Install the libraries in env (example flask but needs to change to actual libs): 
```sh
python3.9 –m pip install flask
```

At any time save all dependencies we use: 
```sh   
python3.9 –m pip freeze > requirements.txt
```

Export flask application as env variable:
```sh
export FLASK_APP=manage.py

flask db init

flask db migrate

flask db upgrade
```

fof prediction you need to place the pytorch model in the torch folder with the name model.pt:
```sh
- application 
    - main
        - torch_model
            - model.pt
```

The model could be find in the research drive with the name of "epochs300_yolo5m_fullData_hypScratch_v2_gen2", in here you can find the weights with the best or last model that is generated in this session.
