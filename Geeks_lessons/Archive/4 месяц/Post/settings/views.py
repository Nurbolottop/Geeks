from django.shortcuts import render,redirect
from django.core.mail import send_mail
from settings.models import Settings,Contact
from users.models import Blog
# # Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    blog = Blog.objects.all()
    return render(request, "index-2.html", locals())

def blog_detail(request,id):
    settings = Settings.objects.latest("id")
    blog = Blog.objects.get(id=id)
    return render(request, "blog-details.html", locals())

def contact(request):
    settings = Settings.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        reserv = Contact.objects.create(name = name,email=email, message=message)
        send_mail(
            f'{message}',
            f'Добрый день {name}, спасибо за обратную связь, мы скоро с вами свяжемся. Ваше почта: {email}',
            "nereply@somehost.local",
            [email]
        )
    return render(request,"contact.html", locals())