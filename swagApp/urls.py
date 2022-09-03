from django.urls import path

from swagApp import views

urlpatterns = [
    path('fasd/',views.swagdef),
    path('daf/',views.swagall),
    path('kasr/',views.drrr),

    path('aa', views.register, name='register'),
    path('emp/', views.emp, name='emp'),
    path('abc/', views.insert, name='new'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('pagination/',views.display),
]
