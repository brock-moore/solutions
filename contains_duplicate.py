# Return True if the integer list nums contains duplicate entries and False otherwise

def hasDuplicate(nums: List[int]) -> bool:
    # HashMap single loop
    # Time O(n) hash put and get is O(1)
    # Space O(n) create n sized hash map
    map = {}
    for i in nums:
        if map.get(i):
            return True
        map[i] = 1
    return False

def hasDuplicateBruteForce(nums: List[int]) -> bool:
    # Brute Force - nested for loop, 
    # Time O(n^2), Size O(1)
    for i in range (len(nums)):
        for j in range (i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

        
