#!/usr/bin/python3
list_1 = [4, 6, 3]

def cumulative_sum(a_list):
	list_2 = []
	list_2.append(a_list[0])
	x = 1
	y = 0
	for i in a_list:
		if len(a_list) == x:
			break
		else:
			var1 = list_2[x]
			var2 = a_list[y]
			var3 = var1 + var2	
			list_2.append(var3)
			x+=1
			y+=1
		return list_2
print(cumulative_sum(list_1))
