from fractions import Fraction
import itertools
import sys

'''
The BNode class here is used to build a binary tree. 
The 'addleft' and 'addright' methods enable us to build the 
tree up. 

In this game, 4 cards are randomly picked from a standard deck of 52 cards. 
We will use the values of these 4 cards and a combination of addition, 
subtraction, multiplication, division, and parentheses to produce the 
value 24. Note that each of the 4 cards can only be used once.
For the purposes of this assignment, we will consider the following 
to be the face values of each card in a suit:
“A”: 1 “2”: 2 “3”: 3 “4”: 4 “5”: 5 “6”: 6 “7”: 7 
“8”: 8 “9”: 9 “10”: 10 “J”: 11 “Q”: 12 “K”: 13
'''

ops = ['+', '-', '*', '/']
d = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6, '7': 7,
     '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}

class BNode:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

    def addleft(self, leftnode):
        self.left = leftnode

    def addright(self, rightnode):
        self.right = rightnode

    def evaluate(self): 
        '''
        This method will take a node of the binary tree and recursively 
        call evaluate method to evaluate it.
        '''
        # An empty tree. 
        if self.element is None: 
            return 0
      
        # A leaf node.
        if self.left is None and self.right is None: 
            return int(d[self.element]) 
      
        # Evaluate left tree.
        left_sum = self.left.evaluate()   

        # Evaluate right tree.
        right_sum = self.right.evaluate()
      
        # Check which operation to apply.
        if self.element == '+': 
            return left_sum + right_sum 
          
        elif self.element == '-': 
            return left_sum - right_sum 
          
        elif self.element == '*': 
            return left_sum * right_sum 
          
        else: 
            if right_sum == 0:
                return 0
            return Fraction(left_sum, right_sum)

    def display(self):
        '''
        This method will display all the values of the nodes in the binary 
        tree in infix notation.
        '''
        if self.element is None: 
            return None

        # Leaf node. 
        if self.left is None and self.right is None: 
            return str(d[self.element]) 
      
        # Evaluate left tree. 
        left_sum = self.left.display()      
        
        # Evaluate right tree.
        right_sum = self.right.display()
      
        # Check which operation to apply.
        if self.element == '+': 
            return '(' + str(left_sum) + '+' + str(right_sum) + ')'
          
        elif self.element == '-': 
            return '(' + str(left_sum) + '-' + str(right_sum) + ')'
          
        elif self.element == '*': 
            return '(' + str(left_sum) + '*' + str(right_sum) + ')'
          
        else: 
            return '(' + str(left_sum) + '/' + str(right_sum) + ')'

def evaluatefive(ops, cards):
    '''
    This function will find all valid forms of representing an expression using 
    a binary expression tree for each 4 card combination and evaluate them to 
    see if they are equal to 24. Every valid possible expression will take one 
    of these five forms.
    '''
    s = set()
    # Tree #1        
    node1 = BNode(ops[0])
    node2 = BNode(ops[1])
    node3 = BNode(ops[2])
   
    node4 = BNode(cards[0])
    node5 = BNode(cards[1])
    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node1.addleft(node2)
    node1.addright(node3)

    node2.addleft(node4)
    node2.addright(node5)

    node3.addleft(node6)
    node3.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())

    # Tree #2
    node8 = BNode(ops[0]) 
    node9 = BNode(ops[1]) 
    node10 = BNode(ops[2]) 

    node11 = BNode(cards[0]) 
    node12 = BNode(cards[1]) 
    node13 = BNode(cards[2]) 
    node14 = BNode(cards[3]) 
    
    node8.addleft(node9)
    node8.addright(node14)

    node9.addleft(node10)
    node9.addright(node13)

    node10.addleft(node11)
    node10.addright(node12)

    if node8.evaluate() == 24:
        s.add(node8.display())

    # Tree #3
    node15 = BNode(ops[0])
    node16 = BNode(ops[1])
    node17 = BNode(ops[2])

    node18 = BNode(cards[0])
    node19 = BNode(cards[1])
    node20 = BNode(cards[2])
    node21 = BNode(cards[3])

    node15.addleft(node16)
    node15.addright(node21)

    node16.addleft(node18)
    node16.addright(node17)

    node17.addleft(node19)
    node17.addright(node20)

    if node15.evaluate() == 24:
        s.add(node15.display())

    #tree #4
    node22 = BNode(ops[0])
    node23 = BNode(ops[1])
    node24 = BNode(ops[2])

    node25 = BNode(cards[0])
    node26 = BNode(cards[1])
    node27 = BNode(cards[2])
    node28 = BNode(cards[3])

    node22.addleft(node25)
    node22.addright(node23)

    node23.addleft(node24)
    node23.addright(node28)

    node24.addleft(node26)
    node24.addright(node27)

    if node22.evaluate() == 24:
        s.add(node22.display())

    #tree #5
    node29 = BNode(ops[0])
    node30 = BNode(ops[1])
    node31 = BNode(ops[2])

    node32 = BNode(cards[0])
    node33 = BNode(cards[1])
    node34 = BNode(cards[2])
    node35 = BNode(cards[3])

    node29.addleft(node32)
    node29.addright(node30)

    node30.addleft(node33)
    node30.addright(node31)

    node31.addleft(node34)
    node31.addright(node35)
    
    if node29.evaluate() == 24:
        s.add(node29.display())
    
    return s

