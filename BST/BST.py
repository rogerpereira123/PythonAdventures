from Node import Node

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
    



print(IsBST(root , 0 , 100))

