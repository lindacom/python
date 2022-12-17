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
8. run the application - python -m uvicorn main:app --reload


Documentation
===================
https://docker.com/blog/how-to-dockerize-your-python-applications 
