from django.http import HttpResponse
from django.shortcuts import render
from .models import Dept, emp  # assuming your model is named Dept
from django.db.models.functions import *
from django.db.models import Q



def dept_view(request):
    if request.method == 'POST':
        try:
            deptno = int(request.POST.get('deptno'))
            dname = request.POST.get('dname')
            loc = request.POST.get('loc')
            
            # Check if department already exists
            exists = Dept.objects.filter(deptno=deptno).exists()
            
            if not exists:
                Dept.objects.create(deptno=deptno, dname=dname, loc=loc)
                return HttpResponse('Department created successfully')
            else:
                return HttpResponse('Department already exists', status=400)
                
        except (ValueError, TypeError):
            return HttpResponse('Invalid input', status=400)
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}', status=500)
    
    # For GET requests, you might want to return a form
    return render(request, 'dept_form.html')  # assuming you have a template






def insert_emp(request):
    deptno=int(input('Enter Deptno: '))
    DO=Dept.objects.filter(deptno=deptno)
    if DO:
        DO=DO[0]
   
        eno=int(input('Enter Employee Id: '))
        ename=input('Enter Employee Name: ')
        job=input('Enter Job: ')
        hiredate=input('Enter Hiredate in the format YYYY-MM-DD: ')
        sal=float(input('Enter Salary: '))

        comm=input('Enter Commission: ')
        if comm:
            comm=float(comm)
        else:
            comm=None
        mgr=input('Enter Manager Id: ')
        MGO=0
        if mgr:
            mgr=int(mgr)
            MGO=emp.objects.filter(eno=mgr)
            if MGO.exists():
                MGO=MGO[0]
            else:
                return HttpResponse('Manager Id not found')
        else:
            MGO=None
        EO= emp.objects.get_or_create(eno=eno, ename=ename, job=job, hiredate=hiredate, sal=sal, comm=comm, mgr=MGO, deptno=DO)
        if EO[1]:
            return HttpResponse('Employee Created Successfully')
        else:
            return HttpResponse('Employee already exists')
    else:
        return HttpResponse('Department not found')
    

def diplay_Dept(reqest):
    T=Dept.objects.all()
    # T=Dept.objects.all()[::]
    # # T=Dept.objects.order_by('loc')
    # # T=Dept.objects.order_by('-loc')
    # # T=Dept.objects.order_by(Length('loc'))
    # # T=Dept.objects.order_by(Length('loc').desc())

    # T=Dept.objects.filter('loc')

    


    c={'T':T}
    return render(reqest,'Dept.html',c)

# to display employee
def diplay_emp(reqest):
    E=emp.objects.all()

#     # E=emp.objects.filter(sal__gt=2000)
#     # E=emp.objects.filter(sal__lt=1000)
#     # E=emp.objects.filter(sal__lte=800)
#     E=emp.objects.filter(sal__gte=5000)

# #WORKING ON  DATE LOOKUP OPERATORS
#     E=emp.objects.filter(hiredate__year=2000)
#     E=emp.objects.filter(hiredate__month=12)
#     E=emp.objects.filter(hiredate__day=15)


# # WORKING ON DATE AND OPERATORS
#     E=emp.objects.filter(hiredate__year__lt=2000)
#     E=emp.objects.filter(hiredate__year__lte=2000)
#     E=emp.objects.filter(hiredate__year__gt=2000)


    Eo={'E':E}
    return render(reqest,'emp.html',Eo)

# to display dept and emp

def joins(request):
    E=emp.objects.select_related('deptno').all()
    # E=emp.objects.select_related('deptno').filter(job='manager')
    # E= emp.objects.select_related('deptno').filter(job='analyst')
    # E= emp.objects.select_related('deptno').filter(job='salesman')
    # E= emp.objects.select_related('deptno').filter(job='clerk')

    # E= emp.objects.select_related('deptno').filter(job='clerk',deptno__dname='sales')
    # E = emp.objects.select_related('deptno').filter(job='manager', sal__gt=2000)
    # E = emp.objects.select_related('deptno').filter(deptno__dname='sales', sal__gt=2000)
    # E = emp.objects.select_related('deptno').filter(deptno__dname__startswith='s')
    # E = emp.objects.select_related('deptno').filter(deptno__dname__startswith='s',ename__endswith='n')
    # E = emp.objects.select_related('deptno').filter(deptno=10,job='clerk')




   
    # E=emp.objects.order_by(Length('job'))
    # E=emp.objects.filter(Ename__contains='n')
    # E=emp.objects.select_related('deptno').all()
    # E=emp.objects.select_related('deptno').filter(deptno=10)
    # E=emp.objects.select_related('deptno').filter(deptno=20)
    # E=emp.objects.select_related('deptno').filter(deptno=30)
    # E=emp.objects.select_related('deptno').filter(deptno=40)
    # E=emp.objects.select_related('deptno').filter(sal__gt=2000)
    # E=emp.objects.select_related('deptno').filter(sal_gt=2000,deptno_Dname='ACCOUNTING')
    # E=emp.objects.select_related('deptno').filter(sal_gte=2000,deptno_Dname='OPERATIONS')
    # E=emp.objects.select_related('deptno').filter(hiredate_year=2025,deptno_Dname='OPERATIONS')
    # E=emp.objects.select_related('deptno').filter(hiredate_month=5,deptno_Dname='OPERATIONS')
    # E=emp.objects.select_related('deptno').filter(hiredate_day=16,deptno_Dname='OPERATIONS')
    # E=emp.objects.select_related('deptno').filter(Ename__startswith='k')
    # E=emp.objects.select_related('deptno').filter(Ename__contains='k')
    # E=emp.objects.select_related('deptno').filter(Ename__endswith='s')



    Eo={'E':E}
    return render(request,'joins.html',Eo)

def selfjoin(request):
    # E =emp.objects.select_related('mgr').all()
    # E =emp.objects.select_related('mgr').filter(job='manager')
    # E =emp.objects.select_related('mgr').filter(job='clerk')
    # E =emp.objects.select_related('mgr').filter(job='analyst')
    # E=emp.objects.select_related('mgr').filter(job='salesman').filter(mgr__sal__gt=2000)


    # E = emp.objects.select_related('mgr').filter(job='manager', mgr__ename__startswith='k',deptno__in=[10,20])
    # E = emp.objects.select_related('mgr').filter(job='manager', mgr__ename__startswith='k',mgr__job='president')
    # E=emp.objects.select_related('mgr').filter(Q(job='salseman')|Q(job='analyst'))
    # E=emp.objects.select_related('mgr').filter(mgr_sal_gt=2000)
    # E=emp.objects.select_related('mgr').filter(comm__isnull=False)
    # E=emp.objects.select_related('mgr').filter(mgr__eno=7839)
    # E=emp.objects.select_related('mgr').filter(mgr_sallt=5000,sal_gt=1500)
    # E=emp.objects.select_related('mgr').filter(mgr_deptno_in=(10,20))
    # E=emp.objects.select_related('mgr').filter(mgr_salgt=2300,sal_gt=2300)

    E=emp.objects.filter(ename='blake').values('sal')

    
    Eo={'E':E}
    return render(request,'selfjoin.html',Eo)

def emd(request):
    E=emp.objects.select_related('deptno','mgr').all()
    E=emp.objects.select_related('deptno','mgr').filter(ename='smith').values('mgr')
     

    Eo={'E':E}
    return render(request,'emd.html',Eo)