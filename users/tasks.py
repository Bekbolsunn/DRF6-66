from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_otp_mail(email, code):
    send_mail(
        "Регистрация на нашем сайте",
        f"Привет ваш код: {code} для регистрации",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return "OK"

@shared_task
def delete_unactive_users():
    from users.models import CustomUser
    deleted = CustomUser.objects.filter(is_active=False).delete()
    return f"Deleted: {deleted}"
