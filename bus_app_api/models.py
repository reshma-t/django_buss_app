# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Bus(models.Model):
	bus_reg_no = models.CharField(max_length=12)
	bus_name = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s %s' % (self.bus_name, self.bus_reg_no);


class Route(models.Model):
	starts_from  = models.CharField(max_length=50)
	ends_at = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s %s' % (self.route_starting_point, self.route_ending_point)


class Trip(models.Model):
	route = models.ForeignKey('Route')
	bus = models.ForeignKey('Bus')
	trip_starting_time = models.TimeField()


class BusStop(models.Model):
	part_of_trip = models.ForeignKey(Trip)
	stop_name = models.CharField(max_length=50)
	bus_arrival_time = models.TimeField()

	def __unicode__(self):
		return u'%s %c' % (self.stop_name, self.bus_arrival_time)
