from Node import Node
import random
import queue

##using BFS
def TraverseBFS(n):
    q =  queue.Queue()
    q.put(n)
    while q.qsize() > 0:
        curNode = q.get()
        if curNode.left != None:
            q.put(curNode.left)
        if curNode.right != None:
            q.put(curNode.right)
        print(str(curNode.data))
          
     
 

        
   


def IsBST(n, min , max):
    if n == None:
        return False
    result = True
    if n.left != None:
        if n.left.data > min and n.left.data < max:
            result = IsBST(n.left , min , n.data)
        else:
            return False
    if n.right != None:
        if result and n.right.data > min and n.right.data < max:
            result = IsBST(n.right , n.data , max)
        else:
            return False
    return result
    

def Insert(root, n):
    if n == None:
        return
    if root == None:
        return 
    if n.data > root.data:
        if root.right != None:
            Insert(root.right , n)
        else:
            root.right = n
            return
    elif n.data < root.data:
        if root.left != None:
            Insert(root.left, n)
        else:
            root.left = n
            return
    




r = random.sample(range(1, 200) , 2)
root = Node(50 , None, None)
for i in r:
    Insert(root ,Node(i, None , None))

TraverseBFS(root)