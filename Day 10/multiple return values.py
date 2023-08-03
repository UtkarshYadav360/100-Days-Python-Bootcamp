# making a function that can return multiple statements :
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No Valid Inputs Found!"
    else:
        formatted_name = f"{f_name.title()} {l_name.title()}"
        return f"Result : {formatted_name}"


full_name = format_name(f_name=input("First Name : "), l_name=input("Last Name : "))
print(full_name)
