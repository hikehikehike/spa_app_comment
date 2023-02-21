from django.shortcuts import render, HttpResponseRedirect
from .models import Comment
from .forms import NewCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def comments_list_view(request):
    all_comments = Comment.objects.all()
    page = request.GET.get("page", 1)

    paginator = Paginator(all_comments, 25)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == "POST":
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect("/")
    else:
        comment_form = NewCommentForm()
    return render(
        request,
        "comment/comments_list.html",
        {
            "comments": comments,
            "comment_form": comment_form,
            "all_comments": all_comments,
        },
    )
