import re
from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        # 다른 풀이 1
        # paragraph = re.split("[!?',;. ]", paragraph.lower())
        # paragraph = [
        #     word for word in paragraph if word is not None and word not in banned
        # ]

        # 다른 풀이 2
        # paragraph = [
        #     word
        #     for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        #     if word not in banned
        # ]

        paragraph = re.sub("[!?',;.]", " ", paragraph)
        paragraph = paragraph.split()
        paragraph = [word.lower() for word in paragraph if word.lower() not in banned]

        word_count = Counter(paragraph)

        return word_count.most_common()[0][0]


sol = Solution()
print(
    sol.mostCommonWord(
        paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
        banned="ball",
    )
)

