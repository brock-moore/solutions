# Return True if the integer list nums contains duplicate entries and False otherwise

def hasDuplicateHash(nums: List[int]) -> bool:
    # HashMap single loop
    # Time O(n) hash put and get is O(1)
    # Space O(n) create n sized hash map
    map = {}
    for i in nums:
        if map.get(i):
            return True
        map[i] = 1
    return False
    
def hasDuplicateSet(self, nums: List[int]) -> bool:
        # Elegant set solution
        # Time O(n) to create set from nums
        # Space O(n) for created set
        nums_set = set(nums)
        return len(nums_set) != len(nums)

def hasDuplicateBruteForce(nums: List[int]) -> bool:
    # Brute Force - nested for loop, 
    # Time O(n^2), Size O(1)
    for i in range (len(nums)):
        for j in range (i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

        
