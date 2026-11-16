
import random
import arabic_reshaper
from bidi.algorithm import get_display



def fa(text):
    return get_display(arabic_reshaper.reshape(str(text)))

The_highest_score_Dr_Ardestani_has_given=10
#سمپل لیست اسامی فارسی
names = [
    "آفریدون", "آتش", "آبتین", "آراز", "آترین",
    "آتروپات", "آیدین", "آذرخش", "آرتین", "آراد",
    "آرین", "آرش", "آرمان", "آروین", "آریا",
    "امید", "بابک", "باربد", "بهرام", "بهمن",
    "بیژن", "جمشید", "خسرو", "خشایار", "داریوش",
    "رادین", "رامین", "رستم", "سامان", "سهراب",
    "سیاوش", "سینا"
]

#سپمل لیست نام خانودگی فارسی
last_names = [
    "محمدی", "احمدی", "حسینی", "رضایی", "کریمی",
    "موسوی", "جعفری", "حیدری", "مرادی", "رحیمی",
    "قاسمی", "اکبری", "صادقی", "کاظمی", "عباسی",
    "زارعی", "نجفی", "رستمی", "شریفی", "نوری",
    "فراهانی", "بهرامی", "سلیمانی", "غفاری", "یوسفی",
    "اسدی", "محمودی", "حسنی", "امیری", "حکیمی"
]

every_detail = []

# ساخت 100 دانشجو
for i in range(25):

    student = []

    # نام و نام خانوادگی
    random_name = random.randint(0, len(names) - 1)
    random_lastname = random.randint(0, len(last_names) - 1)

    full_name = names[random_name] + " " + last_names[random_lastname]
    student.append(full_name)

    # کد ملی
    student.append(str(random.randint(100000000, 999999999)))

    # شماره دانشجویی
    student.append(str(random.randint(100000, 999999999)))

    
    

    # 8 نمره درسی
    for j in range(8):
        student.append(round(random.uniform(0, The_highest_score_Dr_Ardestani_has_given), 2))

    every_detail.append(student)


# نمایش اطلاعات دانشجویان
for i in range(len(every_detail)):

    print("--------------------------------")

    print(fa("دانشجو شماره") , i + 1)

    print(fa("نام و نام خانوادگی:"), fa(every_detail[i][0]))

    print(fa("کد ملی:"), every_detail[i][1])

    print(fa("شماره دانشجویی:"), every_detail[i][2])

    

    for j in range(7):
        print(fa("درس"), j + 1, ":", every_detail[i][j + 4])
