from django.db.models import ForeignKey


class NoopForeignKey(ForeignKey):

    def check(self, **kwargs):
        return []
