
title:  extends
~>new things in django i learn : 1


NOTE:

youtube link:https://youtu.be/SLkS0J5ArPk?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=289


referce link:

code part:
------------------------------------------------------------------------------
{% extends 'base.html' %}
------------------------------------------------------------------------------


title: block
~>new things in django i learn : 2


NOTE:

youtube link:https://youtu.be/SLkS0J5ArPk?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=411


referce link:

code part:
------------------------------------------------------------------------------
{% extends 'base.html' %}

{% comment %} here the you want to use base templates values and html templates values so use 'block.super' {% endcomment %}
{% block title %}{{ block.super }}| home{% endblock title %}

{% block heading %}{{ block.super }}hello home{% endblock heading %}
------------------------------------------------------------------------------