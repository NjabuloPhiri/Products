# Produce Products

Produce Products is a Django project that allows users to view, add, edit and delete 
product entries. 

## Installation

Ensure that you have Python 3 installed on your machine. (To do this, follow the link:
https://docs.python-guide.org/starting/install3/osx/.) In your terminal,
launch the virtual environment and open the shell. Install Django in the 
virtual environment, and then run the project.

```bash
1. git clone https://phi_res@bitbucket.org/byteorbit/njabulo.git
2. python3 -m venv produce_products
Create local postgres database using the name 'produce_productsdb'
3. pipenv install django
4. python manage.py createsuperuser 
5. python manage.py makemigrations produce_products
6. python manage.py migrate produce_products
7. python manage.py runserver and then go to http://localhost:8000/
```

## Usage

```python
To install requirements, run: 
pip install -r requirements.txt

```

## License
[MIT](https://choosealicense.com/licenses/mit/)