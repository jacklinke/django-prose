from django.db import models
from django.utils.html import strip_tags
from django.utils.translation import gettext as _

from prose.fields import DocumentContentField


class AbstractDocument(models.Model):
    title = models.TextField(verbose_name=_("Title for this Document"), max_length=200, blank=True)
    content = DocumentContentField()

    def get_plain_text_content(self):
        return strip_tags(self.content)

    def __str__(self):
        # If a title is not provided, display a portion of plain text
        if self.title == "":
            plain_text = self.get_plain_text_content()

            if len(plain_text) < 32:
                return plain_text

            return f"{plain_text[:28]}..."
        else:
            return self.title

    class Meta:
        abstract = True


class Document(AbstractDocument):
    pass
