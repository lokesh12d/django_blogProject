from django.contrib import admin
from django.urls import path
from Blogapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,PasswordChangeForm,PasswordResetForm,PasswordResetConfirm

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('delete/<int:id>', views.delete),
    path('details/<int:id>', views.details),
    path('edit/<int:id>', views.edit,name='edit'),
    path('addblog', views.addblog),
    path('authors', views.Users),

                  #Admin Urls
    path('signup', views.User_signup.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='login.html'),name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('changepassword', auth_views.PasswordChangeView.as_view(form_class=PasswordChangeForm,
        template_name='changepassword.html',success_url='/passwordchangedone/'),name='changepassword'),
    path('passwordchangedone', auth_views.PasswordChangeDoneView.as_view(template_name='changepassworddone.html'),name='passwordchangedone'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=PasswordResetForm),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html",
                    form_class=PasswordResetConfirm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
