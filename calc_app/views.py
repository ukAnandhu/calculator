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

    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
    
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero"
        else:
            result = "Invalid operation"
            
        return render(request, 'index.html', {'result': result})