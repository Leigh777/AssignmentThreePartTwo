from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.db.models import Sum

now = timezone.now()


def home(request):
    return render(request, 'crm/home.html',
                  {'crm': home})


@login_required
def crochethook_delete(request, pk):
    crochethook = get_object_or_404(CrochetHook, pk=pk)
    crochethook.delete()
    return redirect('crm:crochethook_list')


@login_required
def crochethook_list(request):
    crochethooks = CrochetHook.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/crochethook_list.html',
                  {'crochethooks': crochethooks})


@login_required
def crochethook_new(request):
    if request.method == "POST":
        form = CrochetHookForm(request.POST)
        if form.is_valid():
            crochethook = form.save(commit=False)
            crochethook.created_date = timezone.now()
            crochethook.save()
            crochethooks = CrochetHook.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/crochethook_list.html',
                          {'crochethooks': crochethook})
    else:
        form = CrochetHookForm()
        # print("Else")
        return render(request, 'crm/crochethook_new.html', {'form': form})


@login_required
def crochethook_edit(request, pk):
    crochethook = get_object_or_404(CrochetHook, pk=pk)
    if request.method == "POST":
    # update
        form = CrochetHookForm(request.POST, instance=crochethook)
        if form.is_valid():
            crochethook = form.save(commit=False)
            crochethook.updated_date = timezone.now()
            crochethook.save()
            crochethook = CrochetHook.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/crochethook_list.html',
                          {'crochethooks': crochethook})
    else:  # edit
            form = CrochetHookForm(instance=crochethook)
    return render(request, 'crm/crochethook_edit.html', {'form': form})


@login_required
def yarn_list(request):
    yarns = Yarn.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/yarn_list.html', {'yarns': yarns})


@login_required
def yarn_new(request):
    if request.method == "POST":
        form = YarnForm(request.POST)
        if form.is_valid():
            yarn = form.save(commit=False)
            yarn.created_date = timezone.now()
            yarn.save()
            yarns = Yarn.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/yarn_list.html',
                          {'yarns': yarns})
    else:
        form = YarnForm()
        # print("Else")
        return render(request, 'crm/yarn_new.html', {'form': form})


@login_required
def yarn_edit(request, pk):
    yarn = get_object_or_404(Yarn, pk=pk)
    if request.method == "POST":
        form = YarnForm(request.POST, instance=yarn)
        if form.is_valid():
            yarn = form.save()
            # yarn.CrochetHook = yarn.id
            yarn.updated_date = timezone.now()
            yarn.save()
            yarns = Yarn.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/yarn_list.html', {'yarns': yarns})
    else:
        # print("else")
        form = YarnForm(instance=yarn)
        return render(request, 'crm/yarn_edit.html', {'form': form})


@login_required
def yarn_delete(request, pk):
    yarn = get_object_or_404(Yarn, pk=pk)
    yarn.delete()
    return redirect('crm:crochethook_list')


@login_required
def gift_list(request):
    gifts = Gift.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/gift_list.html', {'gifts': gifts})


@login_required
def gift_new(request):
    if request.method == "POST":
        form = GiftForm(request.POST)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.created_date = timezone.now()
            gift.save()
            gifts = Gift.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/gift_list.html',
                          {'gifts': gifts})
    else:
        form = GiftForm()
        # print("Else")
        return render(request, 'crm/gift_new.html', {'form': form})


@login_required
def gift_edit(request, pk):
    gift = get_object_or_404(Gift, pk=pk)
    if request.method == "POST":
        form = GiftForm(request.POST, instance=gift)
        if form.is_valid():
            gift = form.save()
            # gift.crochethook = gift.id
            gift.updated_date = timezone.now()
            gift.save()
            gifts = Gift.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/gift_list.html', {'gifts': gifts})
    else:
        # print("else")
        form = GiftForm(instance=gift)
        return render(request, 'crm/gift_edit.html', {'form': form})


@login_required
def gift_delete(request, pk):
    gift = get_object_or_404(Gift, pk=pk)
    gift.delete()
    return redirect('crm:crochethook_list')


@login_required
def summary(request, pk):
    crochethook = get_object_or_404(CrochetHook, pk=pk)
    crochethooks = CrochetHook.objects.filter(created_date__lte=timezone.now())
    yarns = Yarn.objects.filter(crochethook_size=pk)
    gifts = Gift.objects.filter(crochethook_size=pk)
    sum_yarn_charge = Yarn.objects.filter(crochethook_size=pk).aggregate(Sum('yarn_charge'))
    sum_gift_charge = Gift.objects.filter(crochethook_size=pk).aggregate(Sum('charge'))
    return render(request, 'crm/summary.html', {'crochethooks': crochethooks,
                                                'gifts': gifts,
                                                'yarns': yarns,
                                                'sum_yarn_charge': sum_yarn_charge,
                                                'sum_gift_charge': sum_gift_charge,})
