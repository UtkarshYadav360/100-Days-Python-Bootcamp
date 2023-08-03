# making a function that returns an output :

# NOTE : title() method turns the string into a title case.


def format_name(f_name, l_name):
    formatted_name = f"{f_name.title()} {l_name.title()}"
    return formatted_name


# calling the function and assigning it to a variable
full_name = format_name("utkArsH", "yaDav")
print(full_name)
