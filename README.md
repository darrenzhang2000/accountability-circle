# Accountability Circle 
An App to find friends to help yourself reach your goals!

## Installation

Clone it 
```python
git clone https://github.com/darrenzhang2000/accountability-circle.git
```
Create an virtual enviroment
```python
# on Linux, python3, on Windows, Python
python3 -m venv venv
```
Initialize the virtual environ
```python
# on Linux
source ./venv/bin/activate
# On Windows
/venv/Scripts/activate.exe
```
cd into the folder
```python
cd accountability-circle
```
Install the required dependencies
```python
pip install -r requirements.txt
```
Cd into django
```python
cd django
```
Apply the migrations
```python
python manage.py migrate
```
Start the developer server
```python
python manage.py runserver
```
