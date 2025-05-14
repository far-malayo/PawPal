from django.urls import path
# Add a print statement to confirm this file is being loaded
print("Loading users/urls.py")

try:
    from .views import RegisterView, LoginView, LogoutView, UserProfileView
    urlpatterns = [
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('profile/', UserProfileView.as_view(), name='profile'),
    ]
    print("Successfully loaded user URL patterns")
except Exception as e:
    print(f"Error loading users/urls.py: {e}")
    # fallback pattern so Django doesn't crash
    urlpatterns = []