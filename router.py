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
        #self.routingTable = {}      #key = id, value = router obj

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
            #else: destination is not connected to this router and packet life is over
            else:
                packet.dropPacket()
            
        else:#packet queue is still 1 or greater
            if packet.lifespan > 0:
                packet.lifespan -= 1
                next_router = packet.path.dequeue()
                if next_router in self.network:

                    next_router.addQueue(packet)
                else:#send to switch 
                    self.network[0].send(packet)
            else:
                print('packet lifespan reached 0')
                packet.dropPacket()


    def connectToSwitch(self, object):
        '''
        takes in switch object as arg
        you must run this method manually before adding any router objects.
        automatically connects the switch object with this router instance.
        '''
        #object.network.append(self)
        self.network.append(object)
        object.connectToRouter(self)

        # if type(object) == Switch and type(self) == Switch and len(object.network) == 0:
        #     object.connectToSwitch(self)

        # elif type(object) == Switch:
        #     object.connectToRouter(self)

        

    def connectToRouter(self, object):
        '''
        takes in router or switch object as arg
        you must run connect to switch method manually before adding any router objects.
        '''
        if self not in object.network:
            object.network.append(self)
        
        if object not in self.network:
            self.network.append(object)
        