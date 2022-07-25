from email import message
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import MyUser, Registeration,Cn_Registeration,Party,Voter

def index(request):
    if request.method=="POST":
        username = request.POST.get("Username")
        password = request.POST.get("password")
        print(f"\n\nusername ==> {username}\npassword ==> {password}\n\n")
        user_data = MyUser.objects.filter(user_name=username,password=password)
        for user in user_data:
            print(user.is_admin)
        try:
            login(request,user_data[0])
            return redirect(ad)
        except:
            messages.info(request, 'Username/Voter ID/DOB may be incorrect, Please Try Again.')
            return render(request,"home.html")       
    return render(request,'home.html')

def join(request):
    if request.method=="POST":
        if request.POST.get("login")=="Login":
            username = request.POST["user_name"]
            vid = request.POST["vid"]
            dob = request.POST["dob"]
            if("/" in dob):
                year = dob.split("/")[-1]
                month = dob.split("/")[-2]
                day = dob.split("/")[-3]
                dob = f"{year}-{month}-{day}"
            user_data = MyUser.objects.filter(user_name=username,VoterID=vid,DOB=dob)
            try:
                login(request,user_data[0])
                return redirect(main)
            except:
                messages.info(request, 'Username/Voter ID/DOB may be incorrect, Please Try Again.')
                return render(request,"join.html")

        if request.POST.get("signup")=="Signup":
            username = request.POST["user_name"]
            email = request.POST["email"]
            address = request.POST["address"]
            phone = request.POST["pno"]
            aadhar = request.POST["aadhar"]
            vid = request.POST["voterid"]
            dob = request.POST["dob"]
            dob = dob.split("/")
            formatted_date = dob[2]+"-"+dob[1]+"-"+dob[0]
            # print(f"\n\n\n\n=======>  {formatted_date}  <===========\n\n\n\n")
            try:
                record = Registeration(Name=username,Email=email,Mobile=phone,Address=address,Aadhar=aadhar,VoterID=vid,DOB=formatted_date) 
                record.save()
                user_record = MyUser(user_name = username, VoterID=vid, DOB=formatted_date)          
                user_record.save()
                return render(request,'join.html')
            except:
                messages.info(request, "Voter ID Already exist.")
    return render(request,'join.html')


@login_required(login_url='/')
def cn(request):
    session = str(request.user)
    if "True" in session:
        if request.method == "POST":
            candidatename = request.POST["cname"]
            Partyfor = request.POST["party"]
            address = request.POST["adress"]
            electoral_constituencies = request.POST["electoral_constituencies"]
            phone = request.POST["phone"]
            gender = request.POST["Gender"]
            choice = request.POST.get("case")
            if(choice.lower()=="yes"):
                doc_file=request.FILES.get("docfile")  
                record = Cn_Registeration(Candidate_Name=candidatename,Party=Partyfor,Address=address,ElectoralConstituencies=electoral_constituencies,Mobile=phone,Gender=gender,doc_file=doc_file) 
                record.save()   
            else:
                record = Cn_Registeration(Candidate_Name=candidatename,Party=Partyfor,Address=address,ElectoralConstituencies=electoral_constituencies,Mobile=phone,Gender=gender) 
                record.save()   
            return render(request,'admin.html')
        return render(request,'cn.html')
    else:
        return render(request,'home.html')

@login_required(login_url='join')
def main(request):
    Cn_record = Cn_Registeration.objects.all()
    record = Party.objects.filter(id=1)
    session = str(request.user)
    vid = session.split(" ")[0]
    if not record:
        record = Party(id=1)
        record.save()

    voted = Voter.objects.all()
    for v in voted:
        if v.VoterID in vid:
            messages.info(request,"You've already voted.")
            return render(request,'join.html')

    if "False" in session:
        if request.method == "POST":
            bjp =int(request.POST.get("BJP",0) and 1)
            # print("########## INC ########\n\n\n",request.POST["INC"],"\n\n\n")
            inc =int(request.POST.get("INC",0) and 1)
            bsp =int(request.POST.get("BSP",0) and 1)
            tmc =int(request.POST.get("TMC",0) and 1)
            ncp =int(request.POST.get("NCP",0) and 1)
            npp =int(request.POST.get("NPP",0) and 1)
            aap =int(request.POST.get("AAP",0) and 1)
            jdu =int(request.POST.get("JDU",0) and 1)
            rjd =int(request.POST.get("RJD",0) and 1)
            sp =int(request.POST.get("SP",0) and 1)
            cpi =int(request.POST.get("CPI",0) and 1)
            cpim =int(request.POST.get("CPIM",0) and 1)
            rld =int(request.POST.get("RLD",0) and 1)
            nota =int(request.POST.get("NOTA",0) and 1)
            Party.objects.filter(id=1).update(BJP=record[0].BJP+bjp, INC=record[0].INC+inc, BSP=record[0].BSP+bsp, TMC=record[0].TMC+tmc, NCP=record[0].NCP+ncp, NPP=record[0].NPP+npp, AAP=record[0].AAP+aap, JDU=record[0].JDU+jdu, RJD=record[0].RJD+rjd, SP=record[0].SP+sp, CPI=record[0].CPI+cpi, CPIM=record[0].CPIM+cpim, RLD=record[0].RLD+rld, NOTA=record[0].NOTA+nota)
            Voter(VoterID=vid).save()
            logout(request)
            return render(request,'home.html',)
    else:
        messages.info(request, 'You are not authorised to vote.')

    return render(request,'main.html',{"view":Cn_record})

def faq(request):
    return render(request,'faq.html')

def about(request):
    return render(request,'about.html')

@login_required(login_url='/')
def ad(request):
    session = str(request.user)
    if "True" in session:
        return render(request,'admin.html')
    return render(request,'home.html')

@login_required(login_url='/')
def list(request):
    session = str(request.user)
    if "True" in session:
        record = Voter.objects.all()
        return render(request,'list.html',{"views":record})
    return render(request,'home.html')


@login_required(login_url='/')
def result(request):
    session = str(request.user)
    if "True" in session:
        Cn_record = Cn_Registeration.objects.all()
        Results = Party.objects.filter(id=1)
        return render(request,'result.html',{"view":Cn_record, "results":Results})
    return render(request,'home.html')


def SignOut(request):
    logout(request)
    return redirect(index)
