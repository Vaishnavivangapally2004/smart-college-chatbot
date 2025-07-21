from django.contrib import admin
from django.urls import path
from chatbot import views as chatbot_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chatbot_views.chatbot, name='home'),
    path('get_response/', chatbot_views.get_response, name='get_response'),
    path('login/', chatbot_views.login_view, name='login'),
    path('register/', chatbot_views.register_view, name='register'),
    path('logout/', chatbot_views.logout_view, name='logout'),
    path('chatbot/', include('chatbot.urls')),
]
