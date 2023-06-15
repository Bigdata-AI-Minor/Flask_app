# Flask_app

This is a proof of contest application for litter detection that is coupled on the 'Stadjutters' program. This repo contain the material prediction of litter pictures in jpg or png format.

The platform of this repo is created in a Linux environment with pip and python3.9 version installed. Below are the commands for installing the dependencies and virtual environment with database. There will be test user with the username and password 'test' for testing purposes if your are making a migration. The model for prediction is not delivered with this repository and it is advised to use a YOLOv5 model with it.

Create from this path a virtual environment: 
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