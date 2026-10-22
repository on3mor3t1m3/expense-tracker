from webbrowser import get
from django.shortcuts import redirect, render, get_object_or_404
from .models import Transaction


def home(request):
    all_transactions = Transaction.objects.all()

    income = sum(t.amount for t in all_transactions if t.transaction_type == 'income')
    expense = sum(t.amount for t in all_transactions if t.transaction_type == 'expense')

    balance = income - expense
    sort_by = request.GET.get('sort', 'date_desc')

    sort_options = {
        'date_desc': '-date',
        'date_asc': 'date',
        'amount_desc': '-amount',
        'amount_asc': 'amount',
    }
    transactions = all_transactions.order_by(sort_options.get(sort_by, '-date'))

    transaction_type = request.GET.get('type', '')
    search = request.GET.get('search', '').strip()
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')

    if (transaction_type in ('income', 'expense')):
        transactions = transactions.filter(transaction_type = transaction_type)
    if search:
        transactions = transactions.filter(title__icontains = search)
    if date_from:
        transactions = transactions.filter(date__gte = date_from)
    if date_to:
        transactions = transactions.filter(date__lte = date_to)

    context = {
        'transactions': transactions,
        'income': income,
        'expense': expense,
        'balance': balance,
        'selected_type': transaction_type,
        'search': search,
        'sort_by': sort_by,
        'date_from': date_from,
        'date_to': date_to,
        'income_chart': float(income),
        'expense_chart': float(expense),
    }
    return render(request, 'transactions/home.html', context)

def add_transaction(request):
    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        category = request.POST.get('category', 'other')
        amount = float(request.POST.get('amount'))
        description = request.POST.get('description')
        date = request.POST.get('date')
        title = request.POST.get('title')
        Transaction.objects.create(
            transaction_type = transaction_type,
            category = category,
            amount = amount,
            description = description,
            date = date,
            title = title
        )
        return redirect('home')
    return render(request, 'transactions/add_transaction.html')


def delete_transaction(request, transaction_id):
    if request.method == "POST":
        transaction = get_object_or_404(
            Transaction,
            id=transaction_id
        )
        transaction.delete()

    return redirect("home")

def edit_transaction(request, transaction_id):
    transaction=get_object_or_404(Transaction, id=transaction_id)
    
    if request.method == 'POST':
        transaction.title = request.POST.get('title')
        transaction.amount = request.POST.get('amount')
        transaction.transaction_type = request.POST.get('transaction_type')
        transaction.category = request.POST.get('category')
        transaction.date = request.POST.get('date')
        transaction.description = request.POST.get('description', '')
        transaction.save()

        return redirect('home')

    return render (request, 'transactions/edit_transaction.html', {'transaction': transaction})