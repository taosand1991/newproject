from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Personal
from portfolio.forms import PortfolioForm, UpdatePortfolioForm
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


@login_required
def portfolio_create(request):
    if request.method == "POST":
        form = PortfolioForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, "Your Portfolio has been created")
        return redirect('post_list')
    else:
        form = PortfolioForm(data=request.FILES)
    return render(request, 'portfolio/porfolio_page.html', {'form': form})


def portfolio_list(request):
    port_list = Personal.objects.all()
    paginator = Paginator(port_list, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.get_page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'portfolio/portfolio_list.html', {'contacts': contacts})


def portfolio_detail(request, pk):
    port = get_object_or_404(Personal, pk=pk)
    context = {'port': port}
    return render(request, 'portfolio/detail_list.html', context)


def update_list(request, pk):
    port = get_object_or_404(Personal, pk=pk)
    update_form = UpdatePortfolioForm(data=request.POST, instance=port or None, files=request.FILES)
    if update_form.is_valid():
        update_form.save()
        messages.success(request, 'Your portfolio has been updated successfully')
        return redirect('portfolio:port-detail', port.pk)

    else:
        update_form = UpdatePortfolioForm(instance=port)
        return render(request, 'portfolio/update_list.html', {'update_form': update_form,
                                                              'port': port})
