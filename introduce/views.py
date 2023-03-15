from django.shortcuts import render, get_object_or_404, redirect
from introduce.models import People
from django.core.paginator import Paginator
from introduce.forms import PeopleForm, UpdatePeopleForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def list(request):
    people = People.objects.all()
    paginator = Paginator(people, 5)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'people': items
    }
    return render(request, 'introduce/list.html', context)


def create(request):
    if request.method == "POST":
        form = PeopleForm(request.POST, request.FILES)
        print("----------------------------------------")
        print(form.is_valid())
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/')
    form = PeopleForm()
    return render(request, 'introduce/create.html', {'form': form})


def detail(request, id):
    if id is not None:
        item = get_object_or_404(People, pk=id)
        return render(request, 'introduce/detail.html', {'item': item})
    return HttpResponseRedirect('/')


def update(request, id):
    if request.method == 'POST':
        item = get_object_or_404(People, pk=id)
        password = request.POST.get('password', '')
        form = UpdatePeopleForm(request.POST, request.FILES, instance=item)
        print("------------------------------")
        print(form.errors)
        if password != item.password:
            messages.warning(request, "비밀번호가 틀렸습니다.")
            return redirect('update', id=id)
        elif form.is_valid():
            item = form.save()
    elif request.method == "GET":
        item = get_object_or_404(People, pk=id)
        form = PeopleForm(instance=item)
        return render(request, 'introduce/update.html', {'form': form, 'item': item})
    return render(request, 'introduce/detail.html', {'item': item})


def delete(request, id):
    item = get_object_or_404(People, pk=id)
    if request.method == 'POST' and 'password' in request.POST:
        if item.password == request.POST.get('password'):
            item.delete()
            return redirect('/')
        messages.warning(request, "비밀번호가 틀렸습니다.")
        return redirect('delete', id=id)
    return render(request, 'introduce/delete.html/', {'item': item})
