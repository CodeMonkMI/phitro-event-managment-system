from django.dispatch import receiver
from users.models import User
from django.db.models.signals import post_save
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if not created:
        return

    token = default_token_generator.make_token(instance)
    activation_url = f"{settings.FRONTEND_URL}/activate/{instance.id}/{token}"
    subject = "Activate you account"
    message = f"Hi, {instance.username},\nPlease activate your account via this link: {activation_url}\n\n Thank you"
    recipient_list = [instance.email]
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
        )
        print("Mail sended successfully")
    except Exception as e:
        print(f"Failed to send email to {instance.email}: {str(e)}")
