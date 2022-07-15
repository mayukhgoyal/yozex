from tabnanny import verbose
from django.db import models

# Create your models here.
class StaticPages(models.Model):
    class Meta:
        verbose_name = "Static page"
        verbose_name_plural = "Static Pages"
    ABOUT_US = "ABOUT US"
    PRIVACY = "PRIVACY"
    TERMS_AND_CONDITIONDS = "TERMS AND CONDITIONS"
    FAQ = "FAQ"
    HELP = "HELP"

    TEMPLATE_TYPE = (
        (ABOUT_US, "About us"),
        (PRIVACY,"Privacy Policy"),
        (TERMS_AND_CONDITIONDS,"Terms & Conditions"),
        (FAQ,"Faq"),
        (HELP,"Help")
    )

    template_name = models.CharField(max_length=50, choices=TEMPLATE_TYPE, unique=True)
    short_description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.template_name)

    