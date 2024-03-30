Insert test data after superuser has been created

```
>>> from web.models import Action
>>> from django.contrib.auth.models import User
>>> Action.objects.create(name="renderizzata la tavoletta del cesso", created_by=User.objects.first())
```

If the desired field (without applied migration) exists:

```
last_updated_by_id = models.GeneratedField(
                    expression=Greatest("created_by", "confirmed_by", "canceled_by"),
                    output_field=models.BigIntegerField(),
                    db_persist=True)

# Desired field
last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                        db_column="last_updated_by_id",
                        related_name="last_updated_actions_set", null=True)
```

then the error is:

```
django.db.utils.ProgrammingError: cannot insert a non-DEFAULT value into column "last_updated_by_id"
DETAIL:  Column "last_updated_by_id" is a generated column.
```

If the ForeignKey field is commented then the Action model instance can be created:

```
<Action: Action object (1)>
```

but the lookup does not work:

```
>>> from web.models import Action
>>> Action.objects.values("created_by__pk", "created_by__username")
<QuerySet [{'created_by__pk': 1, 'created_by__username': 'admin'}]>

>>> Action.objects.values("last_updated_by__pk", "last_updated_by__username")
django.core.exceptions.FieldError: Cannot resolve keyword 'last_updated_by' into field. Choices are: canceled_by, canceled_by_id, confirmed_by, confirmed_by_id, created_by, created_by_id, id, last_updated_by_id, name

>>> Action.objects.values("last_updated_by_id__pk", "last_updated_by_id__username")
django.core.exceptions.FieldError: Cannot resolve keyword 'pk' into field. Join on 'last_updated_by_id' not permitted.
```

Decommenting the ForeignKey leads to working solution:

```
>>> from web.models import Action
>>> Action.objects.values("last_updated_by__pk", "last_updated_by__username")
<QuerySet [{'last_updated_by__pk': 1, 'last_updated_by__username': 'admin'}]>
```

## IT WORKS without db_constraint and db_index

```
>>> from noopfk.models import Event
>>> Event.objects.values("last_updated_by__pk", "last_updated_by__username")
<QuerySet [{'last_updated_by__pk': 1, 'last_updated_by__username': 'admin'}]>
>>> Event.objects.values("created_by__pk", "created_by__username")
<QuerySet [{'created_by__pk': 1, 'created_by__username': 'admin'}]>
>>> Event.objects.filter(last_updated_by__username__startswith="cielcio")
<QuerySet []>
>>> Event.objects.filter(last_updated_by__username__startswith="a")
<QuerySet [<Event: Event object (1)>]>
>>> 
```

## If you want...

IF YOU WANT TO Add Foreign Key constraint into the database, write the code below in `python manage.py dbshell`, 
but it is not needed, and simetimes discouraged. We discourage it on a generated field:

```
BEGIN;
ALTER TABLE "web_action" 
    ADD CONSTRAINT "web_action_last_updated_by_id_46e50e5b_fk_auth_user_id" 
    FOREIGN KEY ("last_updated_by_id") REFERENCES "auth_user"("id") 
    DEFERRABLE INITIALLY DEFERRED; 
    SET CONSTRAINTS "web_action_last_updated_by_id_46e50e5b_fk_auth_user_id" IMMEDIATE;
COMMIT;
```

