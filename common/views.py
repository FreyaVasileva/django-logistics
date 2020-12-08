from django.shortcuts import render, redirect

# Create your views here.
from common.forms import ContactForm


def landing_page(req):
    return render(req, 'landing_page.html')


def about_us_page(req):
    return render(req, 'about_us.html')


def contact_us_page(req):
    if req.method == 'GET':
        context = {
            'form': ContactForm(),
        }
        return render(req, 'contact_us.html', context)
    else:
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form,
            }
            return render(req, 'contact_us.html', context)
