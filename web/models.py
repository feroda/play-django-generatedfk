from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Greatest


class Action(models.Model):

    name = models.CharField(max_length=128)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                            related_name="created_actions_set", null=True)
    confirmed_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                            related_name="confirmed_actions_set", null=True)
    canceled_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                            related_name="canceled_actions_set", null=True)
    last_updated_by_id = models.GeneratedField(
                        expression=Greatest("created_by", "confirmed_by", "canceled_by"),
                        output_field=models.BigIntegerField(),
                        db_persist=True)
    
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                            db_column="last_updated_by_id",
                            related_name="last_updated_actions_set", null=True)

