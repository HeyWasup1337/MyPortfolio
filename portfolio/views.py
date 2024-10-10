from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Author, Category, Work, Service, Testimony, Item, Message

from django.shortcuts import render
from .models import Category, Work, Service, Testimony

def index(request):
    categories = Category.objects.all()
    works = Work.objects.all()
    services = Service.objects.all()
    testimonies = Testimony.objects.all()

    context = {
        'categories': categories,
        'works': works,
        'services': services,
        'testimonies': testimonies,
    }

    return render(request, 'index.html', context)  # Убедитесь, что путь к шаблону правильный

def about(request):
    author = Author.objects.get()
    return render(request, 'about.html', {'author': author})


def work_detail(request, slug):
    work = get_object_or_404(Work, slug=slug)
    testimonies = Testimony.objects.all()
    context = {
        'work': work,
        'testimonies': testimonies,
    }
    return render(request, 'work_detail.html', context)


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f'Имя: {name}\nEmail: {email}\nСообщение: {message}'

        try:
            send_mail(subject, full_message, email, ['recipient@example.com'])
            messages.success(request, 'Ваше сообщение отправлено успешно!')
        except Exception as e:
            messages.error(request, f'Ошибка при отправке сообщения: {e}')

        return redirect('contact')

    return render(request, 'contact.html')
