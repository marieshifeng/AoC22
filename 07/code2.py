import sys
 
 
class Node:
  def __init__(self, path, size):
    self.path = path
    self.children = []
    self.files = []
    self.size = 0
 
 
def getNode(s):
  for node in nodes:
    if node.path == s:
      return node
  sys.exit(0)
 
 
def getFullPath(cd):
  fp = ""
  for c in cd:
    if c.path != "/":
      fp += c.path
 
  return fp
 
 
def addUp(root):
  if root is not None:
    s = 0
    for child in root.children:
      addUp(child)
      for f in child.files:
        s += f["size"]
    root.size += s
 
 
def printTree(root):
  if root is not None:
    for child in root.children:
      printTree(child)
    if root.size <= 100000:
      print(root.path, root.size)
 
 
if __name__ == '__main__':
  f = open("small.txt", "r")
  lines = f.read().splitlines()
 
  R = Node('/', 0)
  nodes =[R]
  cd = [R]
 
  for line in lines:
    # command
    if line[0] == "$":
      # split to get command
      spl = line.split("$ ")[1]
      cmdsplit = spl.split(" ")
      cmd = cmdsplit[0]
 
      if cmd == "cd":
        where = cmdsplit[1]
        if where == "/":
          cd = [R]
        elif where == "..":
          cd.pop()
        else:
          fp = getFullPath(cd) + "/%s" % where
          cd.append(getNode(fp))
 
    # add directory to children with a full path
    elif "dir" in line:
      which = line.split("dir ")[1]
      fp = getFullPath(cd) + "/%s" % which
      newNode = Node(fp, 0)
      nodes.append(newNode)
      curr = cd[-1]
      curr.children.append(newNode)
 
    # add files to current child along with sizes
    else:
      fsplit = line.split(" ")
      fsize = fsplit[0]
      fname = fsplit[1]
      curr = cd[-1]
      curr.files.append({
        "size": int(fsize),
        "name": fname
      })
      curr.size += int(fsize)
 
  # add up values of all children to their parents up to "/"
  root = R
  addUp(root)
 
  # print tree's nodes that have <= 100000
  root = R
  printTree(root)