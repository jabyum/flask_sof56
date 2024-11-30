from flask import Flask, render_template, request
questions = {}
# создаем объект фласка
app = Flask(__name__)
@app.route("/") # создаем url к следующей функции
def home_page(): # создаем views
    test = "а это информация из бэка"
    return render_template("index.html", back=test)
#создаем динамичную ссылку
@app.route("/user/<int:pk>/video/<string:name>") # обрабатываю любую число
def user_info(pk, name): # сохраняю это число в переменную
    return f"информация видео {name} юзера {pk}"
@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
        title = request.form.get("title")
        main_text = request.form.get("main_text")
        questions[title] = main_text
        return render_template("question.html", questions=questions)
    elif request.method == "GET":
        return "так по ссылке переходить нельзя "
# запуск проекта во время тестирования
app.run(debug=True)


