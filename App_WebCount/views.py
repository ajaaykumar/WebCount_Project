from django.shortcuts import render
import operator

def ShowIndex(request):
    return render(request,"index.html")


def Count(request):
    d1 = dict()
    comment = request.POST.get("comments")
    comment_list = comment.split()
    comment_length = len(comment_list)

    for comments in comment_list:
        if comments in d1:
            d1[comments] += 1
        else:
            d1[comments] = 1
    sort = sorted(d1.items(), key=operator.itemgetter(1),reverse=True)
    return render(request, "count.html", {'message':comment, 'len':comment_length, "dict":sort})


def AboutPage(request):
    return render(request,'About.html')