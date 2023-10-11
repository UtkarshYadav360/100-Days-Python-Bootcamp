# EXERCISE 2 :
# KeyError HANDLING

# DON'T CHANGE THE CODE BELOW :
# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0

# MODIFY THE CODE HERE :
# TODO : CATCH THE KEY ERROR EXCEPTION
for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass

# DON'T CHANGE THE CODE BELOW :
print(total_likes)
