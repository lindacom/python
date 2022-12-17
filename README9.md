How to Dokerize a python app
============================

Dockerfile - blue print for building images. Specify base image
Docker image - template for running containers
Docker container - running process containing application

1. Install Docker desktop from www.docker.com. NB. the command line tool will also be installed.
2. Open your project in visual studio code
3. In visual studio code install the docker extension
4. In your project create a docker file called Dockerfile with no extension and enter the following text:

```
FROM python:3.9

WORKDIR /code

COPY .requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0" "--port", "80"]
```

6. Install the python environment manager extension
7. Activate the virtual environment for your project - Click the python icon in the left side of the screen and expand the venv heading. 
Select the virtual environment from the list and click the open in terminal button. You will see venv in the command prompt. 
7. Install the fast api and uvicorn libraries - pip install fastapi uvicorn
8. Create a main.py file in the root of your project with the following information

```
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return { "message": "FastAPI!" }
```

N.b. The command uvicorn main:app refers to:

main: the file main.py (the Python "module").
app: the object created inside of main.py with the line app = FastAPI().
--reload: make the server restart after code changes. Only use for development.

9. Navigate to the root of the project e.g. cd django_project. Run the application - python -m uvicorn main:app --reload. You will see the json message in 
the browser


Documentation
===================
https://docker.com/blog/how-to-dockerize-your-python-applications 

Uvicorn - An ASGI web server, for Python. - https://www.uvicorn.org/
