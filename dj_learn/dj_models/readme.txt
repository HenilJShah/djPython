
title:  showmigrations
~>new things in django i learn : 1


NOTE: 

youtube link: https://youtu.be/M6T1RgtS8b4?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=3157


referce link:

code part: 
------------------------------------------------------------------------------
python manage.py showmigrations
-------------------------------
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
modelsfiles_demo
 [ ] 0001_initial
sessions
 [ ] 0001_initial
------------------------------------------------------------------------------

title: makemigrations
~>new things in django i learn : 2


NOTE: 

youtube link: https://youtu.be/M6T1RgtS8b4?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=3239


referce link:

code part: 
------------------------------------------------------------------------------
python manage.py makemigrations
-------------------------------
Migrations for 'modelsfiles_demo':
  modelsfiles_demo/migrations/0001_initial.py
    - Create model stud_tb



NOTE: here the you can see the 'modelsfiles_demo' have one file

admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
modelsfiles_demo
 [ ] 0001_initial
sessions
 [ ] 0001_initial

------------------------------------------------------------------------------



title: sqlmigrate
~>new things in django i learn : 3


NOTE: 

youtube link: https://youtu.be/M6T1RgtS8b4?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=3383


referce link:

code part: 
------------------------------------------------------------------------------
python manage.py sqlmigrate <app_name>  <migrate_file_number> (hint: 0001)
eg:
    python manage.py sqlmigrate modelsfiles_demo  0001
---------------------------------------------------
BEGIN;
--
-- Create model stud_tb
--
CREATE TABLE "modelsfiles_demo_stud_tb" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "stud_id" integer NOT NULL, "stud_name" varchar(70) NOT NULL, "stud_email" varchar(70) NOT NULL, "stud_passwd" varchar(150) NOT NULL);
COMMIT;
------------------------------------------------------------------------------



title: migrate
~>new things in django i learn : 4


NOTE: apply the qry and create the TABLE

youtube link: https://youtu.be/M6T1RgtS8b4?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=3488

referce link:

code part: 
------------------------------------------------------------------------------
python manage.py migrate
------------------------
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, modelsfiles_demo, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying modelsfiles_demo.0001_initial... OK
  Applying sessions.0001_initial... OK
------------------------------------------------------------------------------