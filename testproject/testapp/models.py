# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

from djangoratings.fields import AnonymousRatingField, RatingField


@python_2_unicode_compatible
class RatingTestModel(models.Model):
    rating = AnonymousRatingField(range=2, can_change_vote=True)
    rating2 = RatingField(range=2, can_change_vote=False)

    def __str__(self):
        return '{}'.format(self.pk)
