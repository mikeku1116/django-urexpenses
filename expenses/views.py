from django.shortcuts import render
from .forms import ExpenseModelForm


def index(request):

    form = ExpenseModelForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context)
