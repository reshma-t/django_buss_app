# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from bus_app_api.models import Bus, Route, Trip, BusStop

# Register your models here.

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(BusStop)