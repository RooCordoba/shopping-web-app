# shopping-web-app-backend
A simple web page to buy clothes and accessories with users's database.

## Pre-requisites

In order to run this project, you must have installed on your OS:
  * Python 3
  * Pip

To install pip in Linux:

```sh
python get-pip.py
```

To install pip in Windows:

```sh
py get-pip.py
```

## Running The proyect

First, create the Virtual enviroment:
```sh
python -m venv env
```

Activate the virtual enviroment (For windows):
```sh
source env/Scripts/activate
```

Install the requeriments for this proyect:
For Windows:
```sh
pip install -r requirements.txt
```
For Linux:
```sh
pip install requirements.txt
```

Then, initialize the server:
```sh
uvicorn main:app --reload
```