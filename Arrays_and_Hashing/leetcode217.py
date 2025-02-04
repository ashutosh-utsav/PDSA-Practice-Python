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

# there is one more approach that is bruet forch in that we will create two loops and check if the element is there or not 

def containsduplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
# but this method has timecomplexity of O(n^2) which is not good so we will use the above method