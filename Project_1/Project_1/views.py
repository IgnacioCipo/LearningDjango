from django.http import HttpResponse
import datetime 

def greetings(request):
    return HttpResponse("<html><body><h1>Hello World from Django!</h1></body></html>")

def goodbye(request):
    return HttpResponse("Goodbye!")

def getTime(request):
    date = datetime.datetime.now()
    response = """<html>
        <body>
        <h1>
        Date: %s
        </h1>
        </body>
        </html>""" % date
    return HttpResponse(response)

def calculateMyAge(request, age, year):
    diference = year - 2023
    my_age = age + diference
    response = """<html>
        <body>
        <h2>
        Your age at %s will be %s
        </h2>
        </body>
        </html>""" % (year, my_age)
    return HttpResponse(response)