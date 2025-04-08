def isAnagram(self, s: str, t: str) -> bool:
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
