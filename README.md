# Flask_app

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

export flask application as env variable:
```sh
export FLASK_APP=manage.py

flask db init

flask db migrate

flask db upgrade
```