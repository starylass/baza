from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import datetime
import pandas as pd
from .tables import *
from django_tables2 import SingleTableView
from .forms import *
from django.core.files import File
import pyodbc
import os
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io


def index(request):
    return render(request, 'index.html')



def claim_cases(request):
    items = Factclaim.objects.exclude(idfactclaimcase__isnull=True)
    context = {
        'items': items,
    }
    return render(request, 'claim_cases.html', {'items': items})



def case_details(request):
    filter = request.GET.get('idfactclaimcase', False)
    items = Factclaim.objects.filter(idfactclaimcase=filter)
    table = tab_recent_claims(items)
    return render(request, 'fact_claim.html', {'table': table})



def recent_claims(request):
    month_before = datetime.datetime.now() - pd.DateOffset(months=10)
    items = Factclaim.objects.filter(dateregistered__gte = month_before)
    table = tab_recent_claims(items)
    return render(request, 'recent_claims.html', {'table': table})



def send(request):
    pks=request.GET.getlist('check')
    selected_objects = Factclaim.objects.filter(pk__in=pks)


    df = pd.DataFrame(Factclaimcases.objects.all().values())
    if df.empty == True:
        pk_set = 1
    else:
        pk = df['idfactclaimcase'].max()
        pk_set = pk + 1

    table = tab_claim_cases(selected_objects)

    if request.method == "POST":
        form = Factclaimcases_input(request.POST, request.FILES)
        if form.is_valid():
            up_doc = request.FILES["doc"].read()
            form.save()
            Factclaimcases.objects.filter(idfactclaimcase = pk_set).update(doc=up_doc)
            selected_objects.update(idfactclaimcase = pk_set)
            return redirect('claim_cases')

    else:
        form = Factclaimcases_input()
        form.initial['idfactclaimcase'] = pk_set
        form.initial['thedate'] = date.today()
        return render(request, 'add_case.html', {'table': table, 'form': form, 'pks': pks, 'pk_set': pk_set})



def download(request):
    connection = pyodbc.connect('Driver=SQL Server Native Client 11.0;'
                            'Server=DL9QKVPF2\DEL;'
                            'Database=Test;'
                            'Trusted_Connection=yes;'
                            )

    cursor = connection.cursor()

    param = request.GET.get('idfactclaimcase', False)
    sql = """exec get_doc @IdFactClaimCase = ?"""
    retrieved_bytes = cursor.execute(sql, param).fetchval()

    buffer = io.BytesIO(retrieved_bytes)
    p = canvas.Canvas(buffer)
    p.showPage()
    p.save()
    buffer.seek(io.SEEK_SET)
    file_name = str(date.today()) + param + '.pdf'
    return FileResponse(buffer, filename=file_name)



def procedures(request):
    items = Dimtestprocedure.objects.all()
    context = {
            'items': items,
        }
    return render(request, 'procedures.html', {'items': items})



def add_procedure(request):

    df = pd.DataFrame(Dimtestprocedure.objects.all().values())
    if df.empty == True:
        pk_set = 1
    else:
        pk = df['idtestprocedure'].max()
        pk_set = pk + 1

    if request.method == "POST":
        form = Dimtestprocedure_input(request.POST, request.FILES)
        if form.is_valid():
            up_doc = request.FILES["doc"].read()
            form.save()
            Dimtestprocedure.objects.filter(idtestprocedure = pk_set).update(doc=up_doc)
            return redirect('procedures')
    else:
        form = Dimtestprocedure_input()
        form.initial['date'] = date.today()
        form.initial['idtestprocedure'] = pk_set
        return render(request, 'add_procedure.html', {'form': form})



def download_procedure(request):
    connection = pyodbc.connect('Driver=SQL Server Native Client 11.0;'
                            'Server=DL9QKVPF2\DEL;'
                            'Database=Test;'
                            'Trusted_Connection=yes;'
                            )

    cursor = connection.cursor()

    param = request.GET.get('idtestprocedure', False)
    sql = """exec get_procedure @IdTestProcedure = ?"""
    retrieved_bytes = cursor.execute(sql, param).fetchval()

    buffer = io.BytesIO(retrieved_bytes)
    p = canvas.Canvas(buffer)
    p.showPage()
    p.save()
    buffer.seek(io.SEEK_SET)
    file_name = str(date.today()) + param + '.pdf'
    return FileResponse(buffer, filename=file_name)



def download_corrective(request):
    connection = pyodbc.connect('Driver=SQL Server Native Client 11.0;'
                            'Server=DL9QKVPF2\DEL;'
                            'Database=Test;'
                            'Trusted_Connection=yes;'
                            )

    cursor = connection.cursor()

    param = request.GET.get('idfactclaimcase', False)
    sql = """exec get_corrective @IdFactClaimCase = ?"""
    retrieved_bytes = cursor.execute(sql, param).fetchval()

    buffer = io.BytesIO(retrieved_bytes)
    p = canvas.Canvas(buffer)
    p.showPage()
    p.save()
    buffer.seek(io.SEEK_SET)
    file_name = str(date.today()) + param + '.pdf'
    return FileResponse(buffer, filename=file_name)


def add_corrective(request):
    filter = request.GET.get('idfactclaimcase', False)
    if request.method == "POST":
        form = Corrective_input(request.POST, request.FILES)
        if form.is_valid():
            up_doc = request.FILES["correctiveactiondoc"].read()
            Factclaimcases.objects.filter(idfactclaimcase = filter).update(correctiveactiondoc=up_doc)
            print(up_doc)
            return redirect('claim_cases')
    else:
        form = Corrective_input()
        form.initial['idfactclaimcase'] = filter
        return render(request, 'add_corrective.html', {'form': form})
