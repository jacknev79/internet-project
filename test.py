from packet import Packet
from client import Client
from router import Router
from switch import Switch
import random as rand
def generateIPAddress():
    parts = []
    for i in range(4):
        part = rand.randrange(255)
        parts.append(str(part))
        parts.append('.')
    ipAddress = ''.join(parts)
    ipAddress = ipAddress.strip('.')

    return ipAddress

def generateMacAddress():
    parts = []
    for i in range(6):
        first = rand.randrange(15)
        second = rand.randrange(15)
        first = hex(first)          #https://www.geeksforgeeks.org/python/python-hex-function/
        second = hex(second)
        first = first.strip('0x')
        second = second.strip('0x')
        if first == '':
            first = '0'
        if second == '':
            second = '0'
        parts.append(first)
        parts.append(second)
        parts.append(':')

    macAddress = ''.join(parts)
    macAddress = macAddress.strip(':')
    return macAddress

def createPackets(sender, destination, message, n):
    '''
    Splits up a given message into one or many packets with max content size n.
    If split into multiple packets they are assigned an order.
    Sender is the client host that is sending the packet(s) to destination.
    Packets are added to sender queue and can be sent using .send method.
    '''
    strings = [message[i:i+n] for i in range(len(0,message, n))]
    order = 1
    for string in strings:
        packet = Packet(sender.ipAddress, destination.ipAddress, string)
        packet.order = order
        packet.length = len(strings)
        sender.readyPacket(packet)

        order += 1
        #nb must add 'create path' functionality.. maybe need routing table?




clientAAddress = generateIPAddress()
clientBAddress = generateIPAddress()
clientA = Client('clientA', clientAAddress)
clientB = Client('clientB', clientBAddress)
switch1MacAddress = generateMacAddress()
switch2MacAddress = generateMacAddress()
switch1 = Switch(switch1MacAddress)
switch2 = Switch(switch2MacAddress)


switch1.connectToSwitch(switch2)
#switch2.connectToSwitch(switch1)

routerA = Router()
routerB = Router()
routerC = Router()
routerD = Router()
routerA.connectToSwitch(switch2)
routerB.connectToSwitch(switch1)
routerC.connectToSwitch(switch2)
routerD.connectToSwitch(switch1)


#nb must add more routers into network (multiple routers should connect to each switch?)


packet1 = Packet(clientBAddress, clientAAddress, 'This is packet 1 from client A to client B')
path = [routerD, routerB, routerD]
packet1.create_path(path)
packet2 = Packet(clientAAddress, clientBAddress, 'This is packet 2 from client B to client A')
path = [routerB, routerA, routerD, routerC]
packet2.create_path(path)
packet3 = Packet(clientBAddress, clientAAddress, 'This is packet 3 from client A to client B')
path = [routerB, routerA, routerC, routerA, routerB]
packet3.create_path(path)

clientA.readyPacket(packet1)
clientA.readyPacket(packet3)
clientB.readyPacket(packet2)
clientA.connectToRouter(routerD)
#clientB.connectToRouter(routerA)
clientB.connectToRouter(routerB)
clientA.connectToRouter(routerB)

clientA.send()
clientA.send()
clientB.send()

while clientA.packets.length() > 0 or clientB.packets.length() > 0 or routerA.numPackets() > 0 or routerB.numPackets() > 0 or routerC.numPackets() > 0 or routerD.numPackets() > 0:
    #print('got here')
    if routerA.numPackets() > 0:

        routerA.process()
    if routerB.numPackets() > 0:

        routerB.process()
    if routerC.numPackets() > 0:

        routerC.process()
    if routerD.numPackets() > 0:

        routerD.process()
    #print('got here now')