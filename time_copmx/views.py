from django.shortcuts import render

def estimate_time_complexity(function_code):
    return "O(n^2)"

def home(request):
    if request.method == 'POST':
        function_code = request.POST.get('function_code')
        complexity = estimate_time_complexity(function_code)
        return render(request, 'result.html', {'function_code': function_code, 'complexity': complexity})
    return render(request, 'index.html')
