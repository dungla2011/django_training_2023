from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.http import Http404
from django.urls import reverse

from django.views import generic

# def index(request):
#     lastest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # output = " <br> ".join("ID " + str(q.id) + '.' + q.question_text  for q in lastest_question_list)
#     # return HttpResponse(output)

#     context = {
#         "lastest_question_list": lastest_question_list
#     }
    
#     return render(request, "polls\index.html", context)
#     # template = loader.get_template("polls/index.html")
#     # return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "lastest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
        

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(id=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls\detail.html", {'question': question})
#     # res = "You are looking at question %s"
#     # return HttpResponse(res % question_id)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# def results(request, question_id):
#     # res = "You are looking at the result of question %s"
#     # return HttpResponse(res % question_id)
    
#     question = get_object_or_404(Question, pk=question_id)

#     # return HttpResponse(type(question));

#     return render(request, "polls/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    # res = "You are voting on question %s"
    # return HttpResponse(res % question_id)
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls\detail.html", 
            {
                'question': question, 
                "error_message": "Bạn chưa chọn một lựa chọn!"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


