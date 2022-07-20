def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)

	lps = [0]*M
	j = 0 
	cnt = 0
	pos = []

	computeLPSArray(pat, M, lps)

	i = 0 
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			cnt += 1
			pos.append(i-j+1)
			j = lps[j-1]	

		elif i < N and pat[j] != txt[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

	print(cnt)
	print(*pos)


def computeLPSArray(pat, M, lps):
	len = 0

	lps[0] = 0
	i = 1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1
	
txt = input()
pat = input()
KMPSearch(pat, txt)


# # Python program for KMP Algorithm
# def KMPSearch(pat, txt):
#     M = len(pat)
#     N = len(txt)
  
#     # create lps[] that will hold the longest prefix suffix 
#     # values for pattern
#     lps = [0]*M
#     j = 0 # index for pat[]
  
#     # Preprocess the pattern (calculate lps[] array)
#     computeLPSArray(pat, M, lps)
  
#     i = 0 # index for txt[]
#     while i < N:
#         if pat[j] == txt[i]:
#             i += 1
#             j += 1
  
#         if j == M:
#             print ("Found pattern at index " + str(i-j))
#             j = lps[j-1]
  
#         # mismatch after j matches
#         elif i < N and pat[j] != txt[i]:
#             # Do not match lps[0..lps[j-1]] characters,
#             # they will match anyway
#             if j != 0:
#                 j = lps[j-1]
#             else:
#                 i += 1
  
# def computeLPSArray(pat, M, lps):
#     len = 0 # length of the previous longest prefix suffix
  
#     lps[0] # lps[0] is always 0
#     i = 1
  
#     # the loop calculates lps[i] for i = 1 to M-1
#     while i < M:
#         if pat[i]== pat[len]:
#             len += 1
#             lps[i] = len
#             i += 1
#         else:
#             # This is tricky. Consider the example.
#             # AAACAAAA and i = 7. The idea is similar 
#             # to search step.
#             if len != 0:
#                 len = lps[len-1]
  
#                 # Also, note that we do not increment i here
#             else:
#                 lps[i] = 0
#                 i += 1
  
# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"
# KMPSearch(pat, txt)
  
# # This code is contributed by Bhavya Jain






# def kmp(parent, pattern):
#     n = len(parent)
#     m = len(pattern)
#     table = [0] * m
#     j = 0
#     for i in range(1, m):
#         while j > 0 and pattern[i] != pattern[j]:
#             j = table[j - 1]
#         if pattern[i] == pattern[j]:
#             j += 1
#             table[i] = j
#     j = 0
#     count = 0
#     loc = []
#     for i in range(n):
#         while j > 0 and parent[i] != pattern[j]:
#             j = table[j - 1]
#         if parent[i] == pattern[j]:
#             if j == (m - 1):
#                 count += 1
#                 loc.append(i - m + 2)
#                 j = table[j]
#             else:
#                 j += 1
#     print(count)
#     print(*loc)

# t = input()
# p = input()
# kmp(t, p)