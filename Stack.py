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
        if self.head != None:
            current = self.head
            self.head = current.next
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
        while current != None:
            print( "LIST HAS BEEN UPDATED, LOOK DOWN!" )
            print( current.val )
            current = current.next

# Write a function called validateExpression.
    def validateExpression(self, wordString):
        parentheses = []
        argumentString = str(wordString) # This function receives a string as an argument
        for i in wordString:
            if i == '(':
                parentheses.append(i)
            else:
                if not parentheses:
                    print(wordString, "Contains invalid parentheses")
                    return
                else:
                    top = parentheses[-1]
                    if i == ')' and top == '(':
                        parentheses.pop()

        if not parentheses:
            print(wordString, "contains valid parentheses.")
        else:
            print(wordString, "contains invalid parentheses.")

# You must validate that the string has implemented parentesis
# correctly in a formula

# BONUS, validate that it has square brackets and curly braces implemented correctly as well

# x*(x+z) + x/(y-z) + d should return true
# t – (s-k + x should return false
# ((x + y) * (x + 7)) / )y( should return false
# (((x+z)/(x*y)) + 4 ) should return true
# x + y / ) z + 1 ( * (r - z) should return false
# (b - a) * ) c / 4 ( * (c + b) should return false
# (b - a) * ) c / 4 ( * (c + b)) should return false

# def validateExpression( formula ):
#     parenthesisStack = Stack()

#     for current in formula:
#         if current == "(" or current == "[" or current == "{":
#             parenthesisStack.insert( current )
#         if current == ")":
#             if parenthesisStack.isEmpty():
#                 return False
#             else:
#                 if parenthesisStack.top.val == "(":
#                     parenthesisStack.remove()
#                 else:
#                     return False
#         if current == "]":
#             if parenthesisStack.isEmpty():
#                 return False
#             else:
#                 if parenthesisStack.top.val == "[":
#                     parenthesisStack.remove()
#                 else:
#                     return False
#         if current == "}":
#             if parenthesisStack.isEmpty():
#                 return False
#             else:
#                 if parenthesisStack.top.val == "{":
#                     parenthesisStack.remove()
#                 else:
#                     return False

#     if parenthesisStack.isEmpty():
#         return True
#     else:
#         return False
    

# result = validateExpression( "(b - a) * ) c / 4 ( * (c + b)" )
# print( result )