import sqlite3 
from flask import Flask, render_template, request, redirect
from forms import ChoiceForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/questions')
def question():
    choice_form = ChoiceForm(csrf_enabled = False)
    con = sqlite3.connect("quiz.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT q_id, question, choice_a, choice_b, choice_c, choice_d FROM questions")
    rows = cur.fetchall()
    con.commit()
    con.close
    # print(choice_form)
    print(rows)
    return render_template("question.html", rows=rows, template_form = choice_form)

@app.route("/answer", methods = ["GET", "POST"])
def answer():
    choice_form = ChoiceForm(csrf_enabled = False)
    if request.method == "POST":
        con = sqlite3.connect("quiz.db")
        cur = con.cursor()
        cur.execute("SELECT q_id, correct_answer FROM questions")
        sql_rows = dict(cur.fetchall())
        con.commit()
        con.close
        # q_id = request.form["q_id"]
        form_data = dict(request.form.items())
        print('form_data', form_data)
        print('sql_rows', sql_rows)

        all_results = []
        total_questions = len(sql_rows)
        number_correctly_answered = 0

        for item in sql_rows.items():
            answer_key_question_id = str(item[0])
            answer_key_question_answer = item[1]
            
            # check to see if user answered the question 
            if answer_key_question_id in form_data:
                # user answered, check if it correct
                if (answer_key_question_answer == form_data[answer_key_question_id].upper()):
                    item_results = {
                        'question_id': answer_key_question_id,
                        'user_answered': form_data[answer_key_question_id].upper(),
                        'correct_answer': answer_key_question_answer,
                        'is_correct': True
                    }
                    number_correctly_answered = number_correctly_answered + 1
                # user answered, but it is incorrect
                else:
                    item_results = {
                    'question_id': answer_key_question_id,
                    'user_answered': form_data[answer_key_question_id].upper(),
                    'correct_answer': answer_key_question_answer,
                    'is_correct': False
                }
            #user did not answer so it is incorrect
            else:
                item_results = {
                    'question_id': answer_key_question_id,
                    'user_answered': '',
                    'correct_answer': answer_key_question_answer,
                    'is_correct': False
                }
            all_results.append(item_results)
        return render_template("results.html", all_results=all_results, total_questions=total_questions, number_correctly_answered=number_correctly_answered, template_form=choice_form)

