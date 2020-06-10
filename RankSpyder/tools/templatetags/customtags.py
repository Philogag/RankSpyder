from django import template

register = template.Library()

@register.filter(name="split_str")
def split_str(value, arg):
    return value.split(arg)

@register.filter(name="to_delta_time")
def to_delta_time(value):
    def format_s(s):
        if int(s) > 0:
            return "%d:%02d:%02d" % (int(s) // 3600, int(s) // 60 % 60, int(s) % 60)
        else:
            return s
    return [
        format_s(s) for s in value
    ]
