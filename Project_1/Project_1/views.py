from django.http import HttpResponse

def greetings(request):
    return HttpResponse("Hello World from Django!")