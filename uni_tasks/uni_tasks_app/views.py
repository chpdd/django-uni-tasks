from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    context = {
        "numbers": range(1, 9)
    }
    return render(request, template_name="uni_tasks_app/main.html", context=context)


def task(request, task_number):
    context = dict()
    if task_number == 7:
        context = {
            "jpg_names": [f'media/{i}.jpg' for i in range(1, 9)]
        }
    if 1 <= task_number <= 8:
        return render(request,
                      template_name=f"uni_tasks_app/task{task_number}.html",
                      context=context)
    else:
        return HttpResponse("Нет задачи с таким номером")


def jquery_test(request):
    return render(request, template_name="uni_tasks_app/jquerry_test.html")
