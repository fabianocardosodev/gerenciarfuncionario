from . import views

app_name = 'gerfuncion'

urlpatterns = [
    path('', views.index, name='index'),
]
