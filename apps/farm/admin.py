from django.contrib import admin

from .models import (
    BreedingRecord,
    Chicken,
    ChickenClassification,
    Expense,
    FeedRecord,
    HealthRecord,
    Supply,
)


admin.site.register(ChickenClassification)
admin.site.register(Chicken)
admin.site.register(BreedingRecord)
admin.site.register(HealthRecord)
admin.site.register(Supply)
admin.site.register(FeedRecord)
admin.site.register(Expense)
