import sys
from ruler import Ruler

file_name = sys.argv[1] #sys.argv permet de créer une liste avec les arguments rentrés dans cmd
f = open(file_name, 'r')
a = f.readlines()
k = 0
b = []
for i in range(len(a)):
    b.append(a[i].replace('\n', ''))

for i in range(0, len(b)-1, 2):
    ruler = Ruler(b[i], b[i+1])
    top, bottom = ruler.report()
    k += 1
    print(f"===== example #{k} - distance {ruler.distance}\n{top}\n{bottom}\n")