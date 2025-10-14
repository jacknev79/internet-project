from router import Router
class Switch(Router):
    def __init__(self, macAddress):
        '''
        macAddress is a string in mac Address format
        destination is an instance of a switch object
        switches is an array of all switch objects
        network is an array where network[0] is the switch this switch connects to, other elements are router objects
        you must run connect to switch method manually before adding any router objects.
        '''
        super().__init__()
        self._macAddress = macAddress
        #self._destination = destination
        self.switches = []

    #nb switches talk to switches and finally send to router
    #router then sends to appropriate client, have multiple clients contact 1 router
    #1 router will contact NEAREST switch
    #nb must add mac address/ ip address functionality to packet class
    @property
    def macAddress(self):
        return self._macAddress
    
    @macAddress.setter
    def macAddress(self, new):
        '''
        setter needs new string in mac address format, using colons as separator
        '''
        self._macAddress = new
    @property
    def destination(self):
        return self.network[0]
    #needs recieve a packet from router and send to next switch
    #needs to recieve packet from switch and then send to correspoding router

    def receive(self, packet):
        next_router = packet.path.dequeue()
        if next_router in self.network:
            next_router.addQueue(packet)
        else:
            print('router not in network')
            packet.dropPacket()


    def send(self, packet):
        self.network[0].receive(packet)