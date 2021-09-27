from Node import Node

class Stack:
    def __init__( self ):
        self.head = None

    def insertFirst( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def remove( self ):
        if self.top != None:
            current = self.top
            self.top = current.next
            current.next = None

    def deleteNode( self, val ):
        if self.head == None:
            return None
        current = self.head
        previous = self.head
        if self.head.val == val:
            self.head = self.head.next
            current.next = None
        else:
            while current != None and current.val != val:
                previous = current
                current = current.next
            if current != None:
                previous.next = current.next
                current.next = None

    def printList( self ):
        current = self.head
        if current != None:
            print( "LIST HAS BEEN UPDATED, LOOK DOWN!" )
            print( current.val )
            current = current.next
        elif current == None:
            print( "NOTHING ON THE LIST BY THE MOMENT" )