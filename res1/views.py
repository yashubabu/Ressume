from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from res1.models import *
from django.shortcuts import render_to_response
#from flask import Flask, render_template, redirect, url_for
from django.core.mail import send_mail,BadHeaderError
from pdfs import pdf
import cStringIO
import ho.pisa as pisa
#from generic_mail import Email
from django.template.loader import get_template,render_to_string

from django.template import loader, Context

def home(request):
    return render(request,'home.html',locals())

def registration(request):
    if request.is_ajax() and request.method == "POST":
        global email
	fullname = request.POST.get("fullname")
	email = request.POST.get("emailid")
        #  Implement save function in mongodb
	#import pdb;pdb.set_trace()
	nam = Name.objects.create(Full_name=fullname,Email_id=email)
        print nam
        id = nam.id
        print id
        return render(request,'education.html',{'objects_id':nam.id})
	#nme = Name.Objects.all()
    else:
	raise Http404
    return render(request,'home.html',locals())

   #return render(request,'education.html',{'objects':nam})
def addmore(request):
    if request.is_ajax() and request.method == "POST":
	quafn = request.POST.get("quafn")
	univ = request.POST.get("univ")
	year = request.POST.get("year")
	perc = request.POST.get("perc")
	#  Implement save function in mongodb
        #import pdb;pdb.set_trace()
	edu = Education.objects.create(Qualification=quafn,University=univ,Year_of_Passing=year,Aggrigation=perc)
	# after save implemented
        obj_id = request.POST.get("y1")
        print obj_id
        name_obj = Name.objects.get(id=obj_id)
        print name_obj
        edu.edn = name_obj
        edu.save()
	
	cmp = request.POST.get("cmp",None)
	if cmp == "true":
	    return render(request,'professional.html',{'objects_id':obj_id})
    else:
	raise Http404
    return render(request,'education.html',{'objects_id':obj_id})
    


def profn(request):
    
    if request.is_ajax() and request.method == "POST":
	job = request.POST.get("job",None)
	exp = request.POST.get("exp",None)
	ind = request.POST.get("ind",None)
	func = request.POST.get("func",None)
	key = request.POST.get("key",None)
	#  Implement save function in mongodb
	pro = Profession.objects.create(Job_Type=job, Total_Experience_in_months=exp,Current_Industry=ind,Functional_Area=func,Key_Skills=key)
        obj_id = request.POST.get("y2")
        print obj_id
        try:
            nam = Name.objects.get(id=obj_id)
            print nam
        except Name.DoesNotExist:
            nam = None
        pro.prof = nam
        pro.save()
	cmp = request.POST.get("cmp",None)
	if cmp == "true":
	    return render(request,'home.html',locals())
        else:
	    raise Http404
    return render(request,'professional.html',{'objects_id':obj_id})
def email(request):
    return render(request,'contact.html')

def send(request):
    
    username = ""
    print username
    subject = "Confirmation mail"
    from_email = 'test@creyo.com'
    
    to = ['yashwanthbabu.gujarathi@gmail.com']
    message = render_to_string('/home/naveen/Resume1/res1/templates/c.txt')
    """username = request.POST.get('username', '')
    from_email = request.POST.get('from_email', '')"""
    """message = request.POST.get('message', '')
    print username
    print from_email
    print message
    result = pdf(request)
    file_to_be_sent = pdf(request)
    if username and from_email and message:"""
    try:
        send_mail(subject,message,from_email,['yashwanthbabu.gujarathi@gmail.com'])    
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponse('sent successfully')
    """else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')"""

"""
def mail(request):
    if request.is_ajax() and request.method =="POST":
        Full_name = request.POST.get('fullname', '')
        Mail_id = request.POST.get('emailid', '')
        print Full_name
        print Mail_id
        if Full_name and Mail_id:
            try:
                send_mail(fullname, emailid, ['to@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return HttpResponseRedirect('/home/')
"""
"""
app = Flask(__name__)
mail_ext = Mail(app)
@app.route('/your/url')
def pdfview():
    subject = "Mail with PDF"
    receiver = "receiver@mail.com"
    mail_to_be_sent = Message(subject=subject, recipients=[receiver])
    mail_to_be_sent.body = "This email contains PDF."
    pdf = create_pdf(render_template('your/template.html'))
    mail_to_be_sent.attach("file.pdf", "application/pdf", pdf.getvalue())
    mail_ext.send(mail_to_be_sent)
    return redirect(url_for('other_view'))

"""
"""
def convert(data, home.html.pdf, open=False):
    pdfFile = file(filename, "wb")
    pdf = pisa.CreatePDF(
       cStringIO.StringIO(data.encode("ISO-8859-1")),pdfFile)
    pdfFile.close()
    if not pdf.err:
        pisa.startViewer(filename)
"""
# Create your views here.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from res1.models import *
from django.shortcuts import render_to_response

def home(request):
    if request.method =='POST':
        fname = request.GET.get("fullname")
        eid = request.GET.get("emailid")
    try:
        Name.objects.get(Full_name=fname,Email_id=eid)
  	return render_to_response("error_registration.html",{}, RequestContext(request))
    except:
	Name.objects.create(Full_name=fname,Email_id=eid)
    return render(request,'page1.html')
def edn(request):
    if request.method=='POST':
        qualfn = request.POST.get("quafn")
        univ = request.POST.get("univ")
        year = request.POST.get("year")
        perc = request.POST.get("perc")
        edn = Education.objects.create(Qualification=qualfn,University=univ,Year_of_Passing=year,Aggrigation=perc)
    return render_to_response('page2.html')
def profn(request):
    job = request.POST.get("job")
    exp = request.POST.get("exp")
    ind = request.POST.get("ind")
    fun = request.POST.get("fun")
    key = request.POST.get("key")
    Profession.objects.create(Job_Type=job,Total_Experience_in_months=exp,Current_Industry=ind,Functional_Area=fun, Key_Skills=key)
   return render(request, 'page3.html')

from django.shortcuts import render
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from res1.models import Name,Education,Profession

def page1(request):
    fullname=request.GET.get("fullname")
    emailid=request.GET.get("emailid")
    d=Name()
    d.Full_name=fullname
    d.Email_id=emailid
    d.save()
    d=Name.objects.all()
    return render(request, 'page1.html')

def page2(request):
    qualification = request.POST.get("quafn")
    university = request.POST.get("univ")
    year = request.POST.get("year")
    aggrigation = request.POST.get("perc")
    try:
	Education.objects.get(Qualification=qualification,University=university,Year_of_Passing=year,Aggrigation=aggrigation)
	return render_to_response("error_registration.html",{}, RequestContext(request))
    except:
	Education.objects.create(Qualification=qualification,University=university,Year_of_Passing=year,Aggrigation=aggrigation)
	return render_to_response('page2.html')

def page3(request):
    jobtype = request.POST.get("job")
    experience = request.POST.get("exp")
    industry = request.POST.get("ind")
    functarea = request.POST.get("func")
    keyskills = request.POST.get("key")
    try:
	Qualification.objects.get(Job_Type=jobtype,Total_Experience_in_months=experience,Current_Industry=industry,Functional_Area=functarea,Key_Skills=keyskills)
	return render_to_response("error_registration.html",{}, RequestContext(request))
    except:
	Qualification.objects.create(Qualification=qualification,University=university,Year_of_Passing=year,Aggrigation=aggrigation)
	return render_to_response('page3.html', {"tag":True}, RequestContext(request))


	fullname=request.GET.get("fullname")
	emailid=request.GET.get("emailid")
	
	d=Data()
    	d.fullname=fullname
	d.emailid=emailid
   
	d.save()
	return HttpResponseRedirect('/edn')
	d=Data.objects.all()
       return render_to_response(request, 'page1.html')

    if request.method == "POST":
	fullname = request.POST.get("fullname")
	emailid = request.POST.get("emailid")
	Data.objects.create(fullname=fullname,emailid=emailid)
    	return render_to_response("page1.html",{}, RequestContext(request))
    else:
	return render_to_response("page2.html",{},RequestContext(request))
def page2(request):
	return render(request, 'page2.html')
def page3(request):
	return render(request, 'page3.html')

"""
