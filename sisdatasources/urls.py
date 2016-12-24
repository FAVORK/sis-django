from django.conf.urls import url
from django.contrib import admin

from .views import (
    index,
    home,
    notification,
    schooldetails,
    studentprofile,
    studentloggedin,
    blog,
    login,
    auth_view,
    administration,
    students,
    studentdetails,
    staff,
    staffdetails,
    payroll,
    payrolldetails,
    schedule,
    scheduledetails,
    profile
 )

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^home/$', home),
    url(r'^notification/$', notification),
    url(r'^schooldetails/$', schooldetails),
    url(r'^studentprofile/$', studentprofile),
    url(r'^studentloggedin/$', studentloggedin),
    url(r'^blog/$', blog),
    url(r'^login/$', login),
    url(r'^accounts/auth/$', auth_view),
    url(r'^administration/$', administration),
    url(r'^students/$', students),
    url(r'^studentdetails/(?P<id>\d+)/$', studentdetails, name='detail'),
    url(r'^staff/$', staff),
    url(r'^staffdetails/(?P<id>\d+)/$', staffdetails),
    url(r'^payroll/$', payroll),
    url(r'^payrolldetails/(?P<id>\d+)/$', payrolldetails),
    url(r'^schedule/$', schedule),
    url(r'^scheduledetails/(?P<id>\d+)/$', scheduledetails),
    url(r'^accounts/profile/$', profile),
]
