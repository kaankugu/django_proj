from django.contrib import admin
from django.urls import path , include 
from mvt import views 
from django_proj import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from mvt.views import CustomRegistrationView
from film import views as vievs_film

urlpatterns = [
    path('', views.home, name='home'),
    path('hakkımda/', views.about, name='about'),
    path('projelerim/', views.project, name='project'),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path("404/",views.No_page,name="404"),
    path('comments/',views.comment_page, name='comment_page'),
    path('comments/save/', views.save_comment, name='save_comment'),
    path('comments/delete/<int:comment_id>/',views.delete_comment, name='delete_comment'),
    path('popular_movies/', vievs_film.get_popular_movies),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
