from django.shortcuts import render

def home(request):   #browser requests homepage from server
    return render(request,'home.html',{})   #curly are context dictionaries

def add(request):
    from random import randint
    num_1 = randint(0,10)
    num_2 = randint(0,10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct = int(old_num1) + int(old_num2)
        if not answer:
            my_answer= "Hey, You forgot to fill in the blank!"
            color = "danger"
            return render(request, 'divide.html', {'my_answer':my_answer,'color':color,'num_1': num_1, 'num_2': num_2})

        if int(answer) == correct:
            my_answer = "Correct " + old_num1 + "" "+" + "" + old_num2 + "=" + answer
            color = "success"

        else:
            my_answer = "Incorrect " + old_num1 + "" "+" + "" + old_num2 + "=" + str(correct) + " and not " + answer
            color = "danger"


        return render(request,'add.html',{'answer': answer, 'my_answer': my_answer,'num_1':num_1,'num_2':num_2,'color':color})

    return render(request,'add.html',{'num_1':num_1,'num_2':num_2})

def subtract(request):   #browser requests homepage from server
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct = int(old_num1) - int(old_num2)
        if not answer:
            my_answer = "Hey, You forgot to fill in the blank!"
            color = "danger"
            return render(request, 'divide.html',
                          {'my_answer': my_answer, 'color': color, 'num_1': num_1, 'num_2': num_2})

        if int(answer) == correct:
            my_answer = "Correct " + old_num1 + "" "-" + "" + old_num2 + "=" + answer
            color = "success"

        else:
            my_answer = "Incorrect " + old_num1 + "" "-" + "" + old_num2 + "=" + str(correct) + " and not " + answer
            color = "danger"

        return render(request, 'subtract.html',
                      {'answer': answer, 'my_answer': my_answer, 'num_1': num_1, 'num_2': num_2, 'color': color})



    return render(request,'subtract.html',{'num_1':num_1,'num_2':num_2})




def multiply(request):   #browser requests homepage from server
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct = int(old_num1) * int(old_num2)
        if not answer:
            my_answer = "Hey, You forgot to fill in the blank!"
            color = "danger"
            return render(request, 'divide.html',
                          {'my_answer': my_answer, 'color': color, 'num_1': num_1, 'num_2': num_2})

        if int(answer) == correct:
            my_answer = "Correct " + old_num1 + "" "*" + "" + old_num2 + "=" + answer
            color = "success"

        else:
            my_answer = "Incorrect " + old_num1 + "" "*" + "" + old_num2 + "=" + str(correct) + " and not " + answer
            color = "danger"

        return render(request, 'multiply.html',
                      {'answer': answer, 'my_answer': my_answer, 'num_1': num_1, 'num_2': num_2, 'color': color})
    return render(request,'multiply.html',{'num_1':num_1,'num_2':num_2})




def divide(request):   #browser requests homepage from server
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(1, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct = int(old_num1) / int(old_num2)
        if not answer:
            my_answer = "Hey, You forgot to fill in the blank!"
            color = "danger"
            return render(request, 'divide.html',
                          {'my_answer': my_answer, 'color': color, 'num_1': num_1, 'num_2': num_2})

        if float(answer) == correct:
            my_answer = "Correct " + old_num1 + "" "/" + "" + old_num2 + "=" + answer
            color = "success"

        else:
            my_answer = "Incorrect " + old_num1 + "" "/" + "" + old_num2 + "=" + str(correct) + " and not " + answer
            color = "danger"

        return render(request, 'divide.html',
                      {'answer': answer, 'my_answer': my_answer, 'num_1': num_1, 'num_2': num_2, 'color': color})
    return render(request,'divide.html',{'num_1':num_1,'num_2':num_2})