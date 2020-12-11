from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.decorators import group_required
from consignment.form import ConsignmentForm
from consignment.models import Consignment


def is_worker(user):
    return user.groups.filter(name='worker').exists()


@login_required
def consignments_list(request):
    user = request.user
    if user.is_superuser or is_worker(user):
        context = {
            'consignments': set(Consignment.objects.all()),
            'is_worker': True,
        }
    else:
        context = {
            'consignments': set(Consignment.objects.filter(receiver_id=user.id)),
            'is_worker': is_worker(request.user),
        }
    return render(request, 'consignments/list-consignments.html', context)


@login_required
def consignment_details(request, pk):
    consignment = Consignment.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'consignment': consignment,
            'is_worker': is_worker(request.user),
        }

        return render(request, 'consignments/details-consignment.html', context)


@group_required(['worker'])
def edit_consignment(request, pk):
    consignment = Consignment.objects.get(pk=pk)
    if request.method == 'GET':
        form = ConsignmentForm(instance=consignment)

        context = {
            'form': form,
            'consignment': consignment,
            'is_worker': is_worker(request.user),
        }
        return render(request, 'consignments/edit_consignment.html', context)
    else:
        form = ConsignmentForm(request.POST, instance=consignment)
        if form.is_valid():
            form.save()

            return redirect('consignment details', consignment.pk)

        context = {
            'form': form,
            'consignment': consignment,
            'is_worker': is_worker(request.user),
        }

        return render(request, 'consignments/edit_consignment.html', context)


@group_required(['worker'])
def delete_consignment(request, pk):
    consignment = Consignment.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'consignment': consignment,
            'is_worker': is_worker(request.user),
        }

        return render(request, 'consignments/delete-consignment.html', context)
    else:
        consignment.delete()
        return redirect('list consignments')


@group_required(['worker'])
def create_consignment(request):
    if request.method == 'GET':
        context = {
            'form': ConsignmentForm(),
            'is_worker': is_worker(request.user),
        }

        return render(request, 'consignments/create_consignment.html', context)
    else:
        form = ConsignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list consignments')

        context = {
            'form': form,
            'is_worker': is_worker(request.user),
        }

        return render(request, 'consignments/create_consignment.html', context)
