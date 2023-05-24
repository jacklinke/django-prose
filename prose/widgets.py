from django.forms.widgets import Textarea


class RichTextEditor(Textarea):
    template_name = "prose/forms/widgets/editor.html"

    class Media:
        css = {
            "all": (
                "prose/trix/trix.css",
                "prose/editor.css",
            ),
        }
        js = (
            "prose/trix/trix.umd.js",
            "prose/editor.js",
        )
