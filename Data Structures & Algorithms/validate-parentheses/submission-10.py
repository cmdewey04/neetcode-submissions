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
              if cmp != closeToOpen[c]:
                return False
            else:
              return False
            
        
        return True if not stack else False

