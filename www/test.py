height = 0.69
weight = 10
bmi = weight/(height**2)
s = '您好 {0}, 您的BMI指数是: {1:.1f}, 您的体重'.format('Aroma',bmi)
if bmi < 18.5:
    print(s,'过轻')
elif 18.5 <= bmi < 25:
    print(s, '正常')
elif 25 <= bmi < 28:
    print(s, '过重')
elif 28 <= bmi < 32:
    print(s, '肥胖')
elif bmi >= 32:
    print(s, '严重肥胖')
