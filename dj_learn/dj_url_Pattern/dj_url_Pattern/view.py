from django.http.response import HttpResponse


def home(request):
    return HttpResponse(""" 
    <!doctype html>
        <html lang="en">
            <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

                <title>Hello, world!</title>
            </head>
            <style>
            th{
                text-align: center;
            }
            </style>
        <body>
        <div class="container">
            <table class="table table-hover table-primary  mt-5">
        <thead>
            <tr>
            <th scope="col">
                <a href="http://127.0.0.1:8000/app_1/app1_1/">app1_home1</a>
            </th>
            <th scope="col">
            <a href="http://127.0.0.1:8000/app_1/app2_1/">app1_home2
            </a>      
            </th>
            </tr>
        </thead>
        <thead>
            <tr>
            <th scope="col"><a href="http://127.0.0.1:8000/app_2/app1_2/">app2_home1</a></th>
            <th scope="col"><a href="http://127.0.0.1:8000/app_2/app2_2/">app2_home2</a></th>
            </tr>

        </thead>
        <thead>
            <tr>
            <th scope="col"><a href="http://127.0.0.1:8000/app_3/app1_3/">app3_home1</a></th>
            <th scope="col"><a href="http://127.0.0.1:8000/app_3/app2_3/">app3_home2</a></th>
            </tr>

        </thead>
        </table>
            <hr>
        </div>
        <h1 class="text-center">2nd pattern</h1>
        <div class="container">
        <hr>
            <table class="table table-hover table-primary  mt-5">
        <thead>
            <tr>
            <th scope="col">
                <a href="http://127.0.0.1:8000/demo_app1/app1_1/">app1_home1</a>
            </th>
            <th scope="col">
            <a href="http://127.0.0.1:8000/demo_app1/app2_1/">app1_home2
            </a>      
            </th>
            </tr>
        </thead>
        <thead>
            <tr>
            <th scope="col"><a href="http://127.0.0.1:8000/demo_app2/app1_2/">app2_home1</a></th>
            <th scope="col"><a href="http://127.0.0.1:8000/demo_app2/app2_2/">app2_home2</a></th>
            </tr>

        </thead>
        <thead>
            <tr>
            <th scope="col"><a href="http://127.0.0.1:8000/demo_app3/app1_3/">app3_home1</a></th>
            <th scope="col"><a href="http://127.0.0.1:8000/demo_app3/app2_3/">app3_home2</a></th>
            </tr>

        </thead>
        </table>
        </div>

            <!-- Optional JavaScript; choose one of the two! -->

            <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

            <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
            -->
        </body>
        </html>
 """)
