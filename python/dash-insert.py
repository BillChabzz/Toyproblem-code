# Dash Insert
# Using python, have the function DashInsert(str) insert dashes ('-') between each two odd numbers in string.
# For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
def DashInsert(num):
    num_str = str(num)
    new_str = ''
    for i in num_str:
        n = int(i)
        if n %2 == 0:
            new_str += i + '-'
    return new_str
print DashInsert(raw_input())
