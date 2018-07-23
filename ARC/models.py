from django.db import models
import datetime

# Create your models here.
class Ref_UserType(models.Model):
	UserTypeID = models.AutoField(primary_key=True)
	UserType = models.CharField(max_length=50, default='')
	
class Ref_UserStatus(models.Model):
	UserStatusID = models.AutoField(primary_key=True)
	UserStatus = models.CharField(max_length=50)
	
class Group(models.Model):
	GroupID = models.AutoField(primary_key=True)
	Adviser = models.CharField(max_length=50, default='')
	Lab = models.IntegerField(default=0)
	
class User(models.Model):
	UserID = models.AutoField(primary_key=True)
	NFCUniqueID = models.IntegerField(default=0)
	UserType = models.IntegerField(default=0)
	UserStatus = models.IntegerField(default=0)
	Name = models.CharField(max_length=50, default='')
	IDNumber = models.IntegerField(default=0)
	PhoneNumber = models.IntegerField()
	Email = models.CharField(max_length=50, default='')
	Group = models.IntegerField(default=0)
	
class Inbox(models.Model):
	InboxID = models.AutoField(primary_key=True)
	Message = models.CharField(max_length=1000, default='')
	DateTime = models.DateTimeField()

class ActualResidency(models.Model):
	ActualResidencyID = models.AutoField(primary_key=True)
	Student = models.IntegerField(default=0)
	DateTime = models.DateTimeField()
	TimeIn = models.TimeField()
	TimeOut = models.TimeField(blank=True, null=True)
	ResidencyStatus = models.IntegerField(blank=True, null=True)

class Ref_Term(models.Model):
	TermID = models.AutoField(primary_key=True)
	Term = models.CharField(max_length=50, default='')
	StartDate = models.DateTimeField(blank=True, null=True) 
	StartDate = models.DateTimeField(blank=True, null=True)

class Ref_Laboratory(models.Model):
	LabID = models.AutoField(primary_key=True)
	LaboratoryName = models.CharField(max_length=50, default='')
	RoomNum = models.CharField(max_length=50, default='')
	Capacity = models.IntegerField(default=0)

class Ref_Schedule(models.Model):
	ScheduleID = models.AutoField(primary_key=True)
	Day = models.CharField(max_length=20, default='')
	Time = models.TimeField()

class ResidencyTimeSlot(models.Model):
	ResidencyID = models.AutoField(primary_key=True)
	Term = models.IntegerField(default=0)
	Laboratory = models.IntegerField(default=0)
	Schedule = models.IntegerField(default=0)

class StudentResidencySchedule(models.Model):
	StudentResSchedID = models.AutoField(primary_key=True)
	Group = models.IntegerField(default=0)

class Ref_AuditAction(models.Model):
	AuditActionID = models.AutoField(primary_key=True)
	Action = models.CharField(max_length=50, default='')

class Inventory(models.Model):
	ItemID = models.AutoField(primary_key=True)
	ItemName = models.CharField(max_length=50, default='')
	Description = models.CharField(max_length=50, default='')
	ItemType = models.CharField(max_length=50, default='')
	Quantity = models.IntegerField(default=0)
	ItemUniqueID = models.IntegerField(default=0)
	QtyBorrowed = models.IntegerField(default=0)

class AuditTable_Inventory(models.Model):
	AuditID = models.AutoField(primary_key=True)
	AuditAction = models.IntegerField(default=0)
	ItemID = models.IntegerField(default=0)
	Quantity = models.IntegerField(blank=True,null=True)
	DateTime = models.DateTimeField()
	DateTimeReturned = models.DateTimeField(blank=True,null=True)
	Borrower = models.IntegerField(blank=True, null=True)
	Admin = models.IntegerField(blank=True, null=True)
	BorrowStatus = models.IntegerField(blank=True, null=True)