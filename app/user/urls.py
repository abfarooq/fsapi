from django.urls import path, include
from user import views

app_name = 'user'

urlpatterns = [
    #path('admin/', admin.site.urls),

    #path('api/user/', include('user.urls')),

    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),


]
