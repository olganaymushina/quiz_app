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
    all_results = []
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
        # for item in form_data.items():
        return render_template("results.html", rows=sql_rows, template_form=choice_form)


            # if item[0] != 'submit':
            #     form_key = int(item[0].replace('question', ''))
            #     form_value = item[1].upper()
                
            #     # declare item_results with default
            #     item_results = {
            #         'question_id': str(form_key),
            #         'user_answered': '',
            #         'correct_answer': '',
            #         'is_correct': False
            #     }

                # print('this is my item to compare', form_key, form_value)
                

                # if form_value == sql_rows.get(form_key).upper():
                #     print('it is correct')
                #     item_results = {
                #         'question_id': str(form_key),
                #         'user_answered': form_value.upper(),
                #         'correct_answer': sql_rows.get(form_key).upper(),
                #         'is_correct': True
                #     }

                # else: 
                #     print('it is not correct')
                #     item_results = {
                #         'question_id': str(form_key),
                #         'user_answered': form_value.upper(),
                #         'correct_answer': sql_rows.get(form_key).upper(),
                #         'is_correct': False
                #     }

            #     all_results.append(item_results)
            # print(*all_results)
        
