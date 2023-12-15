class Stack():
    def __init__(self):
        self.items = []
        self.count = 0

    def length(self):
        count = 0
        for i in self.items:
            count += 1
        return count

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def s_push(self, item):
        self.items.append(item)

    def s_pop(self):
        return self.items.pop()

    def s_peek(self):
        max_index = 0
        for index in self.items:
            max_index += 1
        return self.items[max_index - 1]

    def get_stack(self):
        print(self.items)


stack = Stack()

print(stack.length())
print(stack.isEmpty())
stack.s_push(4)
stack.s_push(8)
poped_item = stack.s_pop()
print(poped_item)
print(stack.s_peek())
stack.get_stack()




def validator(code):
    with open(code, 'r') as htmlCode:
        code = htmlCode.readlines()
    current_tag = ''
    counter = 0
    for line in code:
        counter +=1
        for char in line:
            if char == "<":
                current_tag += char
            elif current_tag !=0 :
                current_tag+= char
            if char == ">":
                if "<" in current_tag:
                    current_tag += char
                    #stack.s_push(current_tag)
                    slicer = ""
                    slicer = stack.s_peek()
                    if "/" in current_tag:

                        if str(slicer[1:]) == str(current_tag[2:]):
                            continue
                        else:
                            return "the code is not correct at line" + str(counter)

                    current_tag = ""

                else :
                    return "it has an error on line" + str(counter)
    return "It is a valid html code!"