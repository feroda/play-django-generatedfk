# play-django-generatedfk

Try to add a ForeignKey as a GeneratedField

## Try it

./manage.py migrate admin auth contenttypes sessions
./manage.py migrate --skip-checks web 0001

Follow DOC.md

## Try the working solution

./manage.py migrate noopfk 

Follow DOC.md with noopfk app instead of web
