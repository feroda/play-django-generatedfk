from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Greatest
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor

from .fields import NoopForeignKey


class Event(models.Model):

    name = models.CharField(max_length=128)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                            related_name="created_events_set", null=True)
    confirmed_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                            related_name="confirmed_events_set", null=True)
    canceled_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                            related_name="canceled_events_set", null=True)
    last_updated_by_id = models.GeneratedField(
                        expression=Greatest("created_by", "confirmed_by", "canceled_by"),
                        output_field=models.BigIntegerField(),
                        db_persist=True)
    
    # Non lo trova come parametro quando metti il nome del campo nella values
    # django.core.exceptions.FieldError: Cannot resolve keyword 'last_updated_by' into field. Choices are: canceled_by, canceled_by_id, confirmed_by, confirmed_by_id, created_by, created_by_id, id, last_updated_by_id, name
    # last_updated_by = ForwardManyToOneDescriptor(
    #                     models.ForeignKey(User, on_delete=models.SET_NULL,
    #                         db_column="last_updated_by_id", db_constraint=False,
    #                         related_name="last_updated_events_set", null=True))

    last_updated_by = ForwardManyToOneDescriptor(
                        models.ForeignKey(User, on_delete=models.SET_NULL,
                            db_column="last_updated_by_id", db_constraint=False,
                            related_name="last_updated_events_set", null=True))

    @classmethod
    def _check_field_name_clashes(cls):
        return []

    @classmethod
    def _check_column_name_clashes(cls):
        return []
        
