

def twoSum(nums, target):

    hash_map = dict() # create hash map/dictionary

    for x in range(len(nums)): # loop through nums array
        if nums[x] not in hash_map: # if value not in hash_map
            
            hash_map[target-nums[x]] = x #subtract value from target and add to dict under index

        else: # if it is, return dict index and current index
            
            return [hash_map[nums[x]], x] # return index and index key 
         
