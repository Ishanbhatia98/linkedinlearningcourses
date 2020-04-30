#using sorted function
def sort_string(s):
    return ''.join(list(sorted(list(s))))

print('Enter string to sort:')
s = input()
print(f'The sorted string is {sort_string(s)}')
