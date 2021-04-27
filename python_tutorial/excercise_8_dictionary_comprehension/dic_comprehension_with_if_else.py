#dictionary comprehension with if else
dd={1:'odd',2:'even'}
dic_even_odd={num:('even' if num%2==0 else 'odd') for num in range(1,11)}
print(dic_even_odd)