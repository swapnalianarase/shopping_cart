from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    # Home
    path('', views.ProductView.as_view(), name="home"),
    
    # Product details
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    
    # Add to cart
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    
    # Cart
    path('cart/', views.show_cart, name='show_cart'),
    
    # Plus Cart
    path('pluscart/', views.plus_cart),
    
    # Minus cart
    path('minuscart/', views.minus_cart),
    
    # Remove cart
    path('removecart/', views.remove_cart),
    
    # Buy now
    path('buy/', views.buy_now, name='buy-now'),
    
    # Profile
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    # Address
    path('address/', views.address, name='address'),
    
    # Orders
    path('orders/', views.orders, name='orders'),
    
    # Mobile
    path('mobile/', views.mobile, name='mobile'),
    
    # Mobile data
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
    # Payment done
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
    # Accounts
    path('accounts/login', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    
    # Logout
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Registration
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
    # Password Change
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    
    # Password Change Done
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    
    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    # Password reset done
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    # Password reset confirm
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    # Password reset complete
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    # Checkout
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)