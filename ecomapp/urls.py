from django.urls import path
from django.contrib.auth import views
from .views import homeview, latestproductview, popularproductview, productdetailview, CustomerRegistrationView, seeprofile, EditProfileview, addtocart, show_cart, plus_cart, minus_cart, remove_cart, checkout, payment_done, orders, cancelorder, categoryview, cateproductsview, aboutusview, contactview, SearchView, EditProfileview2
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [
    path('', homeview, name='home'),
    path('aboutus/', aboutusview, name='aboutus'),
    path('contact/', contactview, name='contact'),
    path('latest/', latestproductview, name='latest'),
    path('popular/', popularproductview, name='popular'),
    path('category/', categoryview, name='category'),
    path('catproducts/<int:id>', cateproductsview, name='catproducts'),
    path('product/<int:id>', productdetailview, name='productdetail'),
    path('register/', CustomerRegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(template_name='ecomapp/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('passwordchange/', views.PasswordChangeView.as_view(template_name='ecomapp/passwordchange.html', form_class=MyPasswordChangeForm), name='passwordchange'),
    path("password_change/done/", views.PasswordChangeDoneView.as_view(template_name='ecomapp/passwordchangedone.html'), name="password_change_done"),
    path("password_reset/", views.PasswordResetView.as_view(template_name='ecomapp/passwordreset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path("password_reset/done/", views.PasswordResetDoneView.as_view(template_name='ecomapp/passwordresetdone.html'),name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(template_name='ecomapp/passwordresetconfirm.html', form_class=MySetPasswordForm),name="password_reset_confirm"),
    path("reset/done/", views.PasswordResetCompleteView.as_view(template_name='ecomapp/passwordresetcomplete.html'),
        name="password_reset_complete"),
    path('editprofile/', EditProfileview.as_view(), name="editprofile"),
    path('editprofile2/', EditProfileview2.as_view(), name="editprofile2"),
    path('seeprofile/', seeprofile, name="seeprofile"),
    path('add-to-cart/', addtocart, name="add-to-cart"),
    path('cart/', show_cart, name="showcart"),
    path('pluscart/', plus_cart, name='pluscart'),
    path('minuscart/', minus_cart, name='minuscart'),
    path('removecart/<int:id>/', remove_cart, name='removecart'),
    path('checkout/', checkout, name='checkout'),
    path('paymentdone/', payment_done, name='paymentdone'),
    path('orders/', orders, name='orders'),
    path('cancelorder/<int:id>', cancelorder, name='cancelorder'),
     path('search/', SearchView, name='search'),
]
