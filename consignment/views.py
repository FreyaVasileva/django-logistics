from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.decorators import group_required


@login_required
def consignments_list(req):
    pass


@login_required
def consignment_details(req, pk):
    pass


def edit_consignment(req, pk):
    pass


@group_required(['worker'])
def delete_consignment(req, pk):
    pass


@group_required(['worker'])
def create_consignment(req):
    pass
