import operator


class Sol(obj):
    def calculate(self, s):
        def comp(opnd, oprt):
            right, left = opnd.pop(), opnd.pop()
            opnd.append(ops[oprt.pop()](left, right))

        ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.div}
        pre = {'+':0, '-':0, '*':1, '/':1}
        opnd, oprt, operand = [], [], 0
        for i in xrange(len(s)):
            if s[i].isdigit():
                operand = operand*10 + int(s[i])
                if i == len(s)-1 or not s[i+1].isdigit():
                    opnd.append(operand)
                    operand = 0
            elif s[i] == '(':
                oprt.append(s[i])
            elif s[i] == ')':
                while oprt[-1] != '(':
                    comp(opnd, oprt)
                oprt.pop()
            elif s[i] in pre:
                while oprt and oprt[-1] in pre and \
                      pre[oprt[-1]] >= pre[s[i]]:
                    comp(opnd, oprt)
                oprt.append(s[i])
        while oprt:
            comp(opnd, oprt)
        return opnd[-1]
