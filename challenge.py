p1 = float(input('Type the first exam.' ))
p2 = float(input('Type the second exam.' ))
p3 = float(input('Type the third exam.'))
m_calculation = round((p1 + p2 + p3) / 3, 1)
print(m_calculation)
#m = float(input('Type your average grade.'))
#for the naf I used the bigger grade.

m = m_calculation
class_days = 60
days_missed = int(input('Type the days missed.' ))
#failed = int(class_days / 100 * 25)
#25% of 60 = 15

if days_missed > 0 and days_missed > 15:
  naf = 0
  print('Sorry, you failed.' )
else:
    print('OK')

if m < 5:
  print('Reprovado por nota.' )
  naf = 0

elif m >= 5 and m < 7:
  print('Exame Final')
  naf = float(input('Type the final grade.'))
  final_grade = (m + naf) / 2
  round(final_grade, 1)
  if final_grade > 5:
    print('Congrats, approved!' )
  else:
    print('Sorry, failed.' )

else:
  print('Congrats, approved!' ) 