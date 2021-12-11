title: forms API
~>new things in django i learn : 1


NOTE:

youtube link: https://www.youtube.com/watch?v=CtD4u-Bncf8&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=47


referce link:

code part:
------------------------------------------------------------------------------
forms.py
--------
from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

---------
views.py
---------

from django.shortcuts import render
from .forms import StudentRegistrationForm
# Create your views here.

def home(request):
    fm = StudentRegistrationForm()
    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)

----------------
studentform.html
----------------

<!doctype html>
<html lang="en">
  <head>
    <title>student</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  </head>
  <body>
      <form action="" method="post">
          <table>
              {{fm}}
              <tr>
                  <th>
                      <button type="submit">submit</button>
                  </th>
              </tr>
          </table>
      </form>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
------------------------------------------------------------------------------


title: forms render options
~>new things in django i learn : 2


NOTE: here the "forms" is a simple example

youtube link: https://youtu.be/CtD4u-Bncf8?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=1863

referce link:

code part:
------------------------------------------------------------------------------
1. render all data
{{forms}}

2. as_table <tr> tag
{{forms.as_table}}

3. as_p <p> tag
{{forms.as_p}}

4. as_ul
{{forms.as_ul}}

5. field name manually
{{forms.name_of_field}}

eg.
forms.py
--------
from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


{{forms.name}}
{{forms.email}}
------------------------------------------------------------------------------

title: config_id_attribute
~>new things in django i learn : 3


NOTE: 

youtube link: https://www.youtube.com/watch?v=K_NJZd-YsoU&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=47

referce link:

code part:
------------------------------------------------------------------------------
# here we got page source in browser
view-source:http://127.0.0.1:8000/

see the "forms" fields code
<tr>
  <th>
  <label for="id_name">Name:</label>
  </th>
  <td>
  <input type="text" name="name" required id="id_name">
  </td>
</tr>
<tr>
  <th>
  <label for="id_email">Email:</label>
  </th>
  <td>
  <input type="email" name="email" required id="id_email">
  </td>
</tr>


# config_id_attribute of forms fields
eg:
id="id_name", id="id_email"


{% comment %} how to configure {% endcomment %}
views.py

def home(request):
    # normal form
    # fm = StudentRegistrationForm()

    # string with id
    # fm = StudentRegistrationForm(auto_id="some_%s")

    # fields with id
    # fm = StudentRegistrationForm(auto_id=True)

    # remove id
    # fm = StudentRegistrationForm(auto_id=False)

    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)

output in website(auto_id="some_%s")
<input type="text" name="name" required id="some_name"></td></tr>
<tr><th><label for="some_email">Email:</label></th><td><input type="email" name="email" required id="some_email">


output in website(auto_id=True)
<input type="text" name="name" required id="name"></td></tr>
<tr><th><label for="email">Email:</label></th><td><input type="email" name="email" required id="email">


output in website(auto_id=False)
<input type="text" name="name" required></td></tr>
<tr><th>Email:</th><td><input type="email" name="email" required>
------------------------------------------------------------------------------


title: config_lable_tags
~>new things in django i learn : 4


NOTE: 

youtube link: https://youtu.be/K_NJZd-YsoU?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=703

referce link:

code part:
------------------------------------------------------------------------------
{% comment %} how to configure {% endcomment %}
views.py

def home(request):
    # lable suffix = ":"
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = "=")
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = "A")
    fm = StudentRegistrationForm(auto_id=True, label_suffix = " ")
    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)

output on website site
------------------------------------------------------------------------------

title: dynamic initial values
~>new things in django i learn : 5


NOTE: 

youtube link: https://youtu.be/K_NJZd-YsoU?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=881

referce link:

code part:
------------------------------------------------------------------------------
{% comment %} how to configure {% endcomment %}
views.py

def home(request):
    fm = StudentRegistrationForm(auto_id=True, label_suffix = " ", initial = {'name':"abc"})
    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)

output on website site
------------------------------------------------------------------------------

title: forms orders
~>new things in django i learn : 6


NOTE: arrange the form fields

youtube link: https://www.youtube.com/watch?v=XV7VAOrJ3B8&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=48

referce link:

code part:
------------------------------------------------------------------------------
forms.py
---------
from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField()
    phno = forms.IntegerField()
    email = forms.EmailField()

views.py
---------
from django.shortcuts import render
from .forms import StudentRegistrationForm
# Create your views here.

def home(request):
    # field_order
    fm = StudentRegistrationForm(field_order=['name', 'email', 'phno'])





    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)
------------------------------------------------------------------------------



title: render forms field manually
~>new things in django i learn : 7


NOTE: fields and forms are an eg.

youtube link: https://www.youtube.com/watch?v=cVF7PAT8wlk&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=49

referce link:

code part:
------------------------------------------------------------------------------
=> the label of the field
{{field.label}}
eg:
    {{form.name.label}}

=> label tags <label>
{{field.label_tag}}

=> the id that will be used for this field
{{field.id_for_label}}
eg:
    {{form.name.id_for_label}}


=> the value of the field
{{field.value}}
eg:
    {{form.name.value}}


=> html_name
{{field.html_name}}
eg:
    {{form.name.html_name}}

=> any help text that has been associated with the field
{{field.help_text}}
eg:
    {{form.name.help_text}}

the field instancefrom the form class that this BoundField wraps. You can use it to access field attributes.
{{field.field}}
eg:
    {{form.name.field.help_text}}

hidden field
{{field.is_hidden}}

eg:
{% if field.is_hidden%}
    {# Do something special #}
{% endif%}



codings:
========
in html file "studentform.html"
{{fm.name.id_for_label}}

<form>
    <div>
      <label for="{{fm.name.id_for_label}}">name:</label>
      {{fm.name}}
    </div>

    <div>{{fm.name.label_tag}} {{fm.name}}</div>

    <div>
      {{fm.name.label_tag}} {% comment %} here the value is none then you can
      pass value with view.py and forms.py {% endcomment %} {{fm.name.value}}
      <br />
      <label>html value:</label>
      {{fm.name.html_name}}

      <br />
      <label>help text:</label>
      {{fm.name.help_text}}
    </div>
  </form>


forms.py
--------
from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField(initial="abc", help_text="this is a help_text demo")
    phno = forms.IntegerField()
    email = forms.EmailField()

output:
load the website 
------------------------------------------------------------------------------



title: field argument
~>new things in django i learn : 8


NOTE: here the field argument

youtube link: https://www.youtube.com/watch?v=XB3lhklF1Ts&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=51&t=149s

referce link:

code part:
------------------------------------------------------------------------------
=>required,
=>label,
=>label_suffix,
=>initial,
=>disabled,
=>help_text,
=>validation,
=>localize,
=>widget,


eg:
forms.py
========
class Student_with_widget(forms.Form):
    name = forms.CharField(
        label="Your name", 
        initial="abc",
        label_suffix=" ",
        required=False,
        disabled=True,
        help_text="this is a help_text demo",
    )

{% comment %} you can also used this method {% endcomment %}

fm_with_widget = Student_with_widget(initial={
        'name': 'Student'
})

html
=======

  <form action="" method="post">
    {{eg_widget.as_p}}
  </form>
------------------------------------------------------------------------------


title: field widget
~>new things in django i learn : 9


NOTE: here the field argument

youtube link: https://www.youtube.com/watch?v=HkW0NxzMZxg&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=52

referce link:

code part:
------------------------------------------------------------------------------
widget
=======
=>attrs
=>TextInput
=>NumberInput
=>EmailInput
=>URLInput
=>PasswordInput
=>HiddenInput
=>DateInput
=>DateTimeInput
=>TimeInput
=>Textarea
=>Select
=>NullBoolenSelect
=>selectMultiple
=>RadioSelect
=>CheckboxSelectMultiple
=>FileInput
=>MultipleHiddenInput
=>SplitDateTimeWidget
=>SplitHiddenDateTimeWidget
=>SplitDateWidget


------------------------------------------------------------------------------


title: data validation
~>new things in django i learn : 9


NOTE: 

youtube link: https://youtu.be/xXZbxxH1jTQ?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=483

referce link:

code part:
------------------------------------------------------------------------------
views.py
=========
def home(request):
    if request.POST:
        fmvalid = StudentRegistrationForm_demo(request.POST)
        print(fmvalid)
        if fmvalid.is_valid():
            print(f"\n\n\n\n{fmvalid.cleaned_data}\n\n\n\n")
            print(f"\n\n\n\n{fmvalid.cleaned_data['name']}\n\n\n\n")
            print(f"\n\n\n\n{fmvalid.cleaned_data['phno']}\n\n\n\n")
            print(f"\n\n\n\n{fmvalid.cleaned_data['email']}\n\n\n\n")
        # clear form fields
        fmvalid = StudentRegistrationForm_demo()
    else:
        fmvalid = StudentRegistrationForm_demo()

    data = {
        "eg_valid": fmvalid
    }
    return render(request, 'studentform.html', data)


forms.py
========
class StudentRegistrationForm_demo(forms.Form):
    name = forms.CharField()
    phno = forms.IntegerField()
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput())


html
=====
{% comment %} valid form {% endcomment %}
  <form method="POST">
    {% csrf_token %}
    {{eg_valid.as_p}}
    <button type="submit">submit</button>
  </form>
------------------------------------------------------------------------------


title: HttpResponseRedirect
~>new things in django i learn : 9


NOTE: 

youtube link: https://www.youtube.com/watch?v=o1JQ6zmMA9U&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=57

referce link:

code part:
------------------------------------------------------------------------------
views.py
=========
def home(request):
    if request.POST:
        fmvalid = StudentRegistrationForm_demo(request.POST)
        print(fmvalid)
        if fmvalid.is_valid():
            print(f"\n\n\n\n{fmvalid.cleaned_data}\n\n\n\n")
            print(f"\n\n\n\n{fmvalid.cleaned_data['name']}\n\n\n\n")
            print(f"\n\n\n\n{fmvalid.cleaned_data['phno']}\n\n\n\n")
            print(f"\n\n\n\n{fmvalid.cleaned_data['email']}\n\n\n\n")
        # clear form fields
        fmvalid = StudentRegistrationForm_demo()
    else:
        fmvalid = StudentRegistrationForm_demo()

    data = {
        "eg_valid": fmvalid
    }
    return render(request, 'studentform.html', data)


forms.py
========
class StudentRegistrationForm_demo(forms.Form):
    name = forms.CharField()
    phno = forms.IntegerField()
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput())


html
=====
{% comment %} valid form {% endcomment %}
  <form method="POST">
    {% csrf_token %}
    {{eg_valid.as_p}}
    <button type="submit">submit</button>
  </form>
------------------------------------------------------------------------------



title: Form Field Type
~>new things in django i learn : 10


NOTE: 

youtube link: https://www.youtube.com/watch?v=MbpBMmjfn6M&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=58

referce link:

code part:
------------------------------------------------------------------------------

------------------------------------------------------------------------------

