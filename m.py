# import turtle 

# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.done()
#-------------------------------------------------------
# import turtle

# turtle.color("blue")
# turtle.begin_fill()
# turtle.circle(50)
# turtle.end_fill()

# turtle.done()
#-----------------------------------------------
# import turtle

# # إعداد السلحفاة
# # pen.shape("turtle")       # ده الشكل الافتراضي
# # pen.shape("arrow")        # ده شكل سهم
# # pen.shape("classic")      # شكل بسيط
# # pen.shape("triangle")     # شكل مثلث
# # pen.shape("circle")       # شكل دائرة

# pen = turtle.Turtle()
# pen.color("black")
# pen.pensize(3)
# # pen.hideturtle()
# pen.speed(2)
# pen.shape("circle")       # شكل دائرة

# # نبدأ تعبئة اللون
# pen.begin_fill()

# # نرسم القلب
# pen.left(140)
# pen.forward(113)
# pen.circle(-57, 200)
# pen.left(120)
# pen.circle(-57, 200)
# pen.forward(113)

# # ننهي تعبئة اللون
# pen.end_fill()

# # نرفع القلم ونروح نكتب
# pen.penup()
# pen.goto(-40, 20)
# pen.color("white")
# pen.write("i Luv U", font=("Arial", 18, "bold"))
# # # نوقف النافذة لحد ما المستخدم يقفلها
# pen.hideturtle()
# turtle.done()

#--------------------------------------
def file_exe():
 m=open("h_3.txt",'x')
 m.write("filllleee2")
 m.close()
 n=open("h_3.txt",'r')
 n.close()
 t=n.read()
 print(t)
