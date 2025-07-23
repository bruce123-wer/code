#判断字符串是否为回文
def is_palindrome(s):
    s1 = s[::-1]
    if s == s1:
        return True
    else:
        return False
    
print(is_palindrome(input("请输入字符串：")))
