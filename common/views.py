from django.shortcuts import render, redirect

# Create your views here.
from common.forms import ContactForm


def landing_page(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'landing_page.html', context)


def about_us_page(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'about_us.html', context)


def contact_us_page(req):
    if req.method == 'GET':
        context = {
            'form': ContactForm(),
            'is_worker': req.user.groups.filter(name='worker').exists(),
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
                'is_worker': req.user.groups.filter(name='worker').exists(),
            }
            return render(req, 'contact_us.html', context)
