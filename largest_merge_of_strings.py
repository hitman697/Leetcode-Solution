import collections

class Sol(obj):
    def largestString(self, word1, word2):

        a1 = collections.deque(word1)
        a2 = collections.deque(word2)
        result = []
        while a1 or a2:
            if a1 > a2:
                result.append(a1.pop())
            else:
                result.append(a2.pop())
        return "".join(result)
