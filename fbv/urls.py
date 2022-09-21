from django.urls import path
from fbv.views import (
    home, 
    people_get_post,
    people_put_delete_patch
)
urlpatterns = [
    path("", home, name='home'),
    path('people/', people_get_post),
    path('people_update/<int:pk>/', people_put_delete_patch)
]
