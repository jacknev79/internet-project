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
print(generateIPAddress())

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

print(generateMacAddress())

#need more than 3 routers, 2 switches, 2 clients, up to 5? packets