#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for i in range(len(lst) - 1): # for [0, 1, 2, 3, 4, 5]
        made_swap = False
        for j in range(len(lst) - 1 - i): # first iteration: for first loop for [0, 1, 2, 3, 4, 5]
                                          # second iteration: for second loop for [0, 1, 2, 3, 4]
            if lst[j] > lst[j + 1]: # if lst[0] > lst[1]
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # lst[0], lst[1] becomes lst[1], lst[0]
                made_swap = True # made_swap is no longer false
        if not made_swap: #if no swaps were made
            return lst # return the lst because it was already sorted
    return lst # either way, at the end return the sorted list


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    merged_list = []
    while len(list1) > 0 or len(list2) > 0:
        if list1 == []:
            merged_list.append(list2.pop(0))
        elif list2 == []:
            merged_list.append(list1.pop(0))
        elif list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
    return merged_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    if len(lst) > 1:
        mid = int(len(lst) / 2)
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        # merge-lecture-snippet-start
        left_index = right_index = new_index = 0

        # Interleave left and right into list

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lst[new_index] = left[left_index]
                left_index += 1
            else:
                lst[new_index] = right[right_index]
                right_index += 1
            new_index += 1
        # merge-lecture-snippet-end

        # If lists were uneven length, add remainder of longer list

        while left_index < len(left):
            lst[new_index] = left[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right):
            lst[new_index] = right[right_index]
            right_index += 1
            new_index += 1
    return lst



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
