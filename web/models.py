from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Greatest


class Action(models.Model):

    name = models.CharField(max_length=128)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    confirmed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    canceled_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_updated_by = models.GeneratedField(
                        expression=Greatest("created_by", "confirmed_by", "canceled_by"),
                        output_field=models.ForeignKey(User, on_delete=models.SET_NULL, null=True),
                        db_persist=True)

