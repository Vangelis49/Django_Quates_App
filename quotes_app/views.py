#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm

def quotes_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes_list.html', {'quotes': quotes})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes_list')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})
