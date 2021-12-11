there is a dynamicprogramming project

------------------------------------------------------------------------------
title: jinja2
~>new things in django i learn : 1


NOTE: Open root setting.py file for jinja2 templating setting app

youtube link: https://youtu.be/6zJo84q2blo?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=936


referce link: https://stackoverflow.com/questions/30701631/how-to-use-jinja2-as-a-templating-engine-in-django-1-8

code part:
------------------------------------------------------------------------------
TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates/jinja2')],
        'APP_DIRS': True,
        'OPTIONS': {'environment': 'myproject.jinja2.Environment',}, 
        
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

------------------------------------------------------------------------------
------------------------------------------------------------------------------

~>new things in django i learn : 2

title: Filter
NOTE: Filter in django templates

youtube link:https://youtu.be/6zJo84q2blo?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=1733

django.docs : https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

referce link: https://www.geeksforgeeks.org/django-template-filters/


code part:template files
------------------------------------------------------------------------------
Filter Methods

    data: (original): heniL
    data: ("capfirst"): HeniL
    code: {{ variable | capfirst }}

    data: (original):
    data: ('default:"Nothing"'): pass the default value
    code: {{ variable|default:"Nothing" }}

    data: (original): abcd
    data: ('length'): 4
    code: {{ variable|length }}

    data: (original): heniL
    data: ('lower'): henil
    code: {{ variable|lower }}

    data: (original): heniL
    data: ('Upper'): HENIL
    code: {{ variable|upper }}

    data: (original): abcd
    data: ('slide'): ab
    code: {{ variable|slice:'value pass here' }}

    data: (original): hello world
    data: ('truncatechars'): h…
    code: {{ variable|truncatechars:'value pass here' }}

    data: (original): hello world
    data: ('truncatewords'): hello …
    code: {{ variable|truncatewords:'value pass here' }}

------------------------------------------------------------------------------


code part: logic file(filter_demo/views.py) imports->from datetime import datetime


code: {{ variable|date:'D d M Y' }}
code: {{ variable|time:'H:i' }}
code: {{ variable|date:'SHORT_DATE_FORMAT' }}
code: {{ variable|time:'TIME_FORMAT' }} 
------------------------------------------------------------------------------
-->output:
data: (original): Jan. 12, 2021, 8:18 a.m.
data: ('date'): Tue 12 Jan 2021
data: ('time:'H:i''): 08:18
data: ('date:'SHORT_DATE_FORMAT''): 01/12/2021
data: ('time:'TIME_FORMAT''): 8:18 a.m.
------------------------------------------------------------------------------

data: (original): 56.9622
data: (original): 56.0
data: (original): 56.37

data: ('floatformat'): 57.0
data: ('floatformat'): 56
data: ('floatformat'): 56.4

data: ('variable|floatformat:values'): 56.962
data: ('floatformat'): 56.000
data: ('floatformat'): 56.370

data: ('variable|floatformat:zero(0)'): 57
data: ('floatformat'): 56
data: ('floatformat'): 56

data: ('variable|floatformat:neg value(-)'): 56.962
data: ('floatformat'): 56
data: ('floatformat'): 56.370

code: {{ variable|truncatewords:'value pass here' }}
code: {{ variable|floatformat }}
code: {{ variable|floatformat:'values' }}
code: {{ variable|floatformat:0 }}
code: {{ variable|floatformat:'neg values' }}
------------------------------------------------------------------------------




------------------------------------------------------------------------------
title: if else jinja2
~>new things in django i learn : 3


NOTE: front end  html file

youtube link: 
https://youtu.be/6zJo84q2blo?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=3861

https://www.geeksforgeeks.org/if-django-template-tags/

code part:
------------------------------------------------------------------------------
 inputs: django("True")

code:
{% if django %}
{{ your data }}
{% endif %}

output:
django
inputs: django, 5

code:
{% if django and 5 %}
condition True
{% endif %}

output:
Condication True
inputs: django, 5

code:
{% if django or 5 %}
condition True
{% endif %}

output:
Condication True
inputs: django, 5

code:
{% if not 5 %}
condition True
{% endif %}

output:
Note: here the code is working bt condition is 'not' they why output is not visible

more eg. see the template
------------------------------------------------------------------------------




------------------------------------------------------------------------------
title: loops
~>new things in django i learn : 4


NOTE: front end  html file

youtube link: 
https://youtu.be/6zJo84q2blo?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=5298


code part:
------------------------------------------------------------------------------
------------------------------------------------------------------------------
