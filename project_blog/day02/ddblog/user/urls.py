from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/users/sms
    # 注意写到最上面,用户名要避免使用sms
    path('sms',views.sms_view),
    # http://127.0.0.1:8000/v1/users/Amiao
    path('<str:username>',views.UserView.as_view()),
    # http://127.0.0.1:8000/v1/users/Amiao/avatar
    path('<str:username>/avatar',views.user_avatar),
]