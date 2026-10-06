class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            word_size = int(s[i:j]) # Take the characters from i to j, convert them into an integer, and store that number in word_size.
            start = j + 1 # skip first #
    
            word = s[start:start + word_size]

            decoded.append(word)

            i = start + word_size
            
        return decoded




