#Groups urls.py

from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('',views.ListGroupViews.as_view(),name='all'),
    path('new/',views.CreateGroupView.as_view(),name='create'),
    path('post/in/<slug:slug>/',views.SingleGroupView.as_view(),name='single'),
    path('join/<slug:slug>/',views.JoinGroupView.as_view(),name='join'),
    path('leave/<slug:slug>/',views.LeaveGroupView.as_view(),name='leave')
]
