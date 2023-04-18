from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Post, Category, Tag, Comment
from django.contrib.postgres.aggregates import ArrayAgg
from django.views import View
# Create your views here.

class BlogView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_blog = Post.objects.all().order_by('-created_date')
        paginator = Paginator(all_blog, 1)
        page = self.request.GET.get('page')
        paged_blog = paginator.get_page(page)
        context['paged_blog'] = paged_blog
        context['all_blog'] = all_blog
        return context
        
class BlogDateilView(TemplateView):
    model = Post
    template_name = 'blog/blog-single.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # blog = Blog.objects.prefetch_related('tags').get(pk=kwargs.get('id'))
        blog = Post.objects.get(pk=kwargs.get('id'))
        len_text = len(blog.text)
        categories = Category.objects.all()
        posts = Post.objects.all()
        tags = Tag.objects.all()

        # comments = Comment.objects.get(id=blog.id)
        # context['comment'] = comments

        context['categories'] = categories
        context['tags'] = tags
        context['blog'] = blog
        context['posts'] = posts
        context['text1'] = blog.text[:len_text//2]
        context['text2'] = blog.text[len_text//2:]
        return context


class CategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'blog/category.html'
    pk_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        kwargs["posts"] = Post.objects.filter(categories__in=self.get_queryset())
        return super().get_context_data(**kwargs)
    