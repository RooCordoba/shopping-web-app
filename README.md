# shopping-web-app
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
python -m venv "name_of_the_ve"
```

Activate the virtual enviroment (For windows):
```sh
source "name_of_the_ve"/Scripts/activate
```

Install the requeriments for this proyect:
```sh
pip install requeriments.txt
```

Then, initialize the server:
```sh
uvicorn main:app --reload
```