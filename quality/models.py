# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime


class Dimbussinesdev(models.Model):
    idbussinsedev = models.IntegerField(db_column='IdBussinseDev', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimBussinesDev'


class Dimclient(models.Model):
    accnumber = models.IntegerField(db_column='AccNumber', verbose_name='Account number', primary_key=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', verbose_name='Client name', max_length=50)  # Field name made lowercase.
    salesgroup = models.CharField(db_column='SalesGroup', max_length=50)  # Field name made lowercase.
    internationalbg = models.CharField(db_column='InternationalBG', max_length=50)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idterritory = models.ForeignKey('Dimsalesterritory', models.DO_NOTHING, db_column='IdTerritory', null=True)  # Field name made lowercase.
    warrantybuyout = models.CharField(db_column='WarrantyBuyout', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idbussinesdev = models.ForeignKey(Dimbussinesdev, models.DO_NOTHING, db_column='IdBussinesDev')  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimClient'


class Dimdate(models.Model):
    thedate = models.DateField(db_column='TheDate', primary_key=True)  # Field name made lowercase.
    theday = models.IntegerField(db_column='TheDay', blank=True, null=True)  # Field name made lowercase.
    thedayname = models.CharField(db_column='TheDayName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    theweek = models.IntegerField(db_column='TheWeek', blank=True, null=True)  # Field name made lowercase.
    theisoweek = models.IntegerField(db_column='TheISOWeek', blank=True, null=True)  # Field name made lowercase.
    thedayofweek = models.IntegerField(db_column='TheDayOfWeek', blank=True, null=True)  # Field name made lowercase.
    themonth = models.IntegerField(db_column='TheMonth', blank=True, null=True)  # Field name made lowercase.
    themonthname = models.CharField(db_column='TheMonthName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    thequarter = models.IntegerField(db_column='TheQuarter', blank=True, null=True)  # Field name made lowercase.
    theyear = models.IntegerField(db_column='TheYear', blank=True, null=True)  # Field name made lowercase.
    thefirstofmonth = models.DateField(db_column='TheFirstOfMonth', blank=True, null=True)  # Field name made lowercase.
    thelastofyear = models.DateField(db_column='TheLastOfYear', blank=True, null=True)  # Field name made lowercase.
    thedayofyear = models.IntegerField(db_column='TheDayOfYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimDate'

    def __date__(self):
        return self.thedate



class Dimproduct(models.Model):
    partnumber = models.CharField(db_column='PartNumber', verbose_name='Part number', primary_key=True, max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idsupplier = models.ForeignKey('Dimsupplier', models.DO_NOTHING, db_column='IdSupplier', blank=True, null=True)  # Field name made lowercase.
    idproductfamilly = models.ForeignKey('Dimproductfamilly', models.DO_NOTHING, db_column='IdProductFamilly', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimProduct'

    def __int__(self):
        return self.idproductfamilly


class Dimproductfamilly(models.Model):
    idproductfamilly = models.AutoField(db_column='IdProductFamilly', primary_key=True)  # Field name made lowercase.
    familly = models.CharField(db_column='Familly', max_length=50)  # Field name made lowercase.
    superfamilly = models.CharField(db_column='SuperFamilly', max_length=50)  # Field name made lowercase.
    hiperfamilly = models.CharField(db_column='HiperFamilly', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimProductFamilly'

    def __str__(self):
        return self.superfamilly + '  -------  ' + self.familly


class Dimsalesterritory(models.Model):
    idterritory = models.AutoField(db_column='IdTerritory', primary_key=True)  # Field name made lowercase.
    salescountry = models.CharField(db_column='SalesCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reportingregionl2 = models.CharField(db_column='ReportingRegionL2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reportingregion = models.CharField(db_column='ReportingRegion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimSalesTerritory'


class Dimsupplier(models.Model):
    idsupplier = models.IntegerField(db_column='IdSupplier', primary_key=True)  # Field name made lowercase.
    supplier = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DimSupplier'


class Dimtechnican(models.Model):
    idtechnican = models.IntegerField(db_column='IdTechnican', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimTechnican'

    def __str__(self):
        return self.name


class Dimtestprocedure(models.Model):
    idtestprocedure = models.IntegerField(db_column='IdTestProcedure', primary_key=True)  # Field name made lowercase.
    date = models.ForeignKey(Dimdate, models.DO_NOTHING, db_column='Date', blank=True, null=True)  # Field name made lowercase.
    idtechnican = models.ForeignKey(Dimtechnican, models.DO_NOTHING, db_column='IdTechnican', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    doc = models.BinaryField(db_column='Doc', blank=True, null=True)  # Field name made lowercase.
    idproductfamilly = models.ForeignKey(Dimproductfamilly, models.DO_NOTHING, db_column='IdProductFamilly', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DimTestProcedure'




class Factclaim(models.Model):
    idclaim = models.IntegerField(db_column='IdClaim', verbose_name='Claim ID', primary_key=True)  # Field name made lowercase.
    claimnumber = models.CharField(db_column='ClaimNumber', verbose_name='Claim number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refinvoice = models.IntegerField(db_column='RefInvoice')  # Field name made lowercase.
    accnumber = models.ForeignKey(Dimclient, models.DO_NOTHING, db_column='AccNumber')  # Field name made lowercase.
    partnumber = models.ForeignKey(Dimproduct, models.DO_NOTHING, db_column='PartNumber')  # Field name made lowercase.
    dateregistered = models.ForeignKey(Dimdate, models.DO_NOTHING, related_name='registration', db_column='DateRegistered', verbose_name='Date registered', blank=True, null=True)  # Field name made lowercase.
    dateinstalled = models.ForeignKey(Dimdate, models.DO_NOTHING, related_name='instalation', db_column='DateInstalled', blank=True, null=True)  # Field name made lowercase.
    dateremoved = models.ForeignKey(Dimdate, models.DO_NOTHING, related_name='deinstalation', db_column='DateRemoved', blank=True, null=True)  # Field name made lowercase.
    milage = models.FloatField(db_column='Milage', blank=True, null=True)  # Field name made lowercase.
    aplication = models.CharField(db_column='Aplication', max_length=500, blank=True, null=True)  # Field name made lowercase.
    claimreason = models.TextField(db_column='ClaimReason', verbose_name = 'Claim reason', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    rejected = models.BooleanField(db_column='Rejected')  # Field name made lowercase.
    additionalcostvalue = models.DecimalField(db_column='AdditionalCostValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    additionacostcurr = models.CharField(db_column='AdditionaCostCurr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idfactclaimcase = models.ForeignKey('Factclaimcases', models.DO_NOTHING, db_column='IdFactClaimCase', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'FactClaim'

    def __str__(self):
        return self.idclaim


class Factclaimcases(models.Model):
    idfactclaimcase = models.IntegerField(db_column='IdFactClaimCase', primary_key=True)  # Field name made lowercase.
    idtechnican = models.ForeignKey(Dimtechnican, models.DO_NOTHING, db_column='IdTechnican')  # Field name made lowercase.
    thedate = models.ForeignKey(Dimdate, models.DO_NOTHING, db_column='TheDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    manufacturedef = models.BooleanField(db_column='ManufactureDef', blank=True, null=True, default=False)  # Field name made lowercase. This field type is a guess.
    doc = models.BinaryField(db_column='Doc', editable = True, blank=True, null=True)  # Field name made lowercase.
    correctiveactiondoc = models.BinaryField(db_column='CorrectiveActionDoc', editable = True, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'FactClaimCases'

    def __str__(self):
        return self.name


class Factsales(models.Model):
    idsale = models.AutoField(db_column='IdSale', primary_key=True)  # Field name made lowercase.
    accnumber = models.ForeignKey(Dimclient, models.DO_NOTHING, db_column='AccNumber')  # Field name made lowercase.
    invoice = models.IntegerField(db_column='Invoice')  # Field name made lowercase.
    partnumber = models.ForeignKey(Dimproduct, models.DO_NOTHING, db_column='PartNumber')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=19, decimal_places=4)  # Field name made lowercase.
    thedate = models.ForeignKey(Dimdate, models.DO_NOTHING, db_column='TheDate')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'FactSales'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Braki(models.Model):
    part_number = models.CharField(db_column='part number', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=50, blank=True, null=True)
    vendor = models.IntegerField(db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    idproceure = models.CharField(max_length=10, blank=True, null=True)
    id_family = models.IntegerField(db_column='id family', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'braki'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Temp(models.Model):
    accnumber = models.IntegerField(db_column='AccNumber', blank=True, null=True)  # Field name made lowercase.
    invoice = models.IntegerField(db_column='Invoice', blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp'


class Tesst(models.Model):
    accnumber = models.IntegerField(db_column='AccNumber', blank=True, null=True)  # Field name made lowercase.
    invoice = models.IntegerField(db_column='Invoice', blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tesst'
