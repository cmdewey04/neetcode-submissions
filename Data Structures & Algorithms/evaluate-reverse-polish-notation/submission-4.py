import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #add each number onto a stack
        #add result back onto stack?
        #whenever come across operator, pop 2
        #["1","2","+","3","*","4","-"]

        # stack = []
        # operators = {"*", "+", "-", "/"}

        # ops = {
        #     "*": operator.mul,
        #     "+": operator.add,
        #     "-": operator.sub,
        #     "/": operator.truediv,
        # }
        
        # for token in tokens:
        #     if token in operators:
        #         #pop 2
        #         right = stack.pop()
        #         left = stack.pop()
        #         stack.append(int(ops[token](left, right)))
        #     else:
        #         stack.append(int(token))

        # return stack.pop()


        stack = []
        opers = {'+', '*', '-', '/'}

        ops = {
          '+': operator.add,
          '-': operator.sub,
          '*': operator.mul,
          '/': operator.truediv,
        }

        for t in tokens:
          if t in opers:
            right,left = stack.pop(), stack.pop()
            stack.append(int(ops[t](left,right)))
          else:
            stack.append(int(t))
        return stack[-1]
