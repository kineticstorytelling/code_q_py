# Question1 Remove First and Last Character
# You are given a string containing a sequence of character sequences separated by commas.

# Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.

# If the input string is empty or the removal of the first and last items would cause the resulting string to be empty, return an empty value (represented as a generic value NULL in the examples below).



def array(string):
    #start off with a empty string
    #first put it in a list
    #pop to remove the end item
    #loop through each item and start from the 2nd item
    #slice to remove commas and replace with a space
    #concat into the empty string
    
    #I didn't know you could just remove the lists items using position and that's it
    
    num = string.split(',')
    num = num[1: -1]
    if len(num) == 0:
        return None
    return ' '.join(num)