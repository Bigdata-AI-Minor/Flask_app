# Flask_app
This is a proof of contest application for litter detection that is coupled to the 'Stadjutters' program. This repo contains the backend and material prediction of litter pictures in jpg or png format. This repository only contain the backend system of the proof of concept application. The prediction is also done as a service with the detection functioned usd from the YOLOv5 algorithm. So only pytorch model will work with this.

for prediction you need to place the pytorch model in the torch folder with the name model.pt:
```sh
- application 
    - main
        - torch_model
            - model.pt
```

The model could be find in the research drive with the name of "epochs300_yolo5m_fullData_hypScratch_v2_gen2", in here you can find the weights with the best or last model that is generated in this session.

There are 2 ways for setting up the environment, by docker or individual stack. Depending on the stack, you need to change 1 line of code. This is because of the nature of routing files between a docker container and a native ubuntu environment. That line is:
```sh
-> application
    -> main
        -> service
            -> Prediction_service.py
                # use this path in native linux environment 
                # path = f'{os.path.dirname(__file__)}/../torch_model/model.pt'
                
                # use this path in docker environment 
                path = f'{os.path.dirname(__file__)}/../../../torch_model/model.pt'
```

Depending on the environment you want to run, command the other line out with a '#' character on the start of the line.

# Docker
https://www.docker.com/products/docker-desktop/ You can download docker from the link and after creating an account, you need to open the terminal. That can be the CMD or VSCode terminal (shortkey: ctrl + `) where you can download from here https://code.visualstudio.com/download. after that open the project from the root and type into the terminal: 
```sh
docker-compose up --build
```

After the build you would see in docker a new container called 'flask_app' with 2 images, one for the application and the database. In here you can see the status of the application running in the container. If everything is running, you can find the application with the below address in the browser:
```sh
http://localhost:5000/
```

If it is not running in the docker container and stop with a exit 1 or 2, you need to delete the container and run the code again. Another option would be running it with WSL or WSL2. This can be installed with -> https://www.windowscentral.com/how-install-wsl2-windows-10. After that, enable it in docker by going into the setting, general and check 'use the WSL 2 based engine'. 

# Individual stack
The platform for this repository is created in a Linux environment with pip and python3.9 version installed. Below are the commands for installing the dependencies and virtual environment with the database. There will be a test user with the username and password 'test' for testing purposes if your are making a migration. The model for prediction is not delivered with this repository and it is advised to use a YOLOv5 model with it.

For running this back-end application you need Python3.9, virtualenv and Pip. For installing that here:
```sh
pip
https://pip.pypa.io/en/stable/installation/
python3.9
https://www.youtube.com/watch?v=uDbDIhR76H4
https://www.python.org/downloads/
```

After installing pip, you need a CLI, for example terminator, CMD or an IDE for installing virtualenv. In the CLI, type in the next command and press 'y' for installing virtualenv:
```sh
pip install virtualenv
```

After installing virtualenv, you can create one by going into the root folder of this project and type for a virtual environment: 
```sh
virtualenv env
```

This create a folder called env where the modules for this program will be downloaded to and used for this program. You can activate the env with: 
```sh
source ./env/bin/activate
```

You should be inside the environment, you can verify it if the sentence starts with (env) in the CLI. After that you can start installing the dependencies for this project by the next command:
```sh
python3.9 -m pip install -r requirements.txt
```

The requirements.txt contains the dependencies modules for this project. It will take some time for downloading and installing the packages. After some time, the Flask package is also installed and you can now set the flask app to the manage.py, the starting point for this application. Export flask application environment variable:
```sh
export FLASK_APP=manage.py
```

After that you can need to make migration and initializing the database. That will create a test user called 'test' with the password 'test' where you can use the application:
```sh 

flask db init

flask db migrate

flask db upgrade
```

After that you can run the application with: 
```sh
flask run
```

Install the stand alone packages in env (example flask but needs to change to actual packages): 
```sh
python3.9 -m pip install flask
```

Save the working dependencies in in the requirements.txt: 
```sh   
python3.9 -m pip freeze > requirements.txt
```