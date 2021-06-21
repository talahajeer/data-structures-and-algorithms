from tree.tree import *
def tree_intersection(tree1, tree2):
	  intersect = [] 
	  
	  if tree1.root == None or tree2.root == None:
			  return None
	  def walk(root1,root2):
		  if root1.value == root2.value:
			  intersect.append(root1.value)

		  if root1.left:
			  walk(root1.left,root2.left)

		  if root1.right:
			  walk(root1.right,root2.right)
	  walk(tree1.root,tree2.root)
	  return intersect

if __name__ == "__main__":
# TEST CASE 1
  node1 = TNode(150)
  node1.left = TNode(100)
  node1.left.left = TNode(75)
  node1.left.right = TNode(160)
  node1.left.right.left = TNode(125)
  node1.left.right.right = TNode(175)
  node1.right = TNode(250)
  node1.right.left = TNode(200)
  node1.right.right = TNode(350)
  node1.right.right.left = TNode(300)
  node1.right.right.right = TNode(500)
  
  node2 = TNode(42)
  node2.left = TNode(100)
  node2.left.left = TNode(15)
  node2.left.right = TNode(160)
  node2.left.right.left = TNode(125)
  node2.left.right.right = TNode(175)
  node2.right = TNode(600)
  node2.right.left = TNode(200)
  node2.right.right = TNode(350)
  node2.right.right.left = TNode(4)
  node2.right.right.right = TNode(500)

  binary_tree1 = BinaryTree(node1)
  binary_tree2 = BinaryTree(node2)

  print(tree_intersection(binary_tree1,binary_tree2))