from django.shortcuts import render,redirect, reverse
from django.http import Http404
from django import forms
from django.utils import timezone
from datetime import datetime

# Create your views here.

import time

from .models import Contest, Submition, Rank
from .models import PLATFORM_OPTIONS

from .tools import saveSubmitions, makeRankFromSubmitions
from spyder import manager


def getContestById(id):
    try:
        contest = Contest.objects.get(id=id)
    except Contest.DoesNotExist:
        raise Http404("Contest does not exist")
    return contest


def view_all(request):
    try:
        contests = Contest.objects.all()
    except Contest.DoesNotExist:
        raise Http404("Contest does not exist")
    return render(request, 'contest/list.html', {'contests': contests})


def view_index(request, contest_id):
    contest = getContestById(contest_id)
    return render(request, 'contest/base.html', {'contest': contest})


def view_submitions(request, contest_id):
    contest = getContestById(contest_id)
    submitions = Submition.objects.filter(localContestId=contest_id)
    return render(request, 'contest/submitions.html', {
        'contest': contest,
        'submitions': submitions
    })


def view_rank(request, contest_id):
    contest = getContestById(contest_id)
    ranks = Rank.objects.filter(localContestId=contest_id)
    return render(request, 'contest/rank.html', {
        'contest': contest,
        'problems': [chr(i + ord('A')) for i in range(26)][:contest.problemNum],
        'ranks': ranks
    })


class NewContestForm(forms.Form):
    platform = forms.ChoiceField(label='Platform', choices=PLATFORM_OPTIONS)
    contestId = forms.IntegerField(label="ID")
    passwd = forms.CharField(label="Password", required=False)
    newLength = forms.IntegerField(label="New Length", required=False)

def add_contest(request):
    if request.method == 'POST':
        form = NewContestForm(request.POST)
        if form.is_valid():
            form = form.clean()
            data = manager.get(
                form["platform"],
                form["contestId"],
                form["passwd"],
                form["newLength"]
            )
            newcontest = Contest(
                platform=form["platform"],
                contestId=data["contestId"],
                contestName=data["contestName"],
                password=form["passwd"],
                problemNum=data["problemNum"],
                startTime=datetime.utcfromtimestamp(data["startTime"]),
                endTime=datetime.utcfromtimestamp(data["endTime"]),
            )
            # print(newcontest)
            newcontest.save()
            print("add new contest, local id:", newcontest.id)
            saveSubmitions(newcontest.id, data["submitions"])
            makeRankFromSubmitions(newcontest.id, newcontest.problemNum)
            return redirect('contest:view_rank', contest_id=newcontest.id)
    else:
        form = NewContestForm()

    return render(request, 'contest/new.html', {'form': form})


def flush_submition(request, contest_id):
    contest = getContestById(contest_id)
    mktimestamp = lambda d : int(time.mktime(d.timetuple()))
    data = manager.get(
        contest.platform,
        contest.contestId,
        contest.password,
        mktimestamp(contest.endTime) - mktimestamp(contest.startTime)
    )
    saveSubmitions(contest.id, data["submitions"])
    return redirect('contest:view_submitions', contest_id=contest.id)


def flush_rank(request, contest_id):
    contest = getContestById(contest_id)
    makeRankFromSubmitions(contest.id, contest.problemNum)
    return redirect('contest:view_rank', contest_id=contest.id)

