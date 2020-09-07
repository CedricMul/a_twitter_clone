import re

# Might be wise to refactor this, or use another function to check 
# if mentioned user is actually a user
def read_reggie(string_content):
    # Starts with single '@', followed by multiple letters until
    # another character/space (maybe add numbers?)
    rex = r"[@]([a-zA_Z]*)"
    prex = re.compile(rex)
    regged = prex.match(string_content)
    # If it captured a name in the grouping it returns a name string
    if regged:
        return regged.group(1)
    else:
        return False
