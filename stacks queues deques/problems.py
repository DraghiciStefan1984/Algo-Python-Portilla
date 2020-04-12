def balanced_parantheses(s):
    if len(s)%2!=0:
        return False
    opening=set('{[(')
    closing=set(')]}')
    matches=set( [('{','}'), ('[',']'), ('(',')')] )
    stack=[]
    for parenthesis in opening:
        stack.append(parenthesis)
    else:
        if len(stack)==0:
            return False
        last_open=stack.pop()
        if (last_open, parenthesis) not in matches:
            return False
    return len(stack)==0


class QueueWithTwoStacks:
    def __init__(self):
        self.instack=[]
        self.outstack=[]

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()