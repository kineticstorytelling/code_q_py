# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(lst):
    # Find the zeros in the list
    # for number in list if that number is equal to 0 
    # remove the number == 0
    # Move the zeros to the end of the list
    # append (everything is appended to the end of the list)
    # remove/append/ bring that list back
    # return the list
    for number in lst:
        if number == 0:
            lst.remove(number)
            lst.append(number)
    return lst