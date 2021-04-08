
class Solution:

    def solve(self, s):
        stack_ops = []
        stack_nums = []

        def calc(a,b,op):
            if(op == "+"):
                return b+a
            if(op == "-"):
                return b-a
            if(op == "*"):
                return b*a
            if(op == "/"):
                t = b/a
                if(t<0):
                    return ceil(b/a)
                else:
                    return floor(b/a)


        t_s = s
        s = ""
        for i in range(len(t_s)):
            if(t_s[i] == "("):
                s += t_s[i]
                s += " "
                continue
            if(t_s[i] == ")"):
                s += " "
                s += t_s[i]
                continue
            s += t_s[i]
        
        s = s.split(" ")


        for x in s:
            if(x == "(" or x == "+" or x == "-" or x == "*" or x == "/"):
                stack_ops.append(x)
            elif(x == ")"):
                a = int(stack_nums.pop())
                b = int(stack_nums.pop())
                op = stack_ops.pop()
                t = stack_ops.pop()
                if(t != "("):
                    stack_ops.append(t)
                stack_nums.append(calc(a,b,op))
            else:
                stack_nums.append(x)
            
        return stack_nums[-1]
