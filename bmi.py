weight = input('wieght(kg)')
weight = int(weight)
heigh = input('heigh(cm)')
heigh = int(heigh)
heigh = heigh / 100

bmi = weight / heigh / heigh
if bmi < 18.5:
	print('too thin')
elif bmi >= 18.5 and bmi < 24:
	print('normal')
elif bmi >= 24 and bmi < 27:
	print('overweight')
elif bmi >= 27 and bmi < 30:
	print('little fat')
elif bmi >= 30 and bmi < 35:
	print('too fat')
elif bmi >= 35:
	print('obysse')