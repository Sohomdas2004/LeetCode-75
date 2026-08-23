"""
LeetCode Problem No 345:Reverse Vowels Of A String(https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75)

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=['A','E','I','O','U','a','e','i','o','u']
        s = list(s)

        start=0
        end=len(s)-1

        while(start<end):
            if s[start] not in vowel:
                start+=1
            elif s[end] not in vowel:
                end-=1
            else:
                temp=s[start]
                s[start]=s[end]
                s[end]=temp
                start+=1
                end-=1

        return ''.join(s)