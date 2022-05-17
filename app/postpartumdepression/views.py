from django.shortcuts import render

from postpartumdepression.models import Question, Answer


def home(request):
    if request.method == "GET":
        questions = Question.objects.all()
        return render(request, "home/home.html", context={"questions": questions})
    if request.method == "POST":
        answers = []
        answer10 = int(request.POST.get("10")[0])
        for n in range(1, 11):
            selected_answer = request.POST.get(str(n))
            answers.append(int(selected_answer[0]))
        points = sum(answers)


        return render(request, "home/solution.html", context={"points": points, "answer10": answer10})


