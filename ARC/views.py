from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Max
import datetime
from django.shortcuts import redirect
from django.shortcuts import reverse

#Models
from ARC.models import Inventory
from ARC.models import Ref_Laboratory
from ARC.models import AuditTable_Inventory
from ARC.models import User
from ARC.models import ActualResidency

# Create your views here.
def login(request):
    return render(request, 'login.html')

def timeinout(request):
	if request.method == 'POST':
		return render(request, 'timein-out.html')
	else:
		return render(request, 'timein-out.html')
	
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
		
def BorrowItemManAjax(request):
	if request.method == 'POST':
		uniqueid = request.POST['uniqueid']
		itemtoborrow2 = Inventory.objects.filter(ItemUniqueID=uniqueid )
		item2_serialized = serializers.serialize('json', itemtoborrow2)
		
		return JsonResponse(item2_serialized, safe=False)
		
def UserInfoAjax(request):
	if request.method == 'POST':
		studentid = request.POST['studentid']
		userinfo = User.objects.filter(NFCUniqueID=studentid)
		user_serialized = serializers.serialize('json', userinfo)
		
		return JsonResponse(user_serialized, safe=False)
		
def TimeInOutAjax(request):
	if request.method == 'POST':
		studentid = request.POST['studentid']
		res = ActualResidency.objects.all().values_list().filter(Student=studentid, ResidencyStatus=1)
		if not res:
			actualres = ActualResidency(Student=studentid, DateTime=datetime.datetime.now(), TimeIn=datetime.datetime.now(), ResidencyStatus=1)
			actualres.save()
		else:
			ActualResidency.objects.filter(Student=studentid, ResidencyStatus=1).update(TimeOut=datetime.datetime.now(),  ResidencyStatus=2)
		res_serialized = serializers.serialize('json', res)
		return JsonResponse(res_serialized, safe=False)

#<--ADMIN-->
def AdminDashboard(request):
    return render(request, 'Admin/AdminDashboard.html')

def AdminCalendar(request):
    return render(request, 'Admin/AdminCalendar.html')

def AdminInbox(request):
    return render(request, 'Admin/AdminInbox.html')

def AdminAddUser(request):
    return render(request, 'Admin/AdminAddUser.html')

def AdminManageUsers(request):
    return render(request, 'Admin/AdminManageUsers.html')

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
		itemname = request.POST.get('itemname', '')
		description = request.POST.get('description', '')
		item_type = request.POST.get('item_type', '')
		quantity = request.POST.get('quantity', '')
		uid = request.POST.get('uid', '')
		
		inventory_obj = Inventory(ItemName=itemname, Description=description, ItemType=item_type, Quantity=quantity, ItemUniqueID=uid)
		inventory_obj.save()
		inv = Inventory.objects.all().values_list()
		inv_max = inv.aggregate(Max('ItemID'))
		print(inv_max['ItemID__max'])
		auditInventory = AuditTable_Inventory(AuditAction=2, ItemID=inv_max['ItemID__max'], Quantity=quantity, DateTime=datetime.datetime.now(),  Admin=1)
		auditInventory.save()

		return render(request,'Admin/AdminAddItem.html', {'Check': ['Success']})

	else:
		return render(request, 'Admin/AdminAddItem.html')

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
		labname = request.POST.get('labname', '')
		roomno = request.POST.get('roomno', '')
		capacity = request.POST.get('capacity', '')
		inventory_obj = Ref_Laboratory(LaboratoryName=labname, RoomNum=roomno, Capacity=capacity)
		inventory_obj.save()

		return render(request,'Admin/AdminAddLaboratory.html', {'Check': ['Success']})

	else:

		return render(request, 'Admin/AdminAddLaboratory.html')

def AdminEditLaboratory(request):
	laboratories = Ref_Laboratory.objects.all().values_list()
	
	if request.method == 'POST':
		
		labname = request.POST.get('labname', '')
		roomno = request.POST.get('roomno', '')
		capacity = request.POST.get('capacity', '')
		labid = request.POST.get('labid', '')
		asd = request.POST.getlist('sched[]', '')
		print(asd)
		#inventory_obj = Ref_Laboratory(LaboratoryName=labname, RoomNum=roomno, Capacity=capacity)
		#inventory_obj.save()
		Ref_Laboratory.objects.filter(LabID=labid).update(LaboratoryName=labname,RoomNum=roomno, Capacity=capacity)
		return render(request, 'Admin/AdminEditLaboratory.html', {'Labs': laboratories, 'Check': ['Success']})

	else:
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

def FacultyProfile(request):
    return render(request, 'Faculty/FacultyProfile.html')

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

def FacultyTechProfile(request):
    return render(request, 'FacultyTech/FacultyTechProfile.html')

def FacultyTechInbox(request):
    return render(request, 'FacultyTech/FacultyTechInbox.html')

def FacultyTechBorrowItem(request):
	inventory = Inventory.objects.all().values_list()
	if request.method == 'POST':
		uniqueid = request.POST.get('unique_id', '')
		idborrow = request.POST.getlist('idborrow[]', '')
		qtyborrow = request.POST.getlist('qtyborrow[]', '')
		
		for i in range(0, len(idborrow)):
			auditInventory = AuditTable_Inventory(AuditAction=1, ItemID=idborrow[i], Quantity=qtyborrow[i], DateTime=datetime.datetime.now(), Borrower=uniqueid, Admin=1, BorrowStatus=1)
			auditInventory.save()
			inv = Inventory.objects.all().values_list().filter(ItemID=idborrow[i])
			currentBorrow = int(inv[0][6])
			stringBorrow = str(qtyborrow[i])
			toBorrow = int(stringBorrow)
			totalBorrow = currentBorrow + toBorrow
			finalTotalBorrow = int(totalBorrow)
			Inventory.objects.filter(ItemID=idborrow[i]).update(QtyBorrowed=finalTotalBorrow)
		return render(request, 'FacultyTech/FacultyTechBorrowItem.html', {
			'inventory': inventory
		})
		
	else:
		print(inventory)
		return render(request, 'FacultyTech/FacultyTechBorrowItem.html', {
			'inventory': inventory
		})

def FacultyTechReturnItem(request):
	if request.method == 'POST':
		uid = request.POST.get('uniqueid', '')
		return redirect(reverse("View2", args =[inventory, pastborrow, userinfo]))
	else:
		return render(request, 'FacultyTech/FacultyTechReturnItem.html')

def FacultyTechReturnItem2(request):
	if request.method == 'POST':
		returnitem = request.POST.getlist('itemreturn[]', '')
		for i in range(0, len(returnitem)):
			AuditTable_Inventory.objects.filter(AuditID=returnitem[i]).update(DateTimeReturned=datetime.datetime.now(), BorrowStatus=2)
			auditlatest = AuditTable_Inventory.objects.all().values_list().filter(AuditID=returnitem[i])
			inv = Inventory.objects.all().values_list().filter(ItemID=auditlatest[0][2])
			currentBorrow = int(inv[0][6])
			qtyToSubtract = int(auditlatest[0][3])
			finalQtyBorrowRemaining = currentBorrow - qtyToSubtract
			print (finalQtyBorrowRemaining)
			Inventory.objects.filter(ItemID=auditlatest[0][2]).update(QtyBorrowed=finalQtyBorrowRemaining)
		return render(request, 'FacultyTech/FacultyTechReturnItem2.html')
	else:
		uid = request.GET.get('uniqueid')
		inventory = AuditTable_Inventory.objects.all().filter(Borrower=uid, BorrowStatus=1).values_list()
		pastborrow = AuditTable_Inventory.objects.all().filter(Borrower=uid, BorrowStatus=2).values_list()
		userinfo = User.objects.all().filter(NFCUniqueID=uid).values_list()
		print (inventory)
		print (pastborrow)
		print (userinfo)
		return render(request, 'FacultyTech/FacultyTechReturnItem2.html', {'inventory': inventory, 'pastborrow': pastborrow, 'userinfo': userinfo})

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
