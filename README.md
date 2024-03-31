# Play Django ForeignKey on Generated Field

Try to add a ForeignKey that uses a GeneratedField.

This repo addresses the problem of using a ForeignKey accessor/descriptor on a GeneratedField. 

This is a weird problem because you cannot use the related lookup feature `__` on a GeneratedField that represents a ForeignKey.

### Opportunities

I think that the proposed solution:

- can be applied also to annotation on `F(fk_field_name)` and overcome the limitation presented at https://docs.djangoproject.com/en/5.0/ref/models/expressions/#using-f-with-annotations. Specifically: *When referencing relational fields such as ForeignKey, F() returns the primary key value rather than a model instance:*
- can be embedded in the value of an `output_field=` like `NoopForeignKey` avoiding to specify a duplicate field in a Model

### Drawbacks

Really not many. If you want to take advantage of this feature, you must specify 2 fields in your Model:

- the first one is the GeneratedField with output_field=BigIntegerField() or the value of your ForeignKey
- the second one is the NoopForeignKey the will be the accessor for the first one.

## Try the working solution in the "noopfk" application

./manage.py migrate  # No matter about errors

./manage.py createsuperuser

./manage.py shell

```
>>> from noopfk.models import Event
>>> from django.contrib.auth.models import User
>>> Event.objects.create(name="releasing Django 6.0", created_by=User.objects.first())
>>> Event.objects.values("created_by__pk", "created_by__username")
<QuerySet [{'created_by__pk': 1, 'created_by__username': 'admin'}]>
>>> Event.objects.values("last_updated_by__pk", "last_updated_by__username")
<QuerySet [{'last_updated_by__pk': 1, 'last_updated_by__username': 'admin'}]>
>>> Event.objects.filter(last_updated_by__username__startswith="cielcio").values()
<QuerySet []>
>>> Event.objects.filter(last_updated_by__username__startswith="a").values()
<QuerySet [<Event: Event object (1)>]>
```

## Try other stuff in the "web" application

./manage.py migrate admin auth contenttypes sessions

./manage.py migrate --skip-checks web 0001

Follow DOC.md

## History

Check [my - short - commit history](https://github.com/feroda/play-django-generatedfk/commits/main/) if you are interested in my other attempts with related fields and descriptors.
