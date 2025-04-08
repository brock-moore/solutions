def isAnagram(s: str, t: str) -> bool:
        # Create char arrays, sort, and compare
        # Time O(nlogn) for sort time where n = len(s + t)
        # Space O(n) for lists where n = len(s + t)
        chars = []
        for c in s:
            chars.append(c)
        chars2 = []
        for c in t:
            chars2.append(c)
        chars.sort()
        chars2.sort()
        return chars == chars2

def isAnagramHash(s: str, t: str) -> bool:
        # Hashmap with char counts
        # Time O(n) loop through strings three times with constant time Dict ops
        # Space O(n) created two dicts of roughly size s and t
        if len(s) != len(t):
            return False
        sDict = {}
        for char in s:
            if sDict.get(char):
                sDict[char] += 1
            else:
                sDict[char] = 1
        tDict = {}
        for char in t:
            if tDict.get(char):
                tDict[char] += 1
            else:
                tDict[char] = 1
        # Loop through set of characters to check equal counts
        for i in s:
            if tDict.get(i) is None or sDict[i] != tDict[i]:
                return False
        return True
