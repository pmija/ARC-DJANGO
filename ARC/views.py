from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

#<--ADMIN-->
def AdminDashboard(request):
    return render(request, 'Admin/AdminDashboard.html')

def AdminCalendar(request):
    return render(request, 'Admin/AdminCalendar.html')

def AdminInbox(request):
    return render(request, 'Admin/AdminInbox.html')

def AdminAddUser(request):
    return render(request, 'Admin/AdminAddUser.html')

def AdminManageUser(request):
    return render(request, 'Admin/AdminManageUser.html')

def AdminEvaluateUser(request):
    return render(request, 'Admin/AdminEvaluateUser.html')

def AdminBorrowItem(request):
    return render(request, 'Admin/AdminBorrowItem.html')

def AdminReturnItem(request):
    return render(request, 'Admin/AdminReturnItem.html')

def AdminReturnItem2(request):
    return render(request, 'Admin/AdminReturnItem2.html')

def AdminViewInventory(request):
    return render(request, 'Admin/AdminViewInventory.html')

def AdminAddItem(request):
    return render(request, 'Admin/AdminAddItem.html')

def AdminViewResidencies(request):
    return render(request, 'Admin/AdminViewResidencies.html')

def AdminEvaluateResidency(request):
    return render(request, 'Admin/AdminEvaluateResidency.html')

def AdminManageTerm(request):
    return render(request, 'Admin/AdminManageTerm.html')

def AdminResidencyReport(request):
    return render(request, 'Admin/AdminResidencyReport.html')
#<--END-->

#<--STUDENT-->
def StudentDashboard(request):
    return render(request, 'Students/StudentDashboard.html')

def StudentDashboard2(request):
    return render(request, 'Students/StudentDashboard2.html')

def StudentInbox(request):
    return render(request, 'Students/StudentInbox.html')

def StudentBorrowItem(request):
    return render(request, 'Students/StudentBorrowItem.html')

def StudentReturnItem(request):
    return render(request, 'Students/StudentReturnItem.html')

def StudentReturnItem2(request):
    return render(request, 'Students/StudentReturnItem2.html')
#<--END-->

#<--FACULTY-->
def FacultyDashboard(request):
    return render(request, 'Faculty/FacultyDashboard.html')

def FacultyCalendar(request):
    return render(request, 'Faculty/FacultyCalendar.html')

def FacultyInbox(request):
    return render(request, 'Faculty/FacultyInbox.html')

def FacultyBorrowItem(request):
    return render(request, 'Faculty/FacultyBorrowItem.html')

def FacultyReturnItem(request):
    return render(request, 'Faculty/FacultyReturnItem.html')

def FacultyReturnItem2(request):
    return render(request, 'Faculty/FacultyReturnItem2.html')

def FacultyViewResidencies(request):
    return render(request, 'Faculty/FacultyViewResidencies.html')

def FacultyResidencyReport(request):
    return render(request, 'Faculty/FacultyResidencyReport.html')

def FacultyManageGroups(request):
    return render(request, 'Faculty/FacultyManageGroups.html')

def FacultyAddGroup(request):
    return render(request, 'Faculty/FacultyAddGroup.html')

def FacultyEditGroup(request):
    return render(request, 'Faculty/FacultyEditGroup.html')
#<--END-->

#<--TECHNICIAN AND FACULTY TECHNICIAN-->
def FacultyTechDashboard(request):
    return render(request, 'FacultyTech/FacultyTechDashboard.html')

def FacultyTechCalendar(request):
    return render(request, 'FacultyTech/FacultyTechCalendar.html')

def FacultyTechInbox(request):
    return render(request, 'FacultyTech/FacultyTechInbox.html')

def FacultyTechBorrowItem(request):
    return render(request, 'FacultyTech/FacultyTechBorrowItem.html')

def FacultyTechReturnItem(request):
    return render(request, 'FacultyTech/FacultyTechReturnItem.html')

def FacultyTechReturnItem2(request):
    return render(request, 'FacultyTech/FacultyTechReturnItem2.html')

def FacultyTechViewInventory(request):
    return render(request, 'FacultyTech/FacultyTechViewInventory.html')

def FacultyTechAddItem(request):
    return render(request, 'FacultyTech/FacultyTechAddItem.html')

def FacultyTechViewResidencies(request):
    return render(request, 'FacultyTech/FacultyTechViewResidencies.html')

def FacultyTechEvaluateResidency(request):
    return render(request, 'FacultyTech/FacultyTechEvaluateResidency.html')

def FacultyTechManageTerm(request):
    return render(request, 'FacultyTech/FacultyTechManageTerm.html')

def FacultyTechResidencyReport(request):
    return render(request, 'FacultyTech/FacultyTechResidencyReport.html')
#<--END-->
