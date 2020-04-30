#using string reverse
def id(s):
	return s==s[::-1]
#brute force
def identify(s,i=0):
    n = len(s)-1
    if n-i<=i:
        return True
    elif s[i]==s[n-i]:
        return identify(s,i+1)
    else:
        return False

print('Enter String:')
s = input()
if identify(s):
    print('The input is a palindrome')
else:
    print('The input is not a palindrome')
