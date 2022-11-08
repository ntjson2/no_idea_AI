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
""" from jsonview.decorators import json_view """

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import HttpResponse
import json

""" @json_view
def save_example_form(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        # You could actually save through AJAX and return a success code here
        form.save()
        return {'success': True}

    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    return {'success': False, 'form_html': form_html} """


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
class CommentPost(SingleObjectMixin, FormView): # new
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):

        #form = self.form_class(self.request.POST)

        """   body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        print(received_json) """

        """ print(request.POST.getlist('id_comment')) """
        """  print(request.POST) """

        print(request.GET.getlist("cai"))


        """   y = json.loads(request.POST)

            # the result is a Python dictionary:
            print(y["cai"] + ")))")
         """

        ai1 = "asdf" 
        """  request.POST['id_comment', None] """
        print("------------------------------ ***************** ")
        for key, value in request.POST.items():
            print('Key1: %s' % (key) ) 
            print(f'Key2: {key}') #in Python >= 3.7
            print('Value1 %s' % (value) )
            print(f'Value2: {value}') #in Python >= 3.7

        if is_ajax(request=request):
            cmt = "AI response - " + ai1
            return JsonResponse({"ai_response": cmt}, status=200)
        else:
            return JsonResponse({"error": self.form_class.errors}, status=400)



        #if self.request.is_ajax and self.request.method == "POST":
            return JsonResponse({"instance": "hello"}, status=200)

            form = self.form_class(self.request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [ instance, ])
                    # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)

        #else    
            #return JsonResponse({"error": ""}, status=400)


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