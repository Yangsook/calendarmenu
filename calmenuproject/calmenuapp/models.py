from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Menu(models.Model):
    menu = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    meal_choice = (
        ('아침','아침'),
        ('점심','점심'),
        ('저녁','저녁'),
        ('간식','간식'),
        ('도시락','도시락'),
        ('기타','기타'),
    )
    meal = models.CharField(choices=meal_choice, max_length=100, blank=True)
    
    def __str__(self):
        return self.menu

class Grocery(models.Model):
    item = models.CharField(max_length=200)
    category_choice = (
        ('고기','고기'),
        ('야채','야채'),
        ('생선','생선'),
        ('과일','과일'),
        ('곡류','곡류'),
        ('유제품','유제품'),
        ('냉동식품','냉동식품'),
        ('냉장식품','냉장식품'),
        ('음료','음료'),
        ('소스','소스'),
        ('기타','기타'),
    )
    category = models.CharField(choices=category_choice, max_length=100, blank=True )
    
    def __str__(self):
        return self.item

class MyMenu(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    menu = models.CharField(max_length=200)
    category_choice = (
        ('수프','수프'),
        ('빵','빵'),
        ('면','면'),
        ('밥','밥'),
        ('국','국'),
        ('죽','죽'),
        ('반찬','반찬'),
        ('도시락','도시락'),
        ('고기','고기'),
        ('생선','생선'),
        ('분식','분식'),
        ('전골','전골'),
        ('손님초대','손님초대'),
        ('외식','외식'),
        ('*기타','기타'),
    )
    category = models.CharField(choices=category_choice, max_length=100, blank=True)
    meal_choice = (
        ('아침','아침'),
        ('점심','점심'),
        ('저녁','저녁'),
        ('간식','간식'),
        ('도시락','도시락'),
        ('기타','기타'),
    )
    meal = models.CharField(choices=meal_choice, max_length=100, blank=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.menu

class MyItem(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.CharField(max_length=200)
    category_choice = (
        ('빵','빵'),
        ('고기','고기'),
        ('야채','야채'),
        ('생선','생선'),
        ('과일','과일'),
        ('곡류','곡류'),
        ('유제품','유제품'),
        ('냉동식품','냉동식품'),
        ('냉장식품','냉장식품'),
        ('음료','음료'),
        ('소스','소스'),
        ('기타','기타'),
    )
    category = models.CharField(choices=category_choice, max_length=100, blank=True )

    def __str__(self):
        return  self.item        

class MyMenuItems(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    menuid = models.ForeignKey(MyMenu, on_delete=models.CASCADE)
    itemid = models.ForeignKey(MyItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ' ' + str(self.menuid) + ' ' + str(self.itemid)
     



# class MyCalMenuManager(models.Manager):

    # def get_all_events(self, user):
    #     events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
    #     return events

    # def get_running_events(self, user):
    #     running_events = Event.objects.filter(
    #         user=user,
    #         is_active=True,
    #         is_deleted=False,
    #         end_time__gte=datetime.now().date(),
    #     ).order_by("start_time")
    #     return running_events


class MyCalMenu(models.Model):        
    userid = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    day = models.DateField(auto_now_add=False)
    menuid = models.ForeignKey(MyMenu, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.menuid)

    def get_absolute_url(self):
        url = reverse('mycalmenu_new', args=[self.id])
        ret_val = u'%s' % (str(self.menuid))
        # ret_val = u'<a href="%s">%s</a>' % (url, str(self.menuid))
        
        return ret_val 

    def get_daymenulist(self):
        # print('=====  id ====== ')
        # print(id)
        # print('=====  id ====== ')        
        menus = MyCalMenu.objects.filter(day=self.day)
        return menus


class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sdate = models.DateField(auto_now_add=True) 
    edate = models.DateField(auto_now_add=True)
    memo = models.TextField(blank=True, null=True)  
    day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + ' ' + day



admin.site.register(Menu)
admin.site.register(Grocery)
admin.site.register(MyMenu)
admin.site.register(MyItem)
admin.site.register(MyMenuItems)
admin.site.register(MyCalMenu)
admin.site.register(MyCart)