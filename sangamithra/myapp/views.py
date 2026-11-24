from django.shortcuts import render

def Churnrate(request):
    ic =int(request.POST.get('InitialCustomers', '0'))
    cl = int(request.POST.get('CustomersLost', '0'))

    Churnrate=(cl/ic)*100 if request.method == 'POST' else 0

    print("InitialCustomers =", ic)
    print("CustomersLost =", cl)
    print("Churnrate =", Churnrate)
    return render(
        request,
        'myapp/churnrate.html',
        {'ic': ic, 'cl': cl, 'Churnrate':Churnrate}
    )