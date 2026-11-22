class Solution:
    def isValid(self, s: str) -> bool:
        valid_list = []

        for val in s:
            if(val == '(' or val == '{' or val == '['):
                valid_list.append(val)

            elif(val == ')'):
                if(len(valid_list) == 0):
                    valid_list.append(val)
                    continue

                if(valid_list[-1] == '('):
                    valid_list.pop()

                else:
                    valid_list.append(val)

            elif(val == '}'):
                if(len(valid_list) == 0):
                    valid_list.append(val)
                    continue

                if(valid_list[-1] == '{'):
                    valid_list.pop()

                else:
                    valid_list.append(val)

            elif(val == ']'):
                if(len(valid_list) == 0):
                    valid_list.append(val)
                    continue
                    
                if(valid_list[-1] == '['):
                    valid_list.pop()

                else:
                    valid_list.append(val)

        if not valid_list:
            return True

        else:
            return False
