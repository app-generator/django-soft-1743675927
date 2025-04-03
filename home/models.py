# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Inventory(models.Model):

    #__Inventory_FIELDS__
    model name = models.TextField(max_length=255, null=True, blank=True)
    model purpose and operational context = models.TextField(max_length=255, null=True, blank=True)
    model owner = models.TextField(max_length=255, null=True, blank=True)
    system prompt = models.TextField(max_length=255, null=True, blank=True)
    foundation llm = models.TextField(max_length=255, null=True, blank=True)
    token limit = models.TextField(max_length=255, null=True, blank=True)
    temperature = models.TextField(max_length=255, null=True, blank=True)
    training datasets = models.TextField(max_length=255, null=True, blank=True)
    known limitations = models.TextField(max_length=255, null=True, blank=True)

    #__Inventory_FIELDS__END

    class Meta:
        verbose_name        = _("Inventory")
        verbose_name_plural = _("Inventory")


class Risk Assessment(models.Model):

    #__Risk Assessment_FIELDS__
    what type of ai capabilities are being used for this use-case? = models.TextField(max_length=255, null=True, blank=True)
    primary pattern of the use case = models.TextField(max_length=255, null=True, blank=True)
    are there further data risks associated to this use-case? = models.TextField(max_length=255, null=True, blank=True)
    risk category of genai use case = models.TextField(max_length=255, null=True, blank=True)
    what machine learning pattern(s) are being used for this use-case = models.TextField(max_length=255, null=True, blank=True)
    regulatory impact (beyond ai/ ml standards) = models.TextField(max_length=255, null=True, blank=True)
    financial impact on group = models.TextField(max_length=255, null=True, blank=True)
    reputational impact of use case = models.TextField(max_length=255, null=True, blank=True)
    impact on customers (natural persons) = models.TextField(max_length=255, null=True, blank=True)
    impact on customers (legal entity) = models.TextField(max_length=255, null=True, blank=True)
    impact on staff/ prospective staff = models.TextField(max_length=255, null=True, blank=True)
    impact on market functioning = models.TextField(max_length=255, null=True, blank=True)
    use of personal data = models.TextField(max_length=255, null=True, blank=True)
    use of protected variables = models.TextField(max_length=255, null=True, blank=True)
    importance of ai/ ml recommendation on final decision = models.TextField(max_length=255, null=True, blank=True)

    #__Risk Assessment_FIELDS__END

    class Meta:
        verbose_name        = _("Risk Assessment")
        verbose_name_plural = _("Risk Assessment")



#__MODELS__END
