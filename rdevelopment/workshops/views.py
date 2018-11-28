from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import render

# Forms
from workshops.forms import PostForm

# Models
from workshops.models import Workshop

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Workshop
    ordering = ('created',)
    paginate_by = 30
    context_object_name = 'posts'

class PostsSearchView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/search.html'
    model = Workshop
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Workshop.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
