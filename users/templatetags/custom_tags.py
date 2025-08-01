from django import template

register = template.Library()


@register.filter
def in_groups(user, groups):
    if not user.is_authenticated:
        return False
    group_names = []
    for g in groups.split(","):
        group_names.append(g.strip())
    return user.groups.filter(name__in=group_names).exists()
