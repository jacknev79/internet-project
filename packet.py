from queuell import Queue
class Packet():
    def __init__(self, address, sender, content):
        '''
        address/ sender are strings in the ipV4 address format

        '''
        self._address = address
        self.sender = sender
        self.content = content
        self.length = 1
        self.lifespan = 1

        self._order = 1
        self.path = Queue()
        

    def __str__(self):
        return '' + self._address + self.content 

    def create_path(self, path):
        '''
        path is a list of router objects, ending in the target router.
        packet lifespan grows as more routers are added.
        '''
        for router in path:
            self.lifespan += 5
            self.path.enqueue(router)

    def next_router(self):
        return self.path.dequeue()
    
    
    
    def getAddress(self):
        return self._address 
    
    def getOrder(self):
        return self._order
    
    def setOrder(self, new):
        if type(new) is not int:
            raise TypeError()
        
        self._order = new

    def getLength(self):
        return self._order
    
    def setLength(self, new):
        if type(new) is not int:
            raise TypeError()
        
        self._length = new

    def dropPacket(self):
        print(f'This packet from {self.sender} has been dropped. Content of packet: {self.content}')

    address = property(getAddress)
    order = property(getOrder, setOrder)
    length = property(getLength, setLength)