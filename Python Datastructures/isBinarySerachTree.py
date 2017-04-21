treeList = []
def inorder(tree):
    inorder(tree.getLeftChild())
    treeList.append(tree.getRootVal())
    inorder(tree.getRightChild())

def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)