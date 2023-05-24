from django.conf import settings


ALLOWED_TAGS = getattr(
    settings,
    "PROSE_ALLOWED_TAGS",
    [
        "p",
        "ul",
        "ol",
        "li",
        "strong",
        "em",
        "div",
        "span",
        "a",
        "blockquote",
        "pre",
        "figure",
        "figcaption",
        "br",
        "code",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "picture",
        "source",
        "img",
        "del",
    ],
)

ALLOWED_ATTRIBUTES = getattr(
    settings,
    "PROSE_ALLOWED_ATTRIBUTES",
    {
        "*": [
            "alt",
            "class",
            "id",
            "src",
            "srcset",
            "href",
            "media",
        ],
    },
)

ALLOWED_ATTACHMENT_FILE_TYPES = getattr(
    settings,
    "PROSE_ALLOWED_ATTACHMENT_FILE_TYPES",
    [
        "image/jpeg",
        "image/png",
        "image/gif",
    ],
)
ALLOWED_ATTACHMENT_FILE_SIZE = getattr(
    settings, "PROSE_ALLOWED_ATTACHMENT_FILE_SIZE", 5
)
