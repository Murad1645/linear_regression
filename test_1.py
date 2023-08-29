x=[1,2,3,4,5]
y=[2,4,5,4,5]
sum_x=0
sum_y=0
sum_xy=0
sum_x2=0
[sum_x:=sum_x+element for element in x]
[sum_y:=sum_y+element for element in y]
[sum_x2:=sum_x2+(element*element) for element in x]

for i in range(len(x)):
    sum_xy+=x[i]*y[i]

m=((len(x)*sum_xy)-(sum_x*sum_y))/((len(x)*sum_x2)-(sum_x*sum_x))
c=((sum_y*sum_x2)-(sum_x*sum_xy))/((len(x)*sum_x2)-(sum_x*sum_x))
print(m)
print(c)
