from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),



    #<--------------DIRECTORIES------------>

    #<--ADMIN-->
    #Dashboard
    url(r'^Admin$', views.AdminDashboard, name='Admin/Dashboard'),
    url(r'^Admin/Calendar$', views.AdminCalendar, name='Admin/Calendar'),
    #Accounts
    url(r'^Admin/ManageUser$', views.AdminManageUser, name='Admin/ManageUser'),
    url(r'Admin/AddUser$', views.AdminAddUser, name='Admin/AddUser'),
    #Inventory
    url(r'^Admin/ViewInventory$', views.AdminViewInventory, name='Admin/ViewInventory'),
    url(r'^Admin/AddItem$', views.AdminAddItem, name='Admin/AddItem'),
    #Residency
    url(r'^Admin/ViewResidencies$', views.AdminViewResidencies, name='Admin/ViewResidencies'),
    url(r'^Admin/EvaluateResidency$', views.AdminEvaluateResidency, name='Admin/EvaluateResidency'),
    url(r'^Admin/ManageTerm$', views.AdminManageTerm, name='Admin/ManageTerm'),
    #Item Lending
    url(r'^Admin/BorrowItem$', views.AdminBorrowItem, name='Admin/BorrowItem'),
    url(r'^Admin/ReturnItem$', views.AdminReturnItem, name='Admin/ReturnItem'),
    url(r'^Admin/ReturnItem2$', views.AdminReturnItem2, name='Admin/ReturnItem2'),
    #Reports
    url(r'^Admin/ResidencyReport$', views.AdminResidencyReport, name='Admin/ResidencyReport'),
    #Inbox
    url(r'^Admin/Inbox$', views.AdminInbox, name='Admin/Inbox'),
    #Laboratory
    url(r'^Admin/AddLaboratory', views.AdminAddLaboratory, name='Admin/AddLaboratory'),
    url(r'^Admin/EditLaboratory$', views.AdminEditLaboratory, name='Admin/EditLaboratory'),

    #<--END-->

    #<--STUDENT-->
    #Profile
    url(r'Student/Profile$', views.StudentProfile, name='Student/Profile'),
    #Dashboard
    url(r'^Student$', views.StudentDashboard, name='Student/Dashboard'),
    url(r'^Student/Calendar$', views.StudentDashboard2, name='Student/Calendar'),
    #Item Lending
    url(r'^Student/BorrowItem$', views.StudentBorrowItem, name='Student/BorrowItem'),
    url(r'^Student/ReturnItem$', views.StudentReturnItem, name='Student/ReturnItem'),
    url(r'^Student/ReturnItem2$', views.StudentReturnItem2, name='Student/ReturnItem2'),
    #Inbox
    url(r'^Student/Inbox$', views.StudentInbox, name='Student/Inbox'),
    #Residency
    url(r'Student/SetResidency$', views.StudentSetResidency, name='Student/SetResidency'),
    #<--END-->

    #<--FACULTY-->
    #Dashboard
    url(r'^Faculty$', views.FacultyDashboard, name='Faculty/Dashboard'),
    url(r'^Faculty/Calendar$', views.FacultyCalendar, name='Faculty/Calendar'),
    #Groups
    url(r'Faculty/EvaluateUser$', views.FacultyEvaluateUser, name='Faculty/EvaluateUser'),
    url(r'Faculty/ManageGroups$', views.FacultyManageGroups, name='Faculty/ManageGroups'),
    url(r'Faculty/AddGroup$', views.FacultyAddGroup, name='Faculty/AddGroup'),
    url(r'Faculty/EditGroup$', views.FacultyEditGroup, name='Faculty/EditGroup'),
    #Residency
    url(r'^Faculty/ViewResidencies$', views.FacultyViewResidencies, name='Faculty/ViewResidencies'),
    #Item Lending
    url(r'^Faculty/BorrowItem$', views.FacultyBorrowItem, name='Faculty/BorrowItem'),
    url(r'^Faculty/ReturnItem$', views.FacultyReturnItem, name='Faculty/ReturnItem'),
    url(r'^Faculty/ReturnItem2$', views.FacultyReturnItem2, name='Faculty/ReturnItem2'),
    #Reports
    url(r'^Faculty/ResidencyReport$', views.FacultyResidencyReport, name='Faculty/ResidencyReport'),
    #Inbox
    url(r'^Faculty/Inbox$', views.FacultyInbox, name='Faculty/Inbox'),
    #<--END-->

    #<--TECHNICIAN AND FACULTY-TECHNICIAN-->
    #Dashboard
    url(r'^FacultyTech$', views.FacultyTechDashboard, name='FacultyTech/Dashboard'),
    url(r'^FacultyTech/Calendar$', views.FacultyTechCalendar, name='FacultyTech/Calendar'),
    #Inventory
    url(r'^FacultyTech/ViewInventory$', views.FacultyTechViewInventory, name='FacultyTech/ViewInventory'),
    url(r'^FacultyTech/AddItem$', views.FacultyTechAddItem, name='FacultyTech/AddItem'),
    #Residency
    url(r'^FacultyTech/ViewResidencies$', views.FacultyTechViewResidencies, name='FacultyTech/ViewResidencies'),
    url(r'^FacultyTech/EvaluateResidency$', views.FacultyTechEvaluateResidency, name='FacultyTech/EvaluateResidency'),
    url(r'^FacultyTech/ManageTerm$', views.FacultyTechManageTerm, name='FacultyTech/ManageTerm'),
    #Item Lending
    url(r'^FacultyTech/BorrowItem$', views.FacultyTechBorrowItem, name='FacultyTech/BorrowItem'),
    url(r'^FacultyTech/ReturnItem$', views.FacultyTechReturnItem, name='FacultyTech/ReturnItem'),
    url(r'^FacultyTech/ReturnItem2$', views.FacultyTechReturnItem2, name='FacultyTech/ReturnItem2'),
    #Reports
    url(r'^FacultyTech/ResidencyReport$', views.FacultyTechResidencyReport, name='FacultyTech/ResidencyReport'),
    #Inbox
    url(r'^FacultyTech/Inbox$', views.FacultyTechInbox, name='FacultyTech/Inbox'),
    #<--END-->

    #<-----------END OF DIRECTORIES--------->
    ]
