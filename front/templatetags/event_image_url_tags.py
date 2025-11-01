from django import template

register = template.Library()

@register.filter
def event_image_url(event):
    """
    Returns proper URL for cover image — supports both uploaded and remote images.
    """
    if not event.cover_url:
        # default fallback
        return "https://images.pexels.com/photos/2774556/pexels-photo-2774556.jpeg"

    url = str(event.cover_url)
    if url.startswith("http://") or url.startswith("https://"):
        return url
    try:
        return event.cover_url.url  # normal uploaded file
    except ValueError:
        return url
