from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Models for demonstration (should be in models.py in real app)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test123')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='test123')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='test123')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='test123')

        # Create activities
        Activity.objects.create(user='ironman', team='Marvel', type='Running', duration=30)
        Activity.objects.create(user='batman', team='DC', type='Cycling', duration=45)
        Activity.objects.create(user='wonderwoman', team='DC', type='Swimming', duration=60)
        Activity.objects.create(user='spiderman', team='Marvel', type='Yoga', duration=20)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=50)
        Leaderboard.objects.create(team='DC', points=70)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Pullups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
