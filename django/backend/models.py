from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    """Default user"""

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    has_partner = models.BooleanField(
        _("Is the user partened"), default=False, blank=False
    )
    inQueue = models.BooleanField(
        _("Is the user looking for match"), default=False, blank=False
    )
    goals = models.ForeignKey("Goals", on_delete=models.CASCADE, related_name="users", null=True, blank=True)


class Goals(models.Model):
    """Table with major goals:
    e.g. Health, Job, exercise"""

    GOAL_CHOICES = [
        ("EXERCISE", "Exercise"),
        ("HEALTH", "Health"),
        ("STUDY", "Study"),
        ("HOBBIE", "Hobbie"),
        ("CAREER", "Career"),
    ]

    goal = models.CharField(max_length=50, choices=GOAL_CHOICES, blank=True)


class Partnership(models.Model):
    """ Define a partnership between two users """

    user1 = models.ForeignKey(
        "User", on_delete=models.DO_NOTHING, related_name="partner1"
    )
    user2 = models.ForeignKey(
        "User", on_delete=models.DO_NOTHING, related_name="partner2"
    )
    active = models.BooleanField(
        _("Is the partnership activated?"), blank=False, default=False
    )
    time_stamp = models.DateTimeField(auto_now_add=True)


class WeeklyGoals(models.Model):
    """" Define the weekly goals on a partnership"""

    author = models.ForeignKey(
        "User", on_delete=models.DO_NOTHING, related_name="weekly_goals"
    )
    critic = models.ForeignKey(
        "User", on_delete=models.DO_NOTHING, related_name="weekly_goals_critic"
    )
    goal = models.CharField(_("Weekly goal"), max_length=255, blank=False)
    partnership = models.ForeignKey("Partnership", on_delete=models.DO_NOTHING, related_name='goals')
    time_stamp = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    """ Feedback provide by the critic on each weekly goal"""

    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    rating = models.IntegerField(
        _("Rating on the completion on the Weekly Task"),
        choices=RATING_CHOICES,
        blank=False,
    )


class Communication(models.Model):
    """ Message storage table"""
    user1 = models.ForeignKey(
        "User", on_delete=models.DO_NOTHING, related_name="messages_sent"
    )
    user2 = models.ForeignKey(
        "User", on_delete=models.DO_NOTHING, related_name="messages_received"
    )
    message = models.CharField(max_length=500, blank=False)
    time_stamp = models.DateTimeField(auto_now_add=True)

