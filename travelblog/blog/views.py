from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import Blog
# Create your views here.

class BlogView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_blog = Blog.objects.all().order_by('-created_date')
        paginator = Paginator(all_blog, 6)
        page = self.request.GET.get('page')
        paged_blog = paginator.get_page(page)
        context['paged_cars'] = paged_blog
        context['all_blog'] = all_blog
        return context
        
class BlogDateilView(TemplateView):
    model = Blog
    template_name = 'blog/blog-single.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = Blog.objects.get(pk=kwargs.get('id'))
        len_text = len(blog.text)
        context['blog'] = blog
        context['text1'] = blog.text[:len_text//2]
        context['text2'] = blog.text[len_text//2:]
        return context
