### 50 Problems Version:
1. Two Sum
   loop the indice, not the value, use len(nums) to represent the indice.
   Hashmap can reduce the time complexity from O(n^2) to O(n)

2. Valid Parentheses
   create a dictionary to store the relationship. create a stack to implement. If i is an open bracket, push it; If i isn't an open bracket, check whether last item in stack matches.

3. Merge Two Sorted Lists
   Create a new empty node. Compare two lists and choose the smaller one to the list when none of the two lists is empty; Add to cur when one list is not empty.

4. Best Time to Buy and Sell Stock
   Update variable to avoid runtime exceed.

5. Vaild Palindrome
   alphanumeric_s = ''.join([char.lower() for char in s if char.isalnum()])

6. Invert Binary Tree
   Use invertTree function for leftTree and rightTree and exchange.

7. Valid Anagram
   sorted() to sort string and compare.

8. Binary Search
   Use a while loop and left, right, mid variable to dinf the match.
