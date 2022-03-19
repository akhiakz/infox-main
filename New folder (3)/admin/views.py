from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request,"BRadmin_index.html")

def BRadmin_Reportedissue_department(request):
    departments=department.objects.all()
    return render(request, 'BRadmin_Reportedissue_department.html',{'department':departments})

def BRadmin_Reportedissue(request,id):
    departments=department.objects.get(id=id)
    designations=designation.objects.filter(department_id=departments)
    return render(request, 'BRadmin_Reportedissue.html',{'department':departments,'designation':designations})

def BRadmin_ReportedissueShow(request,id):
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations)
    departments=department.objects.filter()
    reported_issues=reported_issue.objects.all()
    return render(request,'BRadmin_ReportedissueShow.html',{'department':departments,'designation':designations,'reported_issue':reported_issues,'user_registration':user})

def BRadmin_ReportedissueShow1(request,id):
    reported_issues=reported_issue.objects.get(id=id)
    return render(request,'BRadmin_ReportedissueShow1.html',{'reported_issue':reported_issues}) 

# def BRadmin_ReportedissueTrainer(request):
#     designations=designation.objects.all()
#     user=user_registration.objects.all()
#     reported_issues=reported_issue.objects.all()
#     return render(request,'BRadmin_ReportedissueTrainer.html',{"reported_issue":reported_issues})   

# def BRadmin_ReportedissueTrainer1(request,id):
#     reported_issues=reported_issue.objects.get(id=id)
#     return render(request,'BRadmin_ReportedissueTrainer1.html')

# def BRadmin_ReportedissueProjectManager(request):
#     designations=designation.objects.all
#     user=user_registration.objects.all()
#     reported_issues=reported_issue.objects.all()
#     return render(request,'BRadmin_ReportedissueProjectManager.html',{"reported_issue":reported_issues}) 

# def BRadmin_ReportedissueProjectManager1(request):
#     reported_issues=reported_issue.objects.get(id=id)
#     return render(request, 'BRadmin_ReportedissueProjectManager1.html',{"reported_issue":reported_issues}) 

# def BRadmin_ReportedissueTeamLeader(request):
#     designations=designation.objects.all
#     user=user_registration.objects.all()
#     reported_issues=reported_issue.objects.all()
#     return render(request, 'BRadmin_ReportedissueTeamLeader.html',{"reported_issue":reported_issues}) 

# def BRadmin_ReportedissueTeamLeader1(request,id):
#     reported_issues=reported_issue.objects.get(id=id)
#     return render(request, 'BRadmin_ReportedissueTeamLeader1.html',{"reported_issue":reported_issues}) 

# def BRadmin_ReportedissueDevelopers(request):
#     designations=designation.objects.all
#     user=user_registration.objects.all()
#     reported_issues=reported_issue.objects.all()
#     return render(request, 'BRadmin_ReportedissueDevelopers.html',{"reported_issue":reported_issues}) 
    
# def BRadmin_ReportedissueDevelopers1(request,id):
#     reported_issues=reported_issue.objects.get(id=id)
#     return render(request, 'BRadmin_ReportedissueDevelopers1.html',{"reported_issue":reported_issues})