from final_1_6_A import *

new = NewBook('Zeus', '1-1', 'Jackson', 'Penguin', '1st', 1900, 16.99)
new.print()
print('New price:', new.calculate_price())

used = UsedBook('Laurence of Arabia', '1-9', 'Rence', 'Oslo', '8th', 1931, 20.0, 10)
used.print()
print('Used price:', used.calculate_price())
