from collections import defaultdict

# class Solution(object):
#     def groupAnagrams(self, strs):

#         group = defaultdict(list)

#         for word in strs:
#             group[''.join(sorted(word))].append(word)

#         return list(group.values())

group = defaultdict(list)
strs = ["eat","tea","tan","ate","nat","bat"]
for word in strs:
  group[''.join(sorted(word))].append(word)

print(list(group.values()))