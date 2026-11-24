class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        result = []
        
        for i in tokens:
            if(i == '+'):
                result[-2] += result[-1]
                result.pop()

            elif(i == '-'):
                result[-2] -= result[-1]
                result.pop()
            
            elif(i == '*'):
                result[-2] *= result[-1]
                result.pop()
            
            elif(i == '/'):
                result[-2] = int(result[-2] / result[-1])
                result.pop()
            
            else:
                result.append(int(i))

        return result[-1]
