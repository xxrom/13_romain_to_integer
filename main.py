class Solution:
  def romanCharToInt(self, s, i):
    if s[i] == 'I':
      if i + 1 < len(s):
        if s[i + 1] == 'V':
          return 4, 2
        if s[i + 1] == 'X':
          return 9, 2

      return 1, 1

    if s[i] == 'X':
      if i + 1 < len(s):
        if s[i + 1] == 'L':
          return 40, 2
        if s[i + 1] == 'C':
          return 90, 2

      return 10, 1

    if s[i] == 'C':
      if i + 1 < len(s):
        if s[i + 1] == 'D':
          return 400, 2
        if s[i + 1] == 'M':
          return 900, 2

      return 100, 1

    if s[i] == 'L':
      return 50, 1

    if s[i] == 'D':
      return 500, 1

    if s[i] == 'M':
      return 1000, 1

    if s[i] == 'V':
      return 5, 1

    return 0, 1

  def romanToInt(self, roman: str) -> int:
      ans = 0

      s = roman
      i = 0

      while i < len(s):
        # print(s[i])

        addToAns, inc = self.romanCharToInt(s, i)

        ans += addToAns
        i += inc

      return ans

my = Solution()
n = 'IV'
n = "IX"
n = "XL" # 40
n = "XC" # 90
n = 'XX' # 20
n = "LVIII" # 58
n = "MCMXCIV" # 1994
ans = my.romanToInt(n)
print("ans", ans)
