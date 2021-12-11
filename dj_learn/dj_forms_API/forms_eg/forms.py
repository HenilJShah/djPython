from django import forms
from django.forms.widgets import NumberInput


class StudentRegistrationForm(forms.Form):
    name = forms.CharField(initial="abc", help_text="this is a help_text demo")
    phno = forms.IntegerField()
    email = forms.EmailField()


class Student_with_args(forms.Form):
    name = forms.CharField(
        label="Your name",
        initial="abc",
        label_suffix=" ",
        required=False,
        disabled=True,
        help_text="this is a help_text demo",
    )


class Student_with_widget(forms.Form):
    name = forms.CharField(
        widget=forms.HiddenInput
    )
    passwd = forms.CharField(
        widget=forms.PasswordInput(),
    )

    textarea = forms.CharField(
        widget=forms.Textarea()
    )

    NumberInput = forms.CharField(
        widget=forms.NumberInput()
    )

    EmailInput = forms.CharField(
        widget=forms.EmailInput()
    )

    URLInput = forms.CharField(
        widget=forms.URLInput()
    )

    DateInput = forms.CharField(
        widget=forms.DateInput()
    )

    DateTimeInput = forms.CharField(
        widget=forms.DateTimeInput()
    )

    TimeInput = forms.CharField(
        widget=forms.TimeInput()
    )

    Select = forms.CharField(
        widget=forms.Select()
    )

    # NullBoolenSelect = forms.CharField(
    #     widget = forms.NullBoolenSelect()
    # )

    # selectMultiple = forms.CharField(
    #     widget = forms.selectMultiple()
    # )

    RadioSelect = forms.CharField(
        widget=forms.RadioSelect()
    )

    CheckboxSelectMultiple = forms.CharField(
        widget=forms.CheckboxSelectMultiple()
    )

    FileInput = forms.CharField(
        widget=forms.FileInput()
    )

    MultipleHiddenInput = forms.CharField(
        widget=forms.MultipleHiddenInput()
    )

    SplitDateTimeWidget = forms.CharField(
        widget=forms.SplitDateTimeWidget()
    )

    SplitHiddenDateTimeWidget = forms.CharField(
        widget=forms.SplitHiddenDateTimeWidget()
    )

    # SplitDateWidget = forms.CharField(
    #     widget = forms.SplitDateWidget()
    # )

    text_with_attrs = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'somecss',
            'id': 'uniqueid'
        })
    )


class StudentRegistrationForm_demo(forms.Form):
    name = forms.CharField(initial='abc')
    phno = forms.IntegerField(initial='123')
    email = forms.EmailField(initial='abc@gmail.com')
    passwd = forms.CharField(widget=forms.PasswordInput())


class fieldForm(forms.Form):
    # min lenght
    min_len = forms.CharField(min_length=1, error_messages={
                              "required": "min_len 5"},
                              widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }))

    # max lenght
    max_len = forms.CharField(max_length=10, error_messages={
                              "required": "max_len 10"},
                              widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }))

    # wont to space True/Flase
    space_data = forms.CharField(strip=False, initial="              123              ",
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control'
                                     })
                                 )

    # empty_val defines
    empty_val = forms.CharField(
        empty_value="empty_val",
        error_messages={"required": "empty_val here"},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }))

    # error msg
    error_msg = forms.CharField(error_messages={"required": "error_msg here"},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                }))

    # int field
    num = forms.IntegerField(min_value=1, widget=forms.TextInput({
        'class': 'form-control',
    }))

    # decimal field
    price = forms.DecimalField(
        min_value=1,  # min 1
        max_value=40,  # max 40
        max_digits=4,  # 12.45 is four digits
        decimal_places=1,  # here the 12 after point sigle value like: 12.1
        widget=forms.TextInput({
            'class': 'form-control',
        }))

    # bool field
    agree = forms.BooleanField(label_suffix="", label="I Agree")
