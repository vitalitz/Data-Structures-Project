class link(object):
    """
    list of links
    """
    def __init__(self,addr):
        self._link_addr = addr
        self._next_link = None
    link_addr = property(fget=lambda self: self._link_addr, doc="The current link in the list")
    next_link = property(fget=lambda self: self._next_link, doc="The next link in the list")

    def _add_link(self,addr):
        """
        Adding an address to the list of links
        """
        x = self
        # in case firs link has the same address
        if x.link_addr == addr.link_addr:
            return
        # get the last link
        while x.next_link != None:
            x = x.next_link
            if x.link_addr == addr.link_addr:
                return
        x._next_link = addr


class RBTree_leaf(object):
    """
    Struct of a leaf in Red Black Tree
    """
    def __init__(self,word_value,addr):
        "leaf class variables"
        self._word_value = word_value
        self._link = link(addr)
        self._black = True
        self._left = None
        self._right = None
        self._p = None

    word_value = property(fget=lambda self: self._word_value, doc="the leaf search word.")
    link = property(fget=lambda self: self._link, doc="The Link who has the specified word word_value times.")
    black = property(fget=lambda self: self._black, doc="The color of the node, True= black.")
    left = property(fget=lambda self: self._left, doc="The left children of the node.")
    right = property(fget=lambda self: self._right, doc="The right children of the node.")
    p = property(fget=lambda self: self._p, doc="The parent of the node.")


class RBTree(object):
    """
    the Tree struct implementation.
    """
    def __init__(self,leaf = RBTree_leaf):
            self._nil = leaf(word_value = None,addr = None)
            self._root = self.nil
            self._leaf = leaf

    nil = property(fget=lambda self: self._nil, doc="The nil of all leaf in the tree")
    root = property(fget=lambda self: self._root, doc="The root of the tree")

    def insert_new_leaf(self, value, addr):
        """
        insert new value and link to the tree
        """
        self._insert_leaf(self._leaf(value,addr))

    def _left_rotate(self,x):
        """
        The Red black tree left rotation algorithm for leaf x
        """
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y._left._p = x
        y._p = x.p
        if x._p == self.nil:
            self._root = y
        elif x == x.p.left:
            x._p._left = y
        else: x._p._right = y
        y._left = x
        x._p = y

    def _right_rotate(self,x):
        """
        The Red black tree right rotation for leaf of x
        """
        y = x.left
        x._left = y.right
        if y.right != self.nil:
            y._right._p = x
        y._p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.right:
            x._p._right = y
        else : x._p._left = y
        y._right = x
        x._p = y

    def _insert_leaf(self,z):
        """
        Insertion of a leaf to the tree
        """
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z._word_value < x.word_value:
                x = x.left
            elif z._word_value == x.word_value:
                x._link._add_link(z.link)
                return
            else: x = x.right
        z._p = y
        if y == self.nil:
            self._root = z
        elif z.word_value < y.word_value:
            y._left = z
        else : y._right = z
        z._right = self.nil
        z._left = self.nil
        z._black = False
        self._insert_fixup(z)

    def _insert_fixup(self,z):
        """
        fix the tree properties.
        """
        while z.p.black == False:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.black == False:
                    z._p._black = True
                    y._black = True
                    z._p._p._black = False
                    z = z.p.p
                elif z == z.p.right:
                    z = z.p
                    self._left_rotate(z)
                else :
                    z._p._black = True
                    z._p._p._black = False
                    self._right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.black == False:
                    z._p._black = True
                    y._black = True
                    z._p._p._black = False
                    z = z.p.p
                elif z == z.p.left:
                    z = z.p
                    self._right_rotate(z)
                else :
                    z._p._black = True
                    z._p._p._black = False
                    self._left_rotate(z.p.p)
        self._root._black = True


    def _transplant(self,u,v):
        """
        Transplant of Red black tree
        """
        if u.p == self.nil:
            self._root = v
        elif u == u.p.left:
            u.p.left = v
        else: u.p.right = v
        v.p = u.p

    def _delete_fixup(self,x):
        """
        Fix for Red black tree delete algorithm
        """
        while x != self.root and x.black == True:
            if x == x.p.left:
                w = x.p.right
                if w.black == False:
                    w.black = True
                    x.p.black = False
                    self._left_rotate(x.p)
                    w = x.p.right
                if w.left.black == True and w.right.black == True:
                    w.black = False
                    x = x.p
                elif w.right.black == True:
                    w.left.black = True
                    w.black = False
                    self._right_rotate(w)
                    w = x.p.right
                else:
                    w.black = x.p.black
                    x.p.black = True
                    w.right.black = True
                    self._left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.black == False:
                    w.black = True
                    x.p.black = False
                    self._right_rotate(x.p)
                    w = x.p.left
                if w.right.black == True and w.left.black == True:
                    w.black = False
                    x = x.p
                elif w.left.black == True:
                    w.right.black = True
                    w.black = False
                    self._left_rotate(w)
                    w = x.p.left
                else:
                    w.black = x.p.black
                    x.p.black = True
                    w.left.black = True
                    self._right_rotate(x.p)
                    x = self.root
        x.black = True

    def delete(self,z):
        """
        Delete method of Red black tree
        """
        y = z
        y_original_black = y.black
        if z.left == self.nil:
            x = z.right
            self._transplant(z,z.right)
        elif z.right == self.nil:
            x = z.left
            self._transplant(z,z.left)
        else:
            y = self.minimum_value(z.right)
            y_original_black = y.black
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self._transplant(y,y.right)
                y.right = z.right
                y.right.p = y
            self._transplant(z,y)
            y.left = z.left
            y.left.p = y
            y.black = z.black
        if y_original_black == True:
            self._delete_fixup(x)


    def search(self,x,word_value):
        """
        searching for a value in the subtree of x
        """
        if None == x:
            x = self.root
        while x != self.nil and word_value != x.key:
            if word_value < x._word_value:
                x = x.left
            else:
                x = x.right

    def minimum_value(self,root = None):
        """
        The minimum value in subtree of root
        """
        if root == None:
            root = self._leaf.left
        while root.left != self.nil:
            root = root.left
        return root.word_value

    def maximum_value(self,root = None):
        """
        The maximum value of the subtree of root
        """
        if root == None:
            root = self._leaf.right
        while root.right != self.nil:
            root = root.right
        return root.word_value

    def inorder(self,x,myfile):
        """
        Print the tree from smallest to greatest value
        """
        if x != self.nil:
            self.inorder(x.left,myfile)
            mylink = x.link
            while mylink != None:
                myfile.write('link:' + mylink.link_addr + '; word appearance:' + '%d \n' %x.word_value)
                mylink = mylink.next_link
            self.inorder(x.right,myfile)

    def preorder(self,x,myfile):
        """
        print the tree root first and left subtree and after right subtree
        """
        if x != self.nil:
            mylink = x.link
            while mylink != None:
                myfile.write('link:' + mylink.link_addr + '; word appearance:'  + '%d \n' %x.word_value)
                mylink = mylink.next_link
            self.inorder(x.left,myfile)
            self.inorder(x.right,myfile)

    def print_tree(self, x, myfile,tree_file):
        """
        Print the tree from greatest to smallest value
        """
        if x != self.nil:
            self.print_tree(x.right,myfile,tree_file)
            mylink = x.link
            while mylink != None:
                myfile.write('link:' + mylink.link_addr + '; word appearance: ' + '%d \n' %x._word_value)
                mylink = mylink.next_link
            if x == self._root :
                tree_file.write('root of the tree is %d, black %s \n'%(x._word_value,x._black))
            else: tree_file.write('parent: %d value: %d Black: %s \n' %(x._p._word_value,x._word_value,x._black))
            self.print_tree(x.left,myfile,tree_file)


