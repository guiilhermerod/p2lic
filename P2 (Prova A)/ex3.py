tbbt=0
fs=0
bb=0
bm=0
sts=0
fh=0
ds=0
lcf=0
v= open('series.csv','r')
n= open('series_novas.csv','r')
for line in v.readlines():
    sep= line.split(',')
    if sep[0]=="The Big Bang Theory":
        tbbt= tbbt+1
    elif sep[0]=="Friends":
        fs= fs + 1 
    elif sep[0]=="Breaking Bad":
        bb= bb+1
    elif sep[0]=="Black Mirror":
        bm= bm+1
for line1 in n.readlines():
    sep1= line1.split(',')
    if sep1[0]=="Suits":
        sts= sts+1
    elif sep1[0]=="Fuller House":
        fh= fh+1
    elif sep1[0]=="Designated Survivor":
        ds= ds+1
    elif sep1[0]=="Lucifer":
        lcf= lcf+1
    
print ('The Big Bang Theory:',tbbt,'episodios')
print ('Friends:',fs,'episodios')
print ('Breaking Bad:',bb,'episodios')
print ('Black Mirror:',bm,'episodios')
print ('Suits:',sts,'episodios')
print ('Fuller House:',fh,'episodios')
print ('Designated Survivor:',ds,'episodios')
print ('Lucifer:',lcf,'episodios')
