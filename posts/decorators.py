from functools import wraps
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from .models import Post
from django.contrib.auth.decorators import user_passes_test


def user_is_author(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        if post.author == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def is_author(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_author,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def is_public(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        if not post.is_public and request.user.is_authenticated:
            return function(request, *args, **kwargs)
        elif post.is_public:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

