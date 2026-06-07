from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display=('user','title','amount','category','date')
    search_field=('title','category','user__username')
    list_fill=('category','user','date')
