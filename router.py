from queuell import Queue
class Router():
    def __init__(self):
        '''
        network is an array of one switch and many routers that are connected to this router object.
        network[0] is the switch connected to this router object.
        clients is an array of hosts connected to this router object.
        you must run connect to switch method manually before adding any router objects.
        '''
        self._packets = Queue()
        self.network = []
        self.clients = []

    def addQueue(self, packet):
        self._packets.enqueue(packet)

    def numPackets(self):
        return self._packets.length()

    def process(self):
        packet = self._packets.dequeue()
        if packet.path.length() == 0:
            for host in self.clients:
                
                if host[0] == packet.address:
                    host[1].receive(packet)
                    return 
            else:#destination is not connected to this router and packet life is over
                packet.dropPacket()
            
        else:#packet life is still 1 or greater
            next_router = packet.path.dequeue()
            if next_router in self.network:

                next_router.addQueue(packet)
            else:#send to switch 
                self.network[0].send(packet)


    def connectToSwitch(self, switch):
        '''
        takes in switch object as arg
        you must run this method manually before adding any router objects.
        '''
        switch.network.append(self)
        self.network.append(switch)

    def connectToRouter(self, router):
        '''
        takes in router object as arg
        you must run connect to switch method manually before adding any router objects.
        '''
        if self not in router.network:
            router.network.append(self)
        
        if router not in self.network:
            self.network.append(router)