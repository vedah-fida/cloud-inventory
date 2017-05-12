from django.shortcuts import render


# Create your views here.
def products_base(request):
    return render(request, 'product/base.html', {})


def products_inner_view(request):
    return render(request, 'product/index.html', {})

