# Flask_app

This is a proof of contest application for litter detection that is coupled to the 'Stadjutters' program. This repo contains the material prediction of litter pictures in jpg or png format.

The platform of this repo is created in a Linux environment with pip and python3.9 version installed. Below are the commands for installing the dependencies and virtual environment with the database. There will be a test user with the username and password 'test' for testing purposes if your are making a migration. The model for prediction is not delivered with this repository and it is advised to use a YOLOv5 model with it.

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

Export flask application environment variable:
```sh
export FLASK_APP=manage.py

flask db init

flask db migrate

flask db upgrade
```

Start the flask application: 
```sh
flask run
```

Install the libraries in env (example flask but needs to change to actual libs): 
```sh
python3.9 -m pip install flask
```

At any time save all dependencies we use: 
```sh   
python3.9 -m pip freeze > requirements.txt
```