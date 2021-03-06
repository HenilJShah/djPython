from venv import create
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_finished, request_started, got_request_exception
from django.db.backends.signals import connection_created


# when the user is login call this signal
@receiver(user_logged_in, sender=User)
def login_successfully(sender, request, user, **kwargs):
    print("----------------------------------")
    print("logged-in signal...")
    print("sender:", sender)
    print("request:", request)
    print("User:", user)
    print("password", User.password)
    print(f"kwargs:{kwargs}")

# when the user is logout call this signal


@receiver(user_logged_out, sender=User)
def logout_successfully(sender, request, user, **kwargs):
    print("----------------------------------")
    print("logged-out signal...")
    print("sender:", sender)
    print("request:", request)
    print("User:", user)
    print("password", User.password)
    print(f"kwargs:{kwargs}")


# when the user is failed call this signal
@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("----------------------------------")
    print("logged-failed signal...")
    print("sender:", sender)
    print("credentials:", credentials)
    print("request:", request)
    print(f"kwargs:{kwargs}")


# when the user save any operation call this signal
# it's work beginning
@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("----------------------------------")
    print("pre_save signal...")
    print("sender:", sender)
    print("instance:", instance)
    print(f"kwargs:{kwargs}")


# when the user update any operation call this signal
# it's work after
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("----------------------------------")
        print("post_save signal...")
        print("New record...")
        print("sender:", sender)
        print("instance:", instance)
        print("created:", created)
        print(f"kwargs:{kwargs}")
    else:
        print("----------------------------------")
        print("post_save signal...")
        print("Updated...")
        print("sender:", sender)
        print("instance:", instance)
        print("created:", created)
        print(f"kwargs:{kwargs}")


# when the user delete any operation call this signal
# it's work beginning
@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("----------------------------------")
    print("pre_delete signal...")
    print("sender:", sender)
    print("instance:", instance)
    print(f"kwargs:{kwargs}")


# when the user delete any operation call this signal
# it's work after the operation
@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("----------------------------------")
    print("post_delete signal...")
    print("sender:", sender)
    print("instance:", instance)
    print(f"kwargs:{kwargs}")


# when the user inti the model call this signal
# it's work beginning
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("----------------------------------")
    print("pre_init signal...")
    print("sender:", sender)
    print(f"kwargs:{args}")
    print(f"kwargs:{kwargs}")


# when the user inti the model call this signal
# it's work after the operation
@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("----------------------------------")
    print("post_init signal...")
    print("sender:", sender)
    print(f"kwargs:{args}")
    print(f"kwargs:{kwargs}")


# when the user hit app url
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("----------------------------------")
    print("At Beginning request...")
    print("sender:", sender)
    print("environ:", environ)
    print(f"kwargs:{kwargs}")


# when the user hit app url complete
@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("----------------------------------")
    print("At ending request...")
    print("sender:", sender)
    print(f"kwargs:{kwargs}")


# when the user got exception
# here this operation req_exception hit 'home/' url
@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print("----------------------------------")
    print("At Request exception...")
    print("sender:", sender)
    print("request:", request)
    print(f"kwargs:{kwargs}")


# when the user migrate model call this signal
# it's work beginning
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("----------------------------------")
    print("before_install_app...")
    print("sender:", sender)
    print("app_config:", app_config)
    print("verbosity:", verbosity)
    print("interactive:", interactive)
    print("using:", using)
    print("plan:", plan)
    print("apps:", apps)
    print(f"kwargs:{kwargs}")
    


# when the user migrate model call this signal
# it's work after the operation
@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("----------------------------------")
    print("at_end_migrate_flush...")
    print("sender:", sender)
    print("app_config:", app_config)
    print("verbosity:", verbosity)
    print("interactive:", interactive)
    print("using:", using)
    print("plan:", plan)
    print("apps:", apps)
    print(f"kwargs:{kwargs}")
    


# when the database interact with db call this signal
@receiver(connection_created)
def conn_db(sender,connection, **kwargs):
    print("----------------------------------")
    print("here the app is connected with db")
    print("sender:", sender)
    print("connection:", connection)
    print(f"kwargs:{kwargs}")
    

