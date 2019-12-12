from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Personal
from portfolio.forms import PortfolioForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


def portfolio_create(request):
    if request.method == "POST":
        form = PortfolioForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, "Your Portfolio has been created")
        return redirect('post_list')
    else:
        form = PortfolioForm(data=request.FILES)
    return render(request, 'portfolio/portfolio_page.html', {'form': form})

