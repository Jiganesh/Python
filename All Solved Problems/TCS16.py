# Read only region start
class UserMainCode (object):
    @classmethod
    def minHeight(cls, input1, input2, input3):
        '''
        input1 : string
        input2 : string
        
        Expected return type: string[]
        '''
        preorder = input1
        inorder  = input2
        
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right: return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        tree = array_to_tree(0, len(preorder) - 1)
        
        def minDepth(root):

            def helper(root):
                
                if root == None:
                    return 0
                
                else:
                    
                    minLeft = helper(root.left)
                    minRight = helper(root.right)
                    
                    if minLeft ==0 or minRight ==0:
                        return 1+max(minLeft, minRight)
                    
                    return 1+ min(minLeft, minRight)
                
            return helper(root)
        
        return minDepth(tree)
        

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right