import functools
l=[[2,4,5],[4,6,8],[3,6,9]]
all_value_sum=sum(functools.reduce(lambda a, b:a+b,l))
even_list=list(filter(lambda x: (x % 2 == 0), (functools.reduce(lambda a, b:a+b,l))))

# even_sum = sum([val for sublist in l for val in sublist if val%2==0])
# all_value_sum=sum(val for sublist in l for val in sublist)
print("the sum of all the numbers from all the inner lists : ",sum(even_list))
print("the sum of all the numbers from all the inner lists : ",all_value_sum)