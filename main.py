#Main file which runs everything
from binarytree import tree, bst, heap, Node, build
import FindPlayer
import ages
import landing
import singleElim

#tree = tree(height=3, is_perfect=True)
singleElim.singleElim()
#singleElim.postOrderTrav(tree)
#ages.getOldest()

#Runs the home window in the landning file
'''
root1 = tk.Tk()
landing.HomeWin(root1, 'landing')
root1.mainloop()
'''