from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume


def home(request):
    if request.POST:
        resumes = ResumeForm(request.POST)
        resumes.save()
        return redirect("resumes:home")
    resumes = Resume.objects.all()
    return render(request, "resumes/home.html", {"resumes": resumes})


def new(request):
    resumes = ResumeForm()
    return render(request, "resumes/new.html", {"forms": resumes})


def show(request, id):
    resumes = get_object_or_404(Resume, id=id)
    if request.POST:
        forms = ResumeForm(request.POST, instance=resumes)
        forms.save()
        return redirect("resumes:home")
    return render(request, "resumes/show.html", {"resumes": resumes})


def edit(request, id):
    resumes = get_object_or_404(Resume, id=id)
    forms = ResumeForm(instance=resumes)
    return render(request, "resumes/edit.html", {"resumes": resumes, "forms": forms})


def delete(request, id):
    resumes = get_object_or_404(Resume, id=id)
    if request.POST:
        resumes.delete()
        return redirect("resumes:home")
    return render(request, "resumes/delete.html", {"resumes": resumes})


# Create your views here.
