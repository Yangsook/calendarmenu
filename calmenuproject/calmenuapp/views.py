from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import admin
import datetime
import calendar
from django.urls import reverse, reverse_lazy
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from .utils import EventCalendar
from .models import MyCalMenu, MyMenu, MyItem
from .forms import MyCalMenuForm, MyMenuForm, MyItemForm, MyMenuForm1
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User 

# MyItem ==============================================
# class myitem_delete(generic.DeleteView):
#     model = MyItem
#     template_name = "event/myitem_delete.html"
#     success_url = reverse_lazy("myitem_list")   

def myitem_delete(request, pk):
    table = MyItem(pk=pk)
    table.delete()
    return redirect(reverse('myitem_list'))

def myitem_list(request):
    myitemlist = MyItem.objects.all().order_by('item')
    
    if request.method == 'POST':
        form = MyItemForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.userid = 1 #request.user
            form.save()
            return redirect('myitem_list')
    else:
        form = MyItemForm()

    return render(request, 'event/myitem.html', {'form':form, 'myitemlist':myitemlist})
 

# MyMenu ==============================================
class mymenu_delete(generic.DeleteView):
    model = MyMenu
    template_name = "event/mymenu_delete.html"
    success_url = reverse_lazy("mymenu")    

def mymenu_new(request):
    myitemlist = MyItem.objects.all().order_by('category')
    itemdic = {}
    templist = []
    pre_category = ""
    
    for item in myitemlist:
        if item.category != pre_category:
            pre_category = item.category
            templist = []
        
        tempdic = {}
        tempdic[item.item] = item.id
        templist.append(tempdic)
        itemdic[pre_category] = templist
    
    # print('== itemdic === ')
    # print(itemdic)
    # print(myitemlist)

    
    if request.method == 'POST':
        form = MyMenu()
        form.menu = request.POST['menu']
        form.category = request.POST['category']
        form.memo = request.POST['memo']
        form.userid = 1 #request.user
        form.save()

    return render(request, 'event/mymenu_new.html', {'myitemlist':myitemlist})
    # return render(request, 'event/mymenu_edit.html')

def mymenu_edit(request, pk=None):
    # mymenulist = MyMenu.objects.get(pk)
    # print('===== pk ==== ')
    # print(id)
    if request.method == 'POST':
        form = MyMenuForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.userid = 1 #request.user
            form.save()
            return redirect('mymenu_edit', {'pk':pk})
    else:
        form = MyMenuForm()

    return render(request, 'event/mymenu_edit.html')

def mymenu(request):
    mymenulist = MyMenu.objects.all()
    
    if request.method == 'POST':
        form = MyMenuForm1(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.userid = 1 #request.user
            form.save()
            return redirect('mymenu')
    else:
        form = MyMenuForm1()

    return render(request, 'event/mymenu.html', {'form':form, 'mymenulist':mymenulist})
    
def mymenu_list(request):
    mymenulist = MyMenu.objects.all().order_by('category')
    
    if request.method == 'POST':
        form = MyMenuForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.userid = 1 #request.user
            # print('form.userid====')
            # print(form.userid)
            form.save()
            return redirect('mymenu_list')
    else:
        form = MyMenuForm()

    return render(request, 'event/mymenu_list.html', {'form':form, 'mymenulist':mymenulist})



# MyCalMenu ==============================================
class mycalmenu_delete(generic.DeleteView):
    model = MyCalMenu
    template_name = "event/mycalmenu_delete.html"
    success_url = reverse_lazy("home")    
    # success_url = reverse_lazy("mycalmenu_list")    


def mycalmenu_list(request, day=None):
    daymenulist = MyCalMenu.objects.filter(day=day)
    
    if request.method == 'POST':
        form = MyCalMenuForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.userid = 1 #request.userid
            form.save()
            return redirect('home')
    else:
        form = MyCalMenuForm()

    return render(request, 'event/mycalmenu.html', {'form':form, 'day':day, 'daymenulist':daymenulist})
    

def mycalmenu_new(request, id=None):
    # id로 리스트 객체 만들어서 render 하면 됨
    # print('=====  id ====== ')
    # print(id)
    # print('=====  id ====== ')

    if not id:
        daymenulist = {}
    else:
        menu = MyCalMenu.objects.all()
        print(menu)
        
        # daymenulist = menu.get_daymenulist()
        daymenulist = {}
        


    if request.method == 'POST':
        form = MyCalMenuForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'move_mday':form.day})
            # return redirect('home')
    else:
        form = MyCalMenuForm()

    return render(request, 'event/mycalmenu_new.html', {'form':form, 'daymenulist':daymenulist})


# Home  ==============================================
def home(request, extra_context=None):
    move_mday = request.GET.get('move_mday', None)
    extra_context = extra_context or {}

    if not move_mday:
        d = datetime.date.today()
    else:
        try:
            split_move_mday = move_mday.split('-')
            d = datetime.date(year=int(split_move_mday[0]), month=int(split_move_mday[1]), day=1)
        except:
            d = datetime.date.today()

    previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
    previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
    previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                    day=1)  # find first day of previous month

    last_day = calendar.monthrange(d.year, d.month)
    next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
    next_month = next_month + datetime.timedelta(days=1)  # forward a single day
    next_month = datetime.date(year=next_month.year, month=next_month.month, day=1)  # find first day of next month

    extra_context['previous_month'] = reverse('home') + '?move_mday=' + str(previous_month)
    extra_context['next_month'] = reverse('home') + '?move_mday=' + str(next_month)
    
    cal = EventCalendar()
    html_calendar = cal.formatmonth(request, d.year, d.month, withyear=True)
    html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
    extra_context["calendar"] = mark_safe(html_calendar)
    
    print('=======  user =======')
    print(request.user)
    print('=======  user =======')
    return render(request, 'index.html', extra_context)    



# from calendar import HTMLCalendar
# from datetime import datetime as dtime, date, time
# import datetime
# from models import UserCart
 
# class CalendarMenu(HTMLCalendar): 

# class CalendarEvent(HTMLCalendar):
#     def __init__(self, events=None):
#         super(CalendarMenu, self).__init__()
#         # self.events = events
 
#     def formatday(self, day, weekday, events):
#         """
#         Return a day as a table cell.
#         """
#         events_from_day = UserCart.objects.filter(date=day)
#         events_html = "<ul>"
#         for event in events_from_day:
#             events_html += event.get_absolute_url() + "<br>"
#         events_html += "</ul>"
 
#         if day == 0:
#             return '<td class="noday">&nbsp;</td>'  # day outside month
#         else:
#             return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)
 
#     def formatweek(self, theweek, events):
#         """
#         Return a complete week as a table row.
#         """
#         s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
#         return '<tr>%s</tr>' % s
 
#     def formatmonth(self, theyear, themonth, withyear=True):
#         """
#         Return a formatted month as a table.
#         """
 
#         events = Event.objects.filter(day__month=themonth)
 
#         v = []
#         a = v.append
#         a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
#         a('\n')
#         a(self.formatmonthname(theyear, themonth, withyear=withyear))
#         a('\n')
#         a(self.formatweekheader())
#         a('\n')
#         for week in self.monthdays2calendar(theyear, themonth):
#             a(self.formatweek(week, events))
#             a('\n')
#         a('</table>')
#         a('\n')
#         return ''.join(v)

