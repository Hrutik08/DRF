from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/',  views.StudentList.as_view()),
    # path('studentapi/',  views.StudentCreate.as_view()),
    path('studentapi/',  views.StudentListCreate.as_view()),
    # path('studentapi/<int:pk>',  views.StudentRetrive.as_view())
    # path('studentapi/<int:pk>',  views.StudentUpdate.as_view())
    # path('studentapi/<int:pk>',  views.StudentDestroy.as_view()),

    # path('studentapi/<int:pk>',  views.StudentListRetrieveUpdate.as_view()),
    # path('studentapi/<int:pk>',  views.StudentListRetrieveDestroy.as_view()),
    path('studentapi/<int:pk>',  views.StudentListRetrieveUpdateDestroy.as_view()),
    
    
]