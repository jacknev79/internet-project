from queuell import Queue
class Packet():
    def __init__(self, address, sender, content):
        '''
        address/ sender are strings in the ipV4 address format

        '''
        self._address = address
        self.sender = sender
        self.content = content
        self.path = Queue()

    def __str__(self):
        return '' + self._address + self.content 

    def create_path(self, path):
        '''
        path is a list of router objects, ending in the target router
        '''
        for router in path:
            self.path.enqueue(router)

    def next_router(self):
        return self.path.dequeue()
    
    
    
    def getAddress(self):
        return self._address 

    def dropPacket(self):
        print(f'This packet from {self.sender} has been dropped. Content of packet: {self.content}')

    address = property(getAddress)
    