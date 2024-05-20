from django.http import HttpResponse
from django.shortcuts import render
import ast
import sympy
# Create your views here.
def index(req):
    return render(req,'index.html')

def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        print(expression)
        try:
            result = sympy.sympify(expression)
            return render(request, 'index.html', {'result': result})
        except Exception:

            result = "Error"
            return render(request, 'index.html', {'result': result})

    return render(request, 'index.html', {'error_message': "Method not allowed"})
