from django.db.models import ForeignKey


class NoopForeignKey(ForeignKey):

    def db_type(self, connection):
        # No db_type since GeneratedField has already been created
        return None

    def contribute_to_class(self, cls, name, private_only=True):
        # Use private_only=True to not ADD COLUMN in migrations
        return super().contribute_to_class(cls, name, private_only)
