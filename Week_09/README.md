## 算法学习笔记-Week09

# 字符串
https://lemire.me/blog/2017/07/07/are-your-strings-immutable/
In Java, C#, JavaScript, Python and Go, strings are immutable.

## 387. 字符串中的第一个唯一字符
https://leetcode-cn.com/problems/first-unique-character-in-a-string/
1. 暴力
2. map(hashmap, treemap)
找重复
3. hash table

```python
def firstUniqChar(self, s: str) -> int:
    Hash = {}
    for i in s:
        Hash[i] = Hash.get(i, 0) + 1

    for key in Hash.keys():
        if Hash[key] == 1:
            return s.find(key)

    return -1
```
## 8. 字符串转换整数 (atoi)
https://leetcode-cn.com/problems/string-to-integer-atoi/
```python
class Solution:
    def myAtoi(self, s: str) -> int:        
        ls = list(s.strip())
        if len(ls) == 0: return 0
        
        sign = -1 if ls[0] == '-' else 1

        if ls[0] in ['-','+']: del ls[0]

        ret, i = 0, 0

        while i < len(ls) and ls[i].isdigit():
          ret = ret*10 + ord(ls[i]) - ord('0')
          i+=1

        return max(-2**31, min(sign*ret,2**31-1))
```

## 14. 最长公共前缀
https://u.geekbang.org/lesson/32?article=262162
1. 暴力
2. 排列
3. trie
```python
def longestCommonPrefix2(self, strs: List[str]) -> str:
    s = ""
    for i in zip(*strs):
        if len(set(i)) == 1:
            s += i[0]
        else:
            break
    return s
```