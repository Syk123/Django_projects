from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$',views.form_name_view,name="help"),
]
