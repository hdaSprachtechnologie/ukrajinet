import ua_lexentries
from ua_lexentries import lexlist

out = open('ua-sorted-lexentries.txt','w', encoding="utf-8")



for t in lexlist:
	newlist = []
	newlist.append(t)
	tindex = lexlist.index(t) + 1
	for x in lexlist[tindex:]:
		if x[0] == t[0]:
			newlist.append(x)
			lexlist.remove(x)
		else:
			newlist = newlist
	out.write(str(newlist) + ',\n')

out.close()
        
