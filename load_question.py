import sqlite3
from import_questions import questions

conn = sqlite3.connect("question.db")
cur = conn.cursor()



for q in questions:
    (
        q_it, ca_it, w1_it, w2_it, w3_it,
        q_en, ca_en, w1_en, w2_en, w3_en,
        difficulty, category
    ) = q

    cur.execute("""
    INSERT INTO questions
    (question,correct_answer,wrong_answer1,wrong_answer2,wrong_answer3,difficulty,category,language)
    VALUES (?,?,?,?,?,?,?,?)
    """, (
        q_it, ca_it, w1_it, w2_it, w3_it,
        difficulty, category, "it"
    ))

    cur.execute("""
    INSERT INTO questions
    (question,correct_answer,wrong_answer1,wrong_answer2,wrong_answer3,difficulty,category,language)
    VALUES (?,?,?,?,?,?,?,?)
    """, (
        q_en, ca_en, w1_en, w2_en, w3_en,
        difficulty, category, "en"
    ))

conn.commit()
conn.close()