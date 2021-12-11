title:  {% include  %}
~>new things in django i learn : 1


NOTE:

youtube link: https://www.youtube.com/watch?v=ig7XPN_54X0&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=37


referce link:

code part:
------------------------------------------------------------------------------
base.html
----------
  {% comment %} here the we used 'include' tag {% endcomment %}
  {% include 'menu.html' %}
  
  <div class="container">
    <h1 class="display-1">{% block head %}heading{% endblock head %}</h1>
  </div>

index.html
----------
{% extends 'base.html' %}

{% block title %}Home{% endblock title %}


{% block head %}Home{% endblock head %}
------------------------------------------------------------------------------


with variable context pass
------------------------------------------------------------------------------
base.html
---------
  {% comment %} here the we used 'include' tag {% endcomment %}
  {% comment %} here the we used 'with' key variable to pass the values {% endcomment %}
  {% include 'menu.html' with py='python' %}
  
  <div class="container">
    <h1 class="display-1">{% block head %}heading{% endblock head %}</h1>
  </div>
  


menu.html
---------
<nav class="nav justify-content-center">
  <a class="nav-link active" href="{% url 'home' %}">HOME</a>
  <a class="nav-link" href="{% url 'about' %}">ABOUT US</a>
  <a class="nav-link disabled" href="#">{{py}}</a>
</nav>
------------------------------------------------------------------------------
