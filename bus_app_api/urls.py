from django.conf.urls import url
from views import bus_view, route_view, trip_view
urlpatterns = [
    url(r'^bus/$', bus_view.BusList.as_view()),
    url(r'^bus/(?P<pk>d+)/$', bus_view.BusDetail.as_view()),
    url(r'^route/$', route_view.RouteList.as_view()),
    url(r'^route/(?P<pk>d+)/$', route_view.RouteDetails.as_view()),
    url(r'^trip/$', trip_view.TripList.as_view()),
    url(r'^trip/(?P<pk>d+)/$', trip_view.TripDetails.as_view()),
]
