from django.contrib import admin
from .models.ReceiveTransaction import ReceiveTransaction

class ReceiveTransactionView(admin.ModelAdmin):
    list_display = ("id","user_account","receiver","receive_value",)
    search_fields = ["receiver", "user_account",]

admin.site.register(ReceiveTransaction,ReceiveTransactionView)
