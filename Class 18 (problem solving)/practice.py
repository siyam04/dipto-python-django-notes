## FizzBuzz

# def FizzBuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return 'FizzBuzz'
#
#     elif num % 3 == 0:
#         return 'Fizz'
#
#     elif num % 5 == 0:
#         return 'Bzz'
#
#     else:
#         return str(num)
#
#
# n = int(input())
# print(' '.join(FizzBuzz(i) for i in range(1, n + 1)))

###################################################################################

## Check Prime or Not

# def test_prime(n):
#     if (n == 1):
#         return False
#     elif (n == 2):
#         return True;
#     else:
#         for x in range(2, n):
#             if (n % x == 0):
#                 return False
#         return True
#
# print(test_prime(110))

###################################################################################

# Time:  O(n)
# Space: O(k), k is the number of different characters

# Given a string S and a string T, find the minimum window in S which
# will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T,
# return the emtpy string "".
#
# If there are multiple such windows, you are guaranteed that
# there will always be only one unique minimum window in S.


# from cffi.backend_ctypes import xrange
#
#
# class Solution(object):
#
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         current_count = [0 for i in xrange(52)]
#         expected_count = [0 for i in xrange(52)]
#
#         for char in t:
#             expected_count[ord(char) - ord('a')] += 1
#
#         i, count, start, min_width, min_start = 0, 0, 0, float("inf"), 0
#         while i < len(s):
#             current_count[ord(s[i]) - ord('a')] += 1
#             if current_count[ord(s[i]) - ord('a')] <= expected_count[ord(s[i]) - ord('a')]:
#                 count += 1
#
#             if count == len(t):
#                 while expected_count[ord(s[start]) - ord('a')] == 0 or \
#                         current_count[ord(s[start]) - ord('a')] > expected_count[ord(s[start]) - ord('a')]:
#                     current_count[ord(s[start]) - ord('a')] -= 1
#                     start += 1
#
#                 if min_width > i - start + 1:
#                     min_width = i - start + 1
#                     min_start = start
#             i += 1
#
#         if min_width == float("inf"):
#             return ""
#
#         return s[min_start:min_start + min_width]
#
#
# if __name__ == "__main__":
#     print(Solution().minWindow("ADOBECODEBANC", "ABC"))

###################################################################################


