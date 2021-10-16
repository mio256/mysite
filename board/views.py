from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Thread, Response


class IndexView(generic.ListView):
    template_name = 'board/index.html'
    context_object_name = 'latest_thread_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Thread.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-latest_date')[:10]


class DetailView(generic.DetailView):
    model = Thread
    template_name = 'board/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Thread.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Thread
    template_name = 'board/results.html'


def create_thread(request):
    try:
        thread = Thread(
            thread_text=request.POST['thread_str'],
            pub_date=timezone.now(),
            latest_date=timezone.now(),
        )
    except (KeyError):
        # Redisplay the thread voting form.
        return render(request, 'board/index.html', {
            'error_message': "Error",
        })
    else:
        thread.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('board:index'))


def tweet(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    try:
        tweet = thread.response_set.create(
            response_text=request.POST['tweet_str'],
            name_text=request.POST['name_str'],
            tweet_date=datetime.now()
        )
    except (KeyError):
        # Redisplay the thread voting form.
        return render(request, 'board/detail.html', {
            'thread': thread,
            'error_message': "You didn't have a tweet.",
        })
    else:
        tweet.save()
        thread.update_date()
        thread.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('board:results', args=(thread.id,)))
