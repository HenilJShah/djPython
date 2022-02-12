title:  dango signals
~>new things in django i learn : 1


NOTE: 

youtube link: https://youtu.be/w4pnWgEgv8E?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=966


referce link:

code part: 
------------------------------------------------------------------------------
apps.py
-------
from django.apps import AppConfig


class Signalsapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signalsapp1'

    def ready(self):
        import signalsapp1.signals

new create file signals.py
-------------------------
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_successfully(sender, request, user, **kwargs):
    print("----------------------------------")
    print("logged-in signal... Run dashboard")
    print("sender:", sender)
    print("request:", request)
    print("User:", User)
    print("password", User.password)
    print(f"kwargs:{kwargs}")

------------------------------------------------------------------------------
