# employees/create_test_admin.py
from django.contrib.auth import get_user_model

def run():
    User = get_user_model()
    username = "admin"
    password = "admin123"
    email = "test@example.com"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("✅ Test admin created!")
    else:
        print("ℹ️ Admin already exists.")
