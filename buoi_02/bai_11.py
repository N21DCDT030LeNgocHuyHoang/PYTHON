n=int(input('nhap N: '))
a=[int(input('nhap ngay thu %d: '%i)) for i in range (1,n+1)]
tb=sum(a)/n
print('nhiet do trung binh cua N ngay:',tb)
s=len([a[i] for i in  range (n) if (a[i]>tb)])
print('so ngay co nhiet do cao hon nhiet do trung binh:',s)