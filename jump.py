for i in range(1,101):
#用for循环从1-100遍历
    if i % 7 == 0 or i % 10 ==7 or i // 10 == 7:
#排除被7整除(i % 7 == 0），个位为7(i % 10 == 7,除10余数为7),十位为7(i // 10 == 7,数字除10整数位为7)
        continue
#tiao guo yi shang 3 zhong qing kuang
    print(i)
