Students = 5

scores = []
scoreSum = 0

for i in range(Students):
    value = int(input("성적을 입력하시오: "))
    scores.append(value)
    scoreSum += value

Average = scoreSum/Students   # Students 대신 len(scores) 써도 됨.

goodStudents = 0
for i in range(len(scores)):
    if scores[i] >= 80:
        goodStudents += 1

print("성적 평균은", Average, "입니다.")
print("80점 이상 성적을 받은 학생은", goodStudents,"명입니다.")
