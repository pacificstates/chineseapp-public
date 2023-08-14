from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Book, CustomCards
from .forms import CreateNewCard
from django.db.models import Max
import random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(response):
    return render(response, "home.html")

def Lesson(request, book, lesson):
    request.session['book'] = book
    request.session['lesson'] = lesson

    from_next = request.GET.get('from_next_card', False)

    try:
        vocablist = Book.objects.filter(book=book, lesson=lesson)

        if 'card_index' not in request.session or not from_next:
            request.session['card_index'] = 0

        card_index = request.session['card_index']

        return render(request, "lesson.html", {"vocablist": vocablist[card_index]})
    except Book.DoesNotExist:
        return HttpResponse(f"No data found")
    
def next_card(request):
    book_id = request.session.get('book')
    lesson_id = request.session.get('lesson')
    card_index = request.session.get('card_index', 0)

    card_index += 1

    request.session['card_index'] = card_index

    redirect_url = reverse('Lesson', args=(book_id, lesson_id))
    return HttpResponseRedirect(f"{redirect_url}?from_next_card=true")

@login_required
def create(request):
    if request.method == "POST":
        form = CreateNewCard(request.POST)

        if form.is_valid():
            c = form.cleaned_data['chinese']
            p = form.cleaned_data['pinyin']
            e = form.cleaned_data['english']
            card = CustomCards(user=request.user, chinese=c, pinyin=p, english=e)
            card.save()
    else:
        form = CreateNewCard()
    return render(request, "create.html", {"form": form})

@login_required
def customCards(request):
    list = CustomCards.objects.filter(user=request.user)
    if list.exists():
        random_card = random.choice(list)
        return render(request, "custom.html", {'card': random_card})
    else:
        return render(request, "no_cards.html")

def nextCustom(request):
    return HttpResponseRedirect('/customcards')

def BookNum(response, id):
    highest_lesson = Book.objects.filter(book=id).aggregate(Max('lesson'))['lesson__max']
    context = {
        'range': range(1, highest_lesson + 1),
        'book': id
    }
    return render(response, 'booknum.html', context)