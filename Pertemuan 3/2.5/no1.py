#Levenshtein Distance
#souce : https://www.geeksforgeeks.org/introduction-to-levenshtein-distance/

def levenshteinRecursive(str1, str2, m, n):
	# str1 is empty
	if m == 0:
		return n
	# str2 is empty
	if n == 0:
		return m
	if str1[m - 1] == str2[n - 1]:
		return levenshteinRecursive(str1, str2, m - 1, n - 1)
	return 1 + min(
		# Insert	 
		levenshteinRecursive(str1, str2, m, n - 1),
		min(
			# Remove
			levenshteinRecursive(str1, str2, m - 1, n),
		# Replace
			levenshteinRecursive(str1, str2, m - 1, n - 1))
	)

#main
str1 = str(input("string 1 : "))
str2 = str(input("String 2 : "))
distance = levenshteinRecursive(str1,str2, len(str1), len(str2))
print("Levenshtein Distance:", distance)