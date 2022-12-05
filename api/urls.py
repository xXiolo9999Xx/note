from django.urls import path
from . import views
urlpatterns = [
    path('note',views.getNotes),
    path('note/<int:pk>',views.getNote),
    
    path('note/<int:pk>/update',views.updatedNote),
    path('note/<int:pk>/delate',views.delatedNote),
    path('note/create',views.createNote),
]
