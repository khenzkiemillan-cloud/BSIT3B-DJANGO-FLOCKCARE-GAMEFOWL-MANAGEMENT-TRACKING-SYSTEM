from django.db import models


class ChickenClassification(models.Model):
    classification_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'chicken_classifications'
        ordering = ['classification_name']

    def __str__(self):
        return self.classification_name


class Chicken(models.Model):
    chicken_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, blank=True)
    breed = models.CharField(max_length=100)
    classification = models.ForeignKey(
        ChickenClassification,
        related_name='chickens',
        on_delete=models.PROTECT,
    )
    sex = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'chickens'
        ordering = ['chicken_code']

    def __str__(self):
        return f'{self.chicken_code} - {self.name or self.breed}'


class BreedingRecord(models.Model):
    sire = models.ForeignKey(
        Chicken,
        related_name='sire_breeding_records',
        on_delete=models.PROTECT,
    )
    dam = models.ForeignKey(
        Chicken,
        related_name='dam_breeding_records',
        on_delete=models.PROTECT,
    )
    breeding_date = models.DateField()
    expected_hatch_date = models.DateField(null=True, blank=True)
    actual_hatch_date = models.DateField(null=True, blank=True)
    eggs_count = models.PositiveIntegerField(default=0)
    hatched_count = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'breeding_records'
        ordering = ['-breeding_date']

    def __str__(self):
        return f'{self.sire} × {self.dam} ({self.breeding_date})'


class Supply(models.Model):
    item_name = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    unit = models.CharField(max_length=30)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    minimum_stock = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    expiry_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'supplies'
        ordering = ['item_name']

    def __str__(self):
        return self.item_name


class HealthRecord(models.Model):
    chicken = models.ForeignKey(
        Chicken,
        related_name='health_records',
        on_delete=models.CASCADE,
    )
    record_date = models.DateField()
    record_type = models.CharField(max_length=50)
    description = models.TextField()
    medicine = models.ForeignKey(
        Supply,
        related_name='health_records',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    dosage = models.CharField(max_length=100, blank=True)
    next_schedule = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'health_records'
        ordering = ['-record_date']

    def __str__(self):
        return f'{self.chicken} - {self.record_type} ({self.record_date})'


class FeedRecord(models.Model):
    feeding_date = models.DateField()
    feed_type = models.CharField(max_length=100)
    quantity_used = models.DecimalField(max_digits=12, decimal_places=3)
    unit = models.CharField(max_length=30)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'feed_records'
        ordering = ['-feeding_date']

    def __str__(self):
        return f'{self.feed_type} ({self.feeding_date})'


class Expense(models.Model):
    expense_date = models.DateField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'expenses'
        ordering = ['-expense_date']

    def __str__(self):
        return f'{self.category}: {self.amount} ({self.expense_date})'
