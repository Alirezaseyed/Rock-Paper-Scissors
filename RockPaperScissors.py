#برای شروع اول باید ماژول random را فراخوانی کنیم.

import random
#یک تابع میسازیم و اسم آن را check_win می گزاریم و دو پارامتر به آن میدهیم
#-----------
#پارامتر user نشان دهنده ورودی ارائه شده توسط کاربر و پارامتر کامپیوتر نشان دهنده انتخابی است که توسط دستگاه ما انجام می شود.
def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

#در مرحله بعد ما تابعی به نام rock_paper_scissors () ایجاد کرده ایم. این تابع ، هسته اصلی بازی ما خواهد بود.

#----
#ابتدا ، ما از کاربر ورودی را دریافت می کنیم. در اینجا کاربر می تواند فقط از طریق  r ،  s یا p ورودی وارد کند که به ترتیب سنگ ، قیچی و کاغذ است. اکنون ورودی کاربر در متغیر player کننده ذخیره شده است.
#حال ما می خواهیم از تابع random.choice () برای انتخاب تصادفی یک عنصر واحد از میان لیست ها استفاده کنیم.
def rock_paper_scissors():
    player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ")
    choices = ['r','s','p']
    opponent = random.choice(choices)


    if player == opponent:
        return print(f"mosavi shodi! raghib to {opponent} avorde")

    if check_win(player, opponent):
        return print(f"afariin! bordi! raghib to {opponent} avorde")

    if check_win(player, opponent) != True:
        return print(f"to bakhti! raghib to {opponent} avorde")

rock_paper_scissors()
