from django.contrib import admin
from django.urls import path

from webapp.views import *
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', TaskView.as_view(), name='task_view'),
    path('add/', TaskCreate.as_view(), name='add'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('projects', ProjectView.as_view(), name='projects'),

    path("accounts/", include('accounts.urls'))
]
