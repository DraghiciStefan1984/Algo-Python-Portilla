class BinaryTree:
    def __init__(self, root, root_object):
        self.key=root_object
        self.left_child=None
        self.right_child=None

    def insert_left(self, new_node):
        if not self.left_child:
            self.left_child=BinaryTree(new_node)
        else:
            t=BinaryTree(new_node)
            t.left_child=self.left_child
            self.left_child=t

    def insert_right(self, new_node):
        if not self.right_child:
            self.right_child=BinaryTree(new_node)
        else:
            t=BinaryTree(new_node)
            t.right_child=self.right_child
            self.right_child=t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, obj):
        self.key=obj

    def get_root_value(self):
        return self.key