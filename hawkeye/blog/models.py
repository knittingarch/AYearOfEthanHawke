# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Review(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def was_published_recently(self):
        if self.updated_at > self.created_at:
            return self.updated_at >= timezone.now() - datetime.timedelta(days=7)
        return self.created_at >= timezone.now() - datetime.timedelta(days=7)


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Platform(models.Model):
    NETFLIX = 'netflix'
    HULU = 'hulu'
    AMAZON = 'amazon'
    TV = 'tv'
    PHYSICAL = 'physical'
    OTHER = 'other'
    VIEWING_PLATFORMS = (
        (NETFLIX, 'Netflix'),
        (HULU, 'Hulu'),
        (AMAZON, 'Amazon Prime'),
        (TV, 'Television'),
        (PHYSICAL, 'DVD / Blu Ray'),
        (OTHER, 'Other'),
    )
    platform = models.CharField(max_length=30, choices=VIEWING_PLATFORMS)

    def __str__(self):
        return self.platform


class Role(models.Model):
    SUPPORTING = 'supporting'
    LEADING = 'leading'
    WRITING = 'writing'
    DIRECTING = 'directing'
    TYPES_OF_ROLES = (
        (SUPPORTING, 'Supporting Actor'),
        (LEADING, 'Lead Actor'),
        (WRITING, 'Writer'),
        (DIRECTING, 'Director'),
    )
    role = models.CharField(max_length=50, choices=TYPES_OF_ROLES, default='leading')

    def __str__(self):
        return self.role


class Movie(models.Model):
    title = models.CharField(max_length=200)
    directors = models.ManyToManyField(Director)
    year = models.IntegerField()
    rating = models.IntegerField()
    review = models.OneToOneField(Review) 
    platforms = models.ManyToManyField(Platform)
    role = models.OneToOneField(Role)
    character = models.CharField(max_length=100)
    runtime = models.IntegerField()
    watch_date = models.DateTimeField('dated watched')

    def __str__(self):
        return self.title
