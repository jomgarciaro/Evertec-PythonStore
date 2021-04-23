## PythonStore

---

This project uses PlaceToPay's Web-Checkout service to test its functionality using a single-product online store.

### Installation


Install python for your OS directly from official web page
https://www.python.org/

After successfully installing Python you will be able to install all the requirements of the project by means of the following command
```
pip install -r requeriments.txt

```

### Use

With django installed and configured, in your project path can run the *manage.py* file with the specific commands to config database:
```
python manage.py migrate
```

To see the application, run the command 
```
python manage.py runserver
```
and in your browser go to:

http://localhost:8000/new_order
