def write_to_file(path, d):
    f = open(path, 'w')
    f.write(d)
    print(f'Dictionary object successfully saved to file {path}')

def read_from_file(path):
    f = open(path, 'r')
    print('The dictionary object is:')
    print(*f)

print("Press 'r' to read a file and press 'w' to write a dictionary object to a file")
i = input()
if i=='r':
    print('Please enter path to file(including filename with ".txt")')
    path = input()
    read_from_file(path)
elif i=='w':
    print('Please enter path to file(including filename with ".txt")')
    path = input()
    print('Please enter dictionary object to be saved')
    d = input()
    write_to_file(path, d)
else:
    print('Invalid input.Please try again')
