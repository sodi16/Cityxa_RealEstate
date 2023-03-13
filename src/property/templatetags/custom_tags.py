from django import template


register = template.Library()


@register.simple_tag
def custom_range(start, end):
    return [s for s in range(int(start), int(end))]
    # return


@register.filter
def get_fields(obj):
    return dir(obj)


@register.filter
def is_hidden(field):
    return field.is_hidden


@register.simple_tag()
def render_hidden_fields(form):
    hidden_fields = [field for field in form if field.is_hidden]
    if not hidden_fields:
        return ''
    # return ''.join(str(field) for field in hidden_fields)
    return hidden_fields


@register.simple_tag(takes_context=True)
def display_hidden_fields(context):
    to_display_advanced = context['display_advanced_research']
    print(f'Returned from simple tag with to_display_advanced={not to_display_advanced}')
    return not to_display_advanced


@register.simple_tag(takes_context=True)
def temp_func(context):
    flag = context['display_advanced_research']
    # print(f'Returning  temp_func: {not flag}')
    return not flag

