from django.db import models

# Create your models here.
class Ref_UserType(models.Model):
	UserTypeID = models.IntegerField(primary_key=True)
	UserType = models.CharField(max_length=50, default='')

class Ref_UserStatus(models.Model):
	UserStatusID = models.IntegerField(primary_key=True)
	UserStatus = models.CharField(max_length=50)

class Group(models.Model):
	GroupID = models.IntegerField(primary_key=True)
	Adviser = models.CharField(max_length=50, default='')

class User(models.Model):
	UserID = models.IntegerField(primary_key=True)
	NFCUniqueID = models.IntegerField(default=0)
	UserType = models.IntegerField(default=0)
	UserStatus = models.IntegerField(default=0)
	Name = models.CharField(max_length=50, default='')
	IDNumber = models.IntegerField(default=0)
	PhoneNumber = models.IntegerField()
	Email = models.CharField(max_length=50, default='')
	Group = models.IntegerField(default=0)

class Inbox(models.Model):
	InboxID = models.IntegerField(primary_key=True)
	Message = models.CharField(max_length=1000, default='')
	DateTime = models.DateTimeField()

class ActualResidency(models.Model):
	ActualResidencyID = models.IntegerField(primary_key=True)
	Student = models.IntegerField(default=0)
	DateTime = models.DateTimeField()
	TimeIn = models.TimeField()
	TimeOut = models.TimeField(null=True)

class Ref_Term(models.Model):
	TermID = models.IntegerField(primary_key=True)
	Term = models.CharField(max_length=50, default='')

class Ref_Laboratory(models.Model):
	LabID = models.IntegerField(primary_key=True)
	LaboratoryName = models.CharField(max_length=50, default='')

class Ref_Schedule(models.Model):
	ScheduleID = models.IntegerField(primary_key=True)
	Day = models.CharField(max_length=20, default='')
	Time = models.TimeField()

class ResidencyTimeSlot(models.Model):
	ResidencyID = models.IntegerField(primary_key=True)
	Term = models.IntegerField(default=0)
	Laboratory = models.IntegerField(default=0)
	Schedule = models.IntegerField(default=0)

class StudentResidencySchedule(models.Model):
	StudentResSchedID = models.IntegerField(primary_key=True)
	Group = models.IntegerField(default=0)

class Ref_AuditAction(models.Model):
	AuditActionID = models.IntegerField(primary_key=True)
	Action = models.CharField(max_length=50, default='')

class Inventory(models.Model):
	ItemID = models.IntegerField(primary_key=True)
	ItemName = models.CharField(max_length=50, default='')
	Description = models.CharField(max_length=50, default='')
	Quantity = models.IntegerField(default=0)

class AuditTable_Inventory(models.Model):
	AuditID = models.IntegerField(primary_key=True)
	AuditAction = models.IntegerField(default=0)
	ItemID = models.IntegerField(default=0)
	DateTime = models.DateTimeField()
	DateTimeReturned = models.DateTimeField(null=True)
	Borrower = models.IntegerField(default=0)
	Lender = models.IntegerField(default=0)
