class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index
        return max_length
        """
        char_to_idx = {}
        idx_to_char = {}
        start = 0
        end = 0
        saved_length = 0
        for idx, char in enumerate(s):
            if char not in char_to_idx:
                char_to_idx[char] = idx
                idx_to_char[idx] = char
                end = idx
                if len(char_to_idx) > saved_length:
                    saved_length += 1
            else:
                start = char_to_idx[char] + 1
                idx_to_char_key = list(idx_to_char.keys())
                for i in idx_to_char_key:
                    if i >= start:
                        break
                    del char_to_idx[idx_to_char[i]]
                    del idx_to_char[i]
                char_to_idx[char] = idx
                idx_to_char[idx] = char
                end = idx
        return saved_length
        """
