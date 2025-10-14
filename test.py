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


clientAAddress = generateIPAddress()
clientBAddress = generateIPAddress()
clientA = Client('clientA', clientAAddress)
clientB = Client('clientB', clientBAddress)
switch1MacAddress = generateMacAddress()
switch2MacAddress = generateMacAddress()
switch1 = Switch(switch1MacAddress)
switch2 = Switch(switch2MacAddress)
switch1.connectToSwitch(switch2)
switch2.connectToSwitch(switch1)



routerA = Router()
routerB = Router()
routerA.connectToSwitch(switch2)
routerB.connectToSwitch(switch1)
switch1.connectToRouter(routerA)
switch2.connectToRouter(routerB)







#nb must add more routers into network (multiple routers should connect to each switch)


packet1 = Packet(clientBAddress, clientAAddress, 'This is packet 1 from client A to client B')
path = [routerA, routerB, routerA]
packet1.create_path(path)
packet2 = Packet(clientAAddress, clientBAddress, 'This is packet 2 from client B to client A')
path = [routerB, routerA]
packet2.create_path(path)
packet3 = Packet(clientBAddress, clientAAddress, 'This is packet 3 from client A to client B')
path = [routerB, routerA, routerB, routerA, routerB]
packet3.create_path(path)

clientA.readyPacket(packet1)
clientA.readyPacket(packet3)
clientB.readyPacket(packet2)
clientA.connectToRouter(routerA)
clientB.connectToRouter(routerA)
clientB.connectToRouter(routerB)
#clientA.connectToRouter(routerB)

clientA.send(routerA)
clientA.send(routerB)
clientB.send(routerB)
while clientA.packets.length() > 0 or clientB.packets.length() > 0 or routerA.numPackets() > 0 or routerB.numPackets() > 0:
    #print('got here')
    if routerA.numPackets() > 0:

        routerA.process()
    if routerB.numPackets() > 0:

        routerB.process()
    #print('got here now')