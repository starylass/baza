import django_tables2 as tables
from .models import *
from django_tables2.utils import A, Accessor


class tab_recent_claims(tables.Table):
    check = tables.CheckBoxColumn(accessor='pk')
    dateregistered_thedate = tables.Column(verbose_name = 'Date registered', accessor=Accessor('dateregistered.thedate'))
    dateinstalled_thedate = tables.Column(verbose_name = 'Date installed', accessor=Accessor('dateinstalled.thedate'))
    dateremoved_thedate = tables.Column(verbose_name = 'Date removed', accessor=Accessor('dateremoved.thedate'))
    class Meta:
        model = Factclaim
        template_name = "django_tables2/bootstrap4.html"
        fields = ("check", "accnumber.clientname", "partnumber.partnumber", "dateregistered_thedate", "dateinstalled_thedate", "dateremoved_thedate", "milage", "make", "claimreason" )



class tab_claim_cases(tables.Table):
    class Meta:
        model = Factclaim
        template_name = "django_tables2/bootstrap.html"
        fields = ("accnumber.clientname", "partnumber.partnumber", "dateregistered.thedate", "dateinstalled.thedate", "dateremoved.thedate", "milage", "make", "claimreason" )
