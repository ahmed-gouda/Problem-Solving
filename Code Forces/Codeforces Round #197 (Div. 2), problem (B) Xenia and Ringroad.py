current_place=1

res=[]
number_of_houses,things_to_do=map(int,input().split())
things=list(map(int,input().split()))
for i in things:
    number_of_moves=0
    if i<current_place:
        number_of_moves=(number_of_houses-current_place)+1
        current_place=1
    if i>=current_place:
        number_of_moves+=i-current_place
        current_place=i
    res.append(number_of_moves)
        
print(sum(res))