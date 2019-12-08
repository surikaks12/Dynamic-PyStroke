
from .forms import HomeForm
from .models import UserDatas
import psycopg2
from django.shortcuts import render, redirect
from django.http import HttpResponse
#
# python local setting
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create your views here.

DB_NAME = 'ixvgfxto'
DB_USER = 'ixvgfxto'
DB_PASS = 'Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0'
DB_HOST = 'salt.db.elephantsql.com'
DB_PORT = '5432'
DB_URL = 'postgres://ixvgfxto:Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0@salt.db.elephantsql.com:5432/ixvgfxto'

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print ('Databse connected sucessfully')

except:
    print('Database not connected')

# Local Database connection:
# engine = create_engine("postgres+psycopg2://postgres:password@localhost:5432")
# connection = engine.connect()
# metadata = MetaData()


def index(request):
	return render(request, 'dynamicpystroke/index.html')

def register(request):
	return render(request, 'dynamicpystroke/register.html')

def login(request):
	if request.method == 'POST':
		form = HomeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dynamicpystroke/login.html')
	else:
		form = HomeForm()
		return render(request, 'dynamicpystroke/login.html')
