# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功!"
# 如果不正確 就印出 "密碼錯誤! 還有__次機會!"

x = 3

while x > 0:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功!')
		break
	else:
		x = x - 1
		print('密碼錯誤! 還有', x, '次機會!')