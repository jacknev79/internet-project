from queuell import Queue
from packet import Packet
class Client():
    def __init__(self, name, ipAddress):
        self.name = name
        self.packets = Queue()
        self._ipAddress = ipAddress
        self.buffer = []

    def __str__(self):
        return '' + self.name

    def readyPacket(self, packet):
        self.packets.enqueue(packet)

    def send(self):
        '''
        sends packet to the first router in queue
        '''
        
        packet = self.packets.dequeue()
        router = packet.next_router() #nb must come back and add enqueueing at router object
        router.addQueue(packet)    #adding to a router the next queue, must add packet

    def receive(self, packet):
        print('Received by: ', self.name)
        print('sent to', packet.address, 'send by:', packet.sender)
        if type(packet) is not Packet:
            raise TypeError()
        self.buffer.append(packet)
        #nb add client/ router ports?
        #each client maintains a separate list which acts as port?
        #if so can use following code:
        # if len(self.buffer) == packet.length:
        #     self.display()
        
        #without ports each client could only receive one message at a time... inefficient
        #port num assign can be done router side or client side... not per packet? 
        #Or can put in packet header...

    def connectToRouter(self, router):
        '''
        takes in router object as arg
        '''
        lst = [self._ipAddress, self]
        router.clients.append(lst)

    def display(self):
        '''
        displays the whole message, in correct order if it was broken into multiple packets
        '''
        self.buffer.sort(key = lambda x: x.order, reverse= False) 
        message = ''
        for packet in self.buffer:
                message += packet.content

        print(message)

    @property
    def ipAddress(self):
        return self._ipAddress
    
    @ipAddress.setter
    def ipAddress(self, new):
        '''
        setter needs new string in ipV4 format
        '''
        self._ipAddress = new