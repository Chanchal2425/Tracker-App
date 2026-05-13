from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("create/", views.create_new, name="create_new"),
    path("list/",views.animelist , name="animelist"),
    path("edit/",views.edit ,name="edit"),
    path("delete/<title_id>",views.delete ,name="delete"),
    path("complete/<complete_id>",views.complete_task ,name="complete_task"),
    path("pending/<pending_id>",views.pending_task ,name="pending_task"),
]








































# from . import views

# urlpatterns = [
#     path('',views.index,name='index'),
# ]