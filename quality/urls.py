from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^claim_cases$', claim_cases, name='claim_cases'),
    url(r'^case_details$', case_details, name='case_details'),
    url(r'^recent_claims$', recent_claims, name='recent_claims'),
    url(r'^add_case$', send, name='send'),
    url(r'^download$', download, name='download'),
    url(r'^procedures$', procedures, name='procedures'),
    url(r'^add_procedure$', add_procedure, name='add_procedure'),
    url(r'^download_procedure$', download_procedure, name='download_procedure'),
    url(r'^download_corrective$', download_corrective, name='download_corrective'),
    url(r'^add_corrective$', add_corrective, name='add_corrective'),
]
