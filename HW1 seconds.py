seconds = int (input ('Введите количество секунд: '))
days = seconds // 86400
hours = seconds%86400//3600
minutes = ((seconds%86400)%3600)//60
sec = (((seconds%86400)%3600)%60)
print('Указанное количество секунд составляют:',days,' дней', hours ,' часов',minutes,' минут',sec,' секунд')