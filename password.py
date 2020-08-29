password = 'a123456'
error = 3
while error <= 3:
    a = input('輸入密碼: ')
    if a == password:
        print('登入成功! ')
        break
    elif a != password and error == 3:        
        print('密碼錯誤!還有2次機會!')
        error = error - 1
    elif a != password and error == 2:
        print('密碼錯誤!還有1次機會!')
        error = error - 1
    elif a != password and error == 1:
        print('密碼錯誤!停止輸入!')
        break