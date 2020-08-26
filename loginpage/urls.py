from django.conf.urls import url,include
from loginpage import views
app_name = 'loginpage'
urlpatterns = [
    url(r'^register/',views.register,name='registeration'),
    url(r'^login/',views.user_login,name='user_login'),
]
