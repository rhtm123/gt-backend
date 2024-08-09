from django.db import models
from imagekit.models import ProcessedImageField # type: ignore
from imagekit.processors import ResizeToFill # type: ignore

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

from coupon.models import Coupon


# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=255)
    # price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
# class Coupon(models.Model):
#     name = models.CharField(max_length=255)
#     discount = models.IntegerField(null=True, blank=True) # percent

#     def __str__(self):
#         return self.name
    


class Technology(models.Model):
    icon = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    img = ProcessedImageField(upload_to='gt/project/', format='JPEG',options={'quality': 60 }, null=True,  blank=True)
    thumbnail = ProcessedImageField(upload_to='gt/project/', processors=[ResizeToFill(1280, 720)], format='JPEG',options={'quality': 60 }, null=True,  blank=True)

    published = models.BooleanField(default=False)
    domain_validity = models.DateField(null=True, blank=True)

    # package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    technology_used = models.ManyToManyField(Technology)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class ProjectPackage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)

    price = models.IntegerField(default=0, help_text="price after discount") # price after discount
    paid = models.IntegerField(default=0)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.project.name + " " + self.package.name

    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         if (self.package and self.coupon):
    #             self.price = self.package.price - self.package.price*self.coupon.discount/100
    #         super(Project, self).save(*args, **kwargs)

class ProjectPackageService(models.Model):
    project_package = models.ForeignKey(ProjectPackage, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    price = models.IntegerField(default=0, help_text="price after discount") # price after discount
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            package = self.project_package
            price = self.service.price 
            discount = self.project_package.coupon.discount
            self.price = price*(100-discount)/100
            package.price = package.price + price*(100-discount)/100
            package.save()
            super(ProjectPackageService, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):

        package = self.project_package
        price = self.service.price
        discount = self.project_package.coupon.discount
        package.price = package.price - price*(100-discount)/100
        package.save()
    
        super().delete(using=using, keep_parents=keep_parents)  # Call the parent class's delete method


PAYMENT_MODE = [
    ('online', 'online'),
    ('offline', 'offline'),
]

class ProjectPackagePayment(models.Model):
    project_package = models.ForeignKey(ProjectPackage, on_delete=models.CASCADE)
    amount = models.IntegerField()

    # mode = models.CharField(max_length=255, choices=PAYMENT_MODE, null=True, blank=True)
    due_date = models.DateField()

    recieve_date = models.DateField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.pk:
            package = self.project_package

            old_payment_receipt = ProjectPackagePayment.objects.get(pk=self.pk)
            amount_difference = self.amount - old_payment_receipt.amount

            # Update the BatchPurchase total_paid with the difference
            package.paid = package.paid + amount_difference

            if old_payment_receipt.is_paid != self.is_paid:
                if (self.is_paid):
                    package.paid = package.paid + self.amount
                else:
                    package.paid = package.paid - self.amount
            package.save()


        if self.pk is None:
            package = self.project_package
            if self.is_paid: 
                package.paid = package.paid + self.amount 
            package.save()

        super(ProjectPackagePayment, self).save(*args, **kwargs)
        
    def delete(self, using=None, keep_parents=False):
        package = self.project_package
        if self.is_paid:
            package.paid = package.paid - self.amount 
        package.save()
    
        super().delete(using=using, keep_parents=keep_parents)  # Call the parent class's delete method
