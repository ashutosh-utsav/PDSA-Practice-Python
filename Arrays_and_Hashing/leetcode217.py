#Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.



# This approach uses a hashset to store the elements of the array and after every iteration it is checking if the elemen is there or not.
def containsDuplicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False