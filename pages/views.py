from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def my_first_view(request):
    return render(request, "base.html")

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == "POST":
        #validate data and send email
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Valid form")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            #message_body = f"This is an email from your Capstone. \nName:{name}\nEmail:{email}\nMessage:\n{message}"
            message_body = render_to_string("content/email.html", request.POST)

            #send the email
            send_mail(
                "Capstone email",
                message,
                email,
                ['youngzsbg@gmail.com'],
                html_message=message_body
            )

            return render(request, 'pages/contact.html', {"form": ContactForm(),"sent": 1})

        else:
            print("Invalid form")

    else:
        # show the page
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {'form': form, "sent": 0})

