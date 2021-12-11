
title:  URL tag
~>new things in django i learn : 1


NOTE:

youtube link: https://www.youtube.com/watch?v=v0ZZIi4jkt8&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=36


referce link:

code part:
------------------------------------------------------------------------------
{% url 'urlname' %}

{% comment %} variable as a url {% endcomment %}
{% url 'urlname' as var %}

{% comment %} with args {% endcomment %}
{% url 'urlname' args1=value1, args2=value2 %}

{% comment %} values {% endcomment %}
{% url 'urlname' value1 value2 %}




------------------------------------------------------------------------------

title:  path()
~>new things in django i learn : 1


NOTE:

youtube link: https://youtu.be/v0ZZIi4jkt8?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=151


referce link:

code part:
------------------------------------------------------------------------------
path(route, views, kwargs=None, name=None)

{% comment %} url path with var {% endcomment %}

{% comment %} urls file {% endcomment %}
urlpatterns = [
    path('',views.home, name="home"),
]

{% url 'home' as h %}

<a href="{{h}}">home</a>



------------------------------------------------------------------------------
