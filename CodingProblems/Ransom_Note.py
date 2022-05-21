class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countMagzine = {}
        countRansomNote = {}

        for ch in ransomNote:
            if countRansomNote.get(ch) == None:
                countRansomNote[ch] = 0
            countRansomNote[ch] += 1

        for ch in magazine:
            if countMagzine.get(ch) == None:
                countMagzine[ch] = 0
            countMagzine[ch] += 1

        for key in countRansomNote:
            if countMagzine.get(key) == None or countMagzine[key] < countRansomNote[key]:
                return False

        return True
