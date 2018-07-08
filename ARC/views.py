from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

#Forms
from ARC.forms import InventoryForm
from ARC.forms import LaboratoryForm

#Models
from ARC.models import Inventory
from ARC.models import Ref_Laboratory


# Create your views here.
def login(request):
    return render(request, 'login.html')

#AJAX
def EditLabAjax(request):
	if request.method == 'POST':
		tableid = request.POST['tableid']
		labtoedit = Ref_Laboratory.objects.filter(LabID=tableid)
		lab_serialized = serializers.serialize('json', labtoedit)
		
		return JsonResponse(lab_serialized, safe=False)

def BorrowItemAjax(request):
	if request.method == 'POST':
		id = request.POST['id']
		itemtoborrow = Inventory.objects.filter(ItemID=id )
		item_serialized = serializers.serialize('json', itemtoborrow)
		
		return JsonResponse(item_serialized, safe=False)

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

def AdminBorrowItem(request):
    return render(request, 'Admin/AdminBorrowItem.html')

def AdminReturnItem(request):
    return render(request, 'Admin/AdminReturnItem.html')

def AdminReturnItem2(request):
    return render(request, 'Admin/AdminReturnItem2.html')

def AdminViewInventory(request):
    return render(request, 'Admin/AdminViewInventory.html')


def AdminAddItem(request):
	if request.method == 'POST':
		form = InventoryForm(request.POST)
		if form.is_valid():
			itemname = request.POST.get('itemname', '')
			description = request.POST.get('description', '')
			item_type = request.POST.get('item_type', '')
			quantity = request.POST.get('quantity', '')
			uid = request.POST.get('uid', '')
			inventory_obj = Inventory(ItemName=itemname, Description=description, ItemType=item_type, Quantity=quantity, UniqueID=uid)
			inventory_obj.save();

			return render(request,'Admin/AdminAddItem.html', {'Check': ['Success']})

	else:
		form = InventoryForm()

	return render(request, 'Admin/AdminAddItem.html', {
        'form': form
    })

def AdminViewResidencies(request):
    return render(request, 'Admin/AdminViewResidencies.html')

def AdminEvaluateResidency(request):
    return render(request, 'Admin/AdminEvaluateResidency.html')

def AdminManageTerm(request):
    return render(request, 'Admin/AdminManageTerm.html')

def AdminResidencyReport(request):
    return render(request, 'Admin/AdminResidencyReport.html')

def AdminAddLaboratory(request):
	if request.method == 'POST':
		form = LaboratoryForm(request.POST)
		if form.is_valid():
			labname = request.POST.get('labname', '')
			roomno = request.POST.get('roomno', '')
			capacity = request.POST.get('capacity', '')
			inventory_obj = Ref_Laboratory(LaboratoryName=labname, RoomNum=roomno, Capacity=capacity)
			inventory_obj.save();

			return render(request,'Admin/AdminAddLaboratory.html', {'Check': ['Success']})

	else:
		form = InventoryForm()

	return render(request, 'Admin/AdminAddLaboratory.html', {
        'form': form
    })

def AdminEditLaboratory(request):
	laboratories = Ref_Laboratory.objects.all().values_list()
	
	if request.method == 'POST':
		
		labname = request.POST.get('labname', '')
		roomno = request.POST.get('roomno', '')
		capacity = request.POST.get('capacity', '')
		labid = request.POST.get('labid', '')
		#inventory_obj = Ref_Laboratory(LaboratoryName=labname, RoomNum=roomno, Capacity=capacity)
		#inventory_obj.save();
		Ref_Laboratory.objects.filter(LabID=labid).update(LaboratoryName=labname,RoomNum=roomno, Capacity=capacity)
		
		return render(request, 'Admin/AdminEditLaboratory.html', {'Labs': laboratories, 'Check': ['Success']})

	else:
		form = InventoryForm()

	return render(request, 'Admin/AdminEditLaboratory.html', {
        'Labs': laboratories
    })
	
	
#<--END-->

#<--STUDENT-->
def StudentProfile(request):
    return render(request, 'Students/StudentProfile.html')

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

def StudentSetResidency(request):
    return render(request, 'Students/StudentSetResidency.html')

def StudentEditResidency(request):
    return render(request, 'Students/StudentEditResidency.html')

def StudentGroupInventory(request):
    return render(request, 'Students/StudentGroupInventory.html')
#<--END-->

#<--FACULTY-->
def FacultyDashboard(request):
    return render(request, 'Faculty/FacultyDashboard.html')

def FacultyEvaluateUser(request):
    return render(request, 'Faculty/FacultyEvaluateUser.html')

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
	inventory = Inventory.objects.all().values_list()
	
	return render(request, 'FacultyTech/FacultyTechBorrowItem.html', {
        'inventory': inventory
    })
	

def FacultyTechReturnItem(request):
    return render(request, 'FacultyTech/FacultyTechReturnItem.html')

def FacultyTechReturnItem2(request):
    return render(request, 'FacultyTech/FacultyTechReturnItem2.html')

def FacultyTechBorrowedItems(request):
    return render(request, 'FacultyTech/FacultyTechBorrowedItems.html')

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

def FacultyTechGroupsInventory(request):
    return render(request, 'FacultyTech/FacultyTechGroupsInventory.html')
#<--END-->
