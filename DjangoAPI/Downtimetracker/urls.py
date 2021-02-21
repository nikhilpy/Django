from django.conf.urls import url
from Downtimetracker import views

urlpatterns=[
	url(r'^customer/$',views.CustomerAPI),
	url(r'^customer/([0-9]+)$',views.CustomerAPI)
]