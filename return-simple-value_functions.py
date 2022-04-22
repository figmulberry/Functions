"""Returning a simple Value"""
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f'{first_name} {last_name}'
    return full_name.title()

developer = get_formatted_name('fig', 'mulberry')
print(developer)
