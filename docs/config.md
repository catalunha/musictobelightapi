
# Install django
mkdir musictobelightapi
cd musictobelightapi/

pyenv versions
pyenv install 3.11.0
pyenv local 3.11.0

poetry init

Would you like... no
Would you like... no

poetry shell

poetry add django

# Django + Apps
django-admin startproject project .
cd project
django-admin startapp bases
django-admin startapp accounts
django-admin startapp commons
django-admin startapp musics
django-admin startapp medias

# Apps
poetry add djangorestframework
poetry add djangorestframework-simplejwt
poetry add pillow
poetry add python-decouple
poetry add dj-database-url
poetry add django-cors-headers
poetry add django-storages[s3]
poetry add psycopg2-binary
poetry add gunicorn

# run

python manager.py makemigrations
python manager.py migrate
python manager.py createsuperuser
python manager.py runserver
python manage.py runserver 192.168.10.113:8000


# tutoriais
https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html