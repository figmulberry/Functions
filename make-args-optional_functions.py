# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
#
# developer = get_formatted_name('fig', '-', 'mulberry')
# print(developer)

"""**************************************************************"""
# Middle names aren't always needed
# Make a middle name optional
"""
The name is build in three possible parts, (first, middle, last) names.
Python matches up the positional arguments correctly.
"""
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

developer = get_formatted_name('fig', 'mulberry')
print(developer)

developer = get_formatted_name('fig', '-', 'mulberry')
print(developer)
