# Catching Exceptions :

# try :
# something that might cause an exception.

# except:
# do this if there was an exception.

# else:
# do this if there was no exceptions.

# finally:
# do this no matter what happens.

# ----------------------------------------------------------------------------------------------------------------------------------- #
try:
    file = open("file1.txt")
    my_dict = {"key": "value"}
    print(my_dict["name"])
    # print(my_dict["key"])

# this "except part" only works for the FileNotFoundError
except FileNotFoundError:
    file = open("file1.txt", mode="w")
    file.write("Your file is created.")

# this "except part" only works for KeyError and stores the error key as "error_message"
except KeyError as error_message:
    print(f"{error_message} Key does not exist.")

# this "else part" only works when the "try part" is succeeded
else:
    content = file.read()
    print(content)

# this "finally part" works no matter what
finally:
    file.close()
    print("File was closed.")
