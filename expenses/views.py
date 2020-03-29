from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseModelForm


def index(request):

    expenses = Expense.objects.all()  # 查詢所有資料

    form = ExpenseModelForm()

    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect("/expenses")

    context = {
        'expenses': expenses,
        'form': form
    }

    return render(request, 'expenses/index.html', context)
