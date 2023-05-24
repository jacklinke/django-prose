from django import forms
from django.db import models
import bleach

from prose import settings
from prose.widgets import RichTextEditor


class RichTextField(models.TextField):
    def formfield(self, **kwargs):
        kwargs["widget"] = RichTextEditor
        return super().formfield(**kwargs)

    def pre_save(self, model_instance, add):
        raw_html = getattr(model_instance, self.attname)
        if not raw_html:
            return raw_html

        sanitized_html = bleach.clean(
            raw_html,
            tags=settings.ALLOWED_TAGS,
            attributes=settings.ALLOWED_ATTRIBUTES,
        )
        return sanitized_html


class DocumentContentField(RichTextField):
    pass
