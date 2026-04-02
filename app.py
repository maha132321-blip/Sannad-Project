from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

# متغير عالمي لتخزين اسم المستخدم بعد تسجيل الدخول
current_user = "طالب"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login_check', methods=['POST'])
def login_check():
    global current_user
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('role')

    # التحقق من كلمة المرور
    if password == "1234":
        # استخراج الاسم من الإيميل (ما قبل الـ @)
        current_user = email.split('@')[0]
        return redirect(f'/{role}')
    else:
        return "<h1>خطأ: كلمة المرور هي 1234</h1><a href='/'>رجوع</a>"

@app.route('/student')
def student():
    return render_template('student_dashboard.html', student=current_user)

@app.route('/doctor')
def doctor():
    file_path = 'students_data.xlsx'
    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
            students_list = df.to_dict(orient='records')
        except:
            students_list = []
    else:
        students_list = [] # في حال عدم وجود ملف الإكسل بعد
    return render_template('doctor_dashboard.html', students=students_list)

if __name__ == '__main__':
    app.run(debug=True)
    # أضيفي هذه الأسطر في نهاية ملف app.py قبل (if __name__ == '__main__':)

@app.route('/my_results')
def my_results():
    return "<h1>صفحة النتائج - قيد التطوير</h1>"

@app.route('/notifications')
def notifications():
    return "<h1>صفحة التنبيهات - قيد التطوير</h1>"

@app.route('/settings')
def settings():
    return "<h1>صفحة الإعدادات - قيد التطوير</h1>"