from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView # new
from django.views.generic.detail import SingleObjectMixin # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse # new
from .forms import CommentForm
from .models import Article
from .models import aiw #testing

from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import HttpResponse
import json
import random

import os
import openai




def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article    
    template_name = "article_list.html"


class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"
  

    def get_context_data(self, **kwargs):
       # Call the base implementation first to get a context
       context = super().get_context_data(**kwargs)
       #context.update({'phrase': 'yaabb'}) #AI testing
       context['form'] = CommentForm()
       return context

# Comment post here
class CommentPost(SingleObjectMixin, FormView): 
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):

        origComment = request.POST.get('comment', None) + " "

        #Testing key and values
        """  for key, value in request.POST.items():           
            print(f'Key2: {key}') #in Python >= 3.7          
            print(f'Value2: {value}') #in Python >= 3.7 """

        # Ajax call
        if is_ajax(request=request):
            form = self.form_class(self.request.POST)
            if form.is_valid():

                """   # Fake AI - ready for the real stuff
                cmt = origComment + " " + random.choice(['- so said the bear who had a problem with pizza.',
                'and big tree thinks about this too.',
                'or crabs a night with your favorite slippers.', 
                'and other stuff not worth mentioning.', 
                '- like for real.', 
                'but not really, it is just a mess.',
                ' - said the big grumpy chicken.']) 
                """

                # Real AI
                openai.api_key = os.getenv("OPENAI_API_KEY")

                response = openai.Completion.create(
                    model="text-davinci-002",
                    prompt=origComment,
                    temperature=0.5,
                    max_tokens=250,
                    top_p=0.48, 
                    frequency_penalty=0.96,
                    presence_penalty=1.01
                )
                # print(response)

                return JsonResponse({"ai_response": response}, status=200)                 
            else:
                return JsonResponse({"error": "Please provide a phrase"}, status=400)
               
        else:
            self.object = self.get_object()
            return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleDetailView(LoginRequiredMixin, View):    
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user
    


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user



class ArticleCreateView(LoginRequiredMixin, CreateView):  
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)