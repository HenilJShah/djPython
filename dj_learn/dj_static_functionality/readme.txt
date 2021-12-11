there is a static_file_templating project

------------------------------------------------------------------------------
title: 
~>new things in django i learn : 1


NOTE: here the only tags, no eg. in project file

youtube link: https://youtu.be/sv6kMpCcVIs?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=729


referce link: 

code part:
------------------------------------------------------------------------------
eg.

{% load <packge> %}

{% load <packge.filename> %}

{% comment %} multipal load tags {% endcomment %}
{% load <packge> <packge.file> %}

{% comment %} here the inside the 'file' load 'packagename' {% endcomment %}
{% load <packgename> <packgename> from <import(filename)>  %}
------------------------------------------------------------------------------

------------------------------------------------------------------------------
title: 
~>new things in django i learn : 2


NOTE: 

youtube link: https://youtu.be/sv6kMpCcVIs?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=860


referce link: 

code part:
------------------------------------------------------------------------------
{% comment %} load static file {% endcomment %}
{% static 'img/1.jpg' %}

{% comment %} another type static file load {% endcomment %}
{% get_static_prefix %}img/2.jpg

{% comment %} load file/package  {% endcomment %}
{% load static %}

{% comment %} variable create {% endcomment %}
{% static 'img/1.jpg' as img %}

<img src="{{img}}">
------------------------------------------------------------------------------
