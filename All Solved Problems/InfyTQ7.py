class UserMainCode(object):
    @classmethod
    def checkBraces(cls, input1):

        input1 = "public static void main(String args[]){ if (true) { System.out.println('hello world'); }"

        a = [i for i in input1 if i in ["{","}"]]
        stack = []

        for i in a :
            if a and i == "}" and stack[-1] == "{" :
                stack.pop()
            else:
                stack.append(i)

        print("error" if stack else "correct")
                
                
                