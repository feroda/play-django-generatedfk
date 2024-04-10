from django.test import TestCase
from django.contrib.auth.models import User

from noopfk.models import Event

class EventTestCase(TestCase):

    def setUp(self):
        self.u = "cielcio"
        User.objects.create(username=self.u)
        Event.objects.create(name="releasing Django 6.0", created_by=User.objects.first())

    def test_events_last_updated_by_fk_generated(self):
        """Events have the same values for created_by and last_updated_by GeneratedForeignKey"""
        self.assertEqual(
            Event.objects.first().created_by,
            Event.objects.first().last_updated_by)

    def test_events_last_updated_by_fk_lookup(self):
        """GeneratedForeignKey can use the Queryset lookup API"""
        self.assertEqual(
            list(Event.objects.filter(created_by__username__startswith=self.u).values()),
            list(Event.objects.filter(last_updated_by__username__startswith=self.u).values()))

    def test_events_bulk_create(self):
        """GeneratedForeignKey must support bulk create"""
        Event.objects.bulk_create([
                Event(name="First event"),
                Event(name="Second event", created_by=User.objects.first()),
            ])
