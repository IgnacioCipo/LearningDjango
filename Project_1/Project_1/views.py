from django.http import HttpResponse
import datetime 
from django.template import Template, Context

class Person():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

def greetings(request):
    person_1 = Person("Ignacio", "Cipolatti")
    my_themes = ["Templates", "Models", "Forms", "Views", "Deploy"]
    time = datetime.datetime.now()
    extern_doc = open("/home/cipo/Documents/LearningDjango/Project_1/Project_1/templates/my_template.html")
    template = Template(extern_doc.read())
    extern_doc.close()
    ctx = Context({"personal_name": person_1.name, "personal_lastname": person_1.lastname, "current_time": time, "themes": my_themes})
    renderized_doc = template.render(ctx)
    return HttpResponse(renderized_doc)

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