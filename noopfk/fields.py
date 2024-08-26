from django.db import models


class NoopForeignKey(models.ForeignKey):

    def __init__(self, model, on_delete=None, *args, **kw):
        super().__init__(model, on_delete=models.deletion.DO_NOTHING, *args, **kw)

    def db_type(self, connection):
        # No db_type since GeneratedField has already been created
        return None

    def contribute_to_class(self, cls, name, private_only=True):
        # Use private_only=True to not ADD COLUMN in migrations
        return super().contribute_to_class(cls, name, private_only)
