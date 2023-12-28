from django.contrib import admin
from .models import TicketIpek, ModelService, CustomerService, IntelligenceService, ArchiveService, TicketOnur
# Register your models here.

admin.site.register(TicketIpek)
admin.site.register(ModelService)
admin.site.register(CustomerService)
admin.site.register(IntelligenceService)
admin.site.register(ArchiveService)
admin.site.register(TicketOnur)