# docstrings are used to define, what a function is actually going to do.


def format_name(f_name, l_name):
    """this function takes first and last name as input
    and return it in title format."""
    if f_name == "" or l_name == "":
        return "No Valid Inputs Found!"
    formatted_name = f"{f_name.title()} {l_name.title()}"
    return f"Result : {formatted_name}"


full_name = format_name(f_name=input("First Name : "), l_name=input("Last Name : "))
print(full_name)
