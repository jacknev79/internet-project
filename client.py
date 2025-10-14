from queuell import Queue
class Client():
    def __init__(self, name, ipAddress):
        self.name = name
        self.packets = Queue()
        self._ipAddress = ipAddress

    def __str__(self):
        return '' + self.name

    def readyPacket(self, packet):
        self.packets.enqueue(packet)

    def send(self, address):
        '''
        address is the first router in the queue
        '''
        
        packet = self.packets.dequeue()
        router = packet.next_router() #nb must come back and add enqueueing at router object
        router.addQueue(packet)    #adding to a router the next queue, must add packet

    def receive(self, packet):
        print('Received by: ', self.name)
        print('sent to', packet.address, 'send by:',packet.sender)
        print(packet.content)

    def connectToRouter(self, router):
        '''
        takes in router object as arg
        '''
        lst = [self._ipAddress, self]
        router.clients.append(lst)



    @property
    def ipAddress(self):
        return self._ipAddress
    
    @ipAddress.setter
    def ipAddress(self, new):
        '''
        setter needs new string in ipV4 format
        '''
        self._ipAddress = new