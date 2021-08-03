import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, FormMixin, FormView
from django.views.generic.list import ListView
from django.core.files.uploadedfile import InMemoryUploadedFile

from ajax.forms import PostModelForm

from .models import Post


class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': PostModelForm,
            'posts': Post.objects.all()
        }
        return render(request, self.template_name, context)


class FileJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, InMemoryUploadedFile):
            return o.read()
        return str(o)


class JSONResponsableFormMixin(FormMixin):

    def form_invalid(self, form):        
        response = json.dumps(form.errors)
        return JsonResponse({'errors': response}, content_type='application/json', status=400)

    def form_valid(self, form):
        response = json.dumps(form.cleaned_data, cls=FileJSONEncoder)
        return JsonResponse({'data': response}, content_type='application/json', status=200)


class PostCreateView(JSONResponsableFormMixin, CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)