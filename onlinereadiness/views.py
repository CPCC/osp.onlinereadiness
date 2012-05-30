import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template import Template
from django.utils import simplejson as json
from django.core.exceptions import PermissionDenied
from django.views.generic.simple import direct_to_template

from onlinereadiness import models
from onlinereadiness import forms

@login_required
def online_readiness_show_assessment(request):
    """
        Displays the Online Readiness Assessment.
    """
    if not request.user.groups.filter(name__in=['Students', 'Employees']):
        raise PermissionDenied

    if request.method == 'POST':
       form = forms.OnlineReadinessForm(request.POST)
       # Save the student's responses to the questions - answers will
       # be stored as a json formatted string.
       if form.is_valid():
           answers = []
           for item in form.cleaned_data:
               if item in form.fields:
                   answers.append({'question': form.fields[item].label,
                                   'answer': form.cleaned_data[item],
                                   'question_id': item})
           answers = json.dumps(answers)
           result = models.OnlineReadinessResult(
               student = request.user,
               answers = answers
           )
           result.save()
           # Display the results of the assessment based on the student's
           # responses (or a message indicating successful submission, etc.).
           return redirect('assessment:online-readiness-get-result',
                   result_id=result.pk)
    else:
       form = forms.OnlineReadinessForm()
    return direct_to_template(request,
                              'onlinereadiness/online-readiness.html',
                              {'form': form})

@login_required
def online_readiness_student_results(request, student_id):
    """
        Retrieves the assessment result records for the specified student.
    """
    if not request.user.groups.filter(name__in=['Students', 'Employees']):
        raise PermissionDenied

    # Make sure the logged-in user should have access to these results
    if (not request.user.groups.filter(name='Employees') and
        int(student_id) != request.user.id):
        raise PermissionDenied

    results = models.OnlineReadinessResult.objects.filter(student=student_id)
    return direct_to_template(request,
                              'onlinereadiness/online-readiness-student-results.html',
                              {'results': results,})


@login_required
def online_readiness_get_result(request, result_id):
    """
        Retrieves the specified assessment result record, scores it,
        and displays the outcome.
    """
    if not request.user.groups.filter(name__in=['Students', 'Employees']):
        raise PermissionDenied

    result = get_object_or_404(models.OnlineReadinessResult, id=result_id)

    # Make sure the logged-in user should have access to these results
    if (not request.user.groups.filter(name='Employees') and
        result.student != request.user):
        raise PermissionDenied

    answers = json.loads(result.answers)
    #TODO: this is self efficacy scoring - change to online readiness scoring
    total = 0
    for answer in answers:
        if(int('0'+answer['question_id']) == 14 ):
            total = total + (6 - float(answer['answer']))
        else:
            if(int('0'+answer['question_id']) >21 and int('0'+answer['question_id']) < 28):
                total = total + (6 - float(answer['answer']))
            else:
                if (int('0'+answer['question_id']) == 36 or int('0'+answer['question_id']) == 37):
                    total = total + (6 - float(answer['answer']))
                else:
                    total = total + float(answer['answer'])
    score = total
    compTotal = 0
    indeTotal = 0
    depTotal = 0
    acaTotal = 0
    olTotal = 0
    for answer in answers:
        if (int('0'+answer['question_id']) < 12):
            compTotal = compTotal + float(answer['answer'])
        if (int('0'+answer['question_id']) < 22 and int('0'+answer['question_id']) > 11):
            if ( int('0'+answer['question_id']) == 14 ):
                indeTotal = indeTotal + (6 - float(answer['answer']))
            else:
                indeTotal = indeTotal + float(answer['answer'])
        if (int('0'+answer['question_id']) < 28 and int('0'+answer['question_id']) > 21):
                depTotal = depTotal + (6 - float(answer['answer']))
        if (int('0'+answer['question_id']) < 33 and int('0'+answer['question_id']) > 27):
            olTotal = olTotal + float(answer['answer'])
        if (int('0'+answer['question_id']) > 32):
            if ( int('0'+answer['question_id']) == 36 or int('0'+answer['question_id']) == 37):
                acaTotal = acaTotal + (6 - float(answer['answer']))
            else:
                acaTotal = acaTotal + float(answer['answer'])

    compSkills = compTotal/11
    independant = indeTotal/10
    dependant = depTotal/6
    academic = acaTotal/13
    onlineDelivery = olTotal/5

    return direct_to_template(request, 'onlinereadiness/online-readiness-result.html', 
                              {'score': score, 'compSkills': compSkills, 
                              'independant': independant, 'dependant':dependant, 'academic': academic, 'onlineDelivery': onlineDelivery})
