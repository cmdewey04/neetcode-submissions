class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{","]":"[",")":"("}
        for c in s:
          if c not in closeToOpen:
            stack.append(c)
          else:
            if stack:
              cmp = stack.pop()
            else:
              return False
            if cmp != closeToOpen[c]:
              return False
        
        return True if not stack else False

