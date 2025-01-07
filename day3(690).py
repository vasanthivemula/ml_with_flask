a = float(input("Enter marks for Subject 1: "))
b = float(input("Enter marks for Subject 2: "))
c = float(input("Enter marks for Subject 3: "))
avg = (a + b + c) / 3
if avg >= 90:
result = "A"
elif 80 <= avg < 90:
result = "B"
elif 70 <= avg < 80:
result = "C"
else:
result = "Fail"
print(f"Grade: (Fail)")
