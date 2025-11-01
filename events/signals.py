from django.dispatch import receiver
from events.models import Events
from django.db.models.signals import m2m_changed
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from users.models import User


@receiver(m2m_changed, sender=Events.participants.through)
def participant_update(sender, instance, action, pk_set, **kwargs):
    if action not in ("post_add", "post_remove"):
        return

    if action == "post_add":
        users = instance.participants.filter(pk__in=pk_set)
        message = f"Hi,\nThanks you participating on the event."

    if action == "post_remove":
        users = User.objects.filter(pk__in=pk_set)
        message = (
            "Hi,\nThanks you for taking interested. Hopefully you participate later"
        )

    recipient_list = [user.email for user in users]  # type: ignore

    subject = "Event response"
    try:
        # send_mail(
        #     subject=subject,
        #     message=message,  # type: ignore
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=recipient_list,
        # )
        print('participant mail sended successfully!')
    except Exception as e:
        print(f"Failed to send email to {instance.email}: {str(e)}")
