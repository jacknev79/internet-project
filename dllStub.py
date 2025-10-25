""" Classes to implement a doubly linked list.


For CS2515 labs on DoublyLinked Lists
Comments provided with permission by Prof. Ken Brown

Stub file - specifies method signatures, but the method bodies need to be completed.

"""


class DLLNode:
    """ An internal node in a doubly linked list.    

    Attributes:
        # these should really be private ...
        element: the object in this position in the list
        next: the next DLLNode instance in the list
        prev: the previous DLLNode instance in the list
    """

    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode


class DLL:
    """ A doubly linked list.

    Attributes:
        # these should really be private ...
        head: an empty DLLNode to start the list
        tail: an empty DLLNode to end the list
        size: the integer number of items in the list
    """

    def __init__(self):
        """ Initialise an empty library. """
        self.dummy_head = DLLNode(None, None, None)
        self.dummy_tail = DLLNode(None, self.dummy_head, None)
        #empty = DLLNode(None, self.dummy_head, self.dummy_tail)
        self.dummy_head.next = self.dummy_tail
        
    
        self.size = 0
    def __str__(self):
        """ Return a string representation of the list. """
        string = ''
        next_item = self.dummy_head.next
        for i in range(self.size):
        
            if  next_item.element is None:
                break
            string += str(next_item.element)
            string += '-'
            next_item = next_item.next
        if string == '':
            return 'Empty'
        return string

#---------- Public Methods ------------------------------#
           
    def add_first(self, item):
        """ Add item to the start of the list.

        Args:
            item: an object instance to be added
        """

        newNode = DLLNode(item, self.dummy_head, self.dummy_head.next)
        self.dummy_head.next.prev = newNode
        self.dummy_head.next = newNode
        
        
        self.size += 1
    def add_last(self, item):
        """ Add item to the end of the list.

        Args:
            item: an object instance to be added
        """
        newNode = DLLNode(item, self.dummy_tail.prev, self.dummy_tail)
        self.dummy_tail.prev.next = newNode
        self.dummy_tail.prev = newNode
        
    
        self.size += 1
    def add_after(self, item, othernode):
        """ Insert item into the list, after the DLLNode othernode.

        Args:
            item: an object instance to be added
            othernode: a DLLNode in this list
        """
        newNode = DLLNode(item, othernode, othernode.next)


    def get_first(self):
        """ Return the first item from the list.

        Returns the instance, but does not remove it.
        """
        return self.dummy_head.next.element

    def get_last(self):
        """ Return the last item from the list.

        Returns the instance, but does not remove it.
        """
        return self.dummy_tail.prev.element

    def remove_first(self):
        """ Remove the first item from the list.

        Returns the instance that has been removed.
        """
        if self.size == 0:
            return None
        first = self.dummy_head.next
        self.dummy_head.next = first.next
        first.next.prev = self.dummy_head
        self.size -= 1
    def remove_last(self):
        """ Remove the last item from the list.

        Returns the instance that has been removed.
        """
        if self.size == 0:
            return None
        last = self.dummy_tail.prev
        self.dummy_tail.prev = last.prev
        last.prev.next = self.dummy_tail
        self.size -= 1
        return last.element
    def length(self):
        """ Return the number of items in the list.  """
        return self.size

    def remove_node(self, node):
        """ Remove a node and return its element.

        Args:
            node: a DLLNode in this list

        Note: wipes the DLLNode. """
        next_node = self.dummy_head.next
        item = 0
        for i in range(self.size):
            if node == next_node:
                item = next_node.element
                nodeafter = next_node.next
                nodebefore = next_node.prev
                next_node.prev = None
                next_node.next = None
                nodeafter.prev = nodebefore
                nodebefore.next = nodeafter
                next_node.element = None
                size -= 1
            else:
                next_node = next_node.next

        return item
