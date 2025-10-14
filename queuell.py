from dllStub import DLLNode, DLL


class Queue():
    def __init__(self):
        self.queue = DLL()

    def enqueue(self,item):
        self.queue.add_first(item)

    def dequeue(self):
        return self.queue.remove_last()
    
    def front(self):
        return self.queue.get_first()
    
    def length(self):
        return self.queue.length()