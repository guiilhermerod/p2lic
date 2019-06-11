def listas ():
    s= open('series.csv', 'r')
    s_novas= open('series_novas.csv', 'r')
    for line in s.readlines():
        s= line.split(',')
        lista = s[4]
        a= list(lista)
        print (a)
listas ()
    

