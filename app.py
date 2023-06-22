from flask import Flask, render_template

app = Flask(__name__)

MAX_MISTAKES_EASY: int = 13
LETTER_USED = "disabled"
LETTER_ACTIVE = ""
PLAYER1:str = "player1 name"
PLAYER2:str = "player2 name"

current_mistakes: int = 13
current_category: str = "category name"
current_word_list: list = ["_ _ _", " _ _ _ _ _ _ _ _ _ _ _ _", " _ _ _ _ ",
                           " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"]
current_letters:list = [["A", LETTER_USED], ["B", LETTER_ACTIVE], ["C", LETTER_ACTIVE],
                        ["D", LETTER_ACTIVE], ["E", LETTER_ACTIVE], ["F", LETTER_ACTIVE],
                        ["G", LETTER_ACTIVE], ["H", LETTER_ACTIVE], ["I", LETTER_ACTIVE],
                        ["J", LETTER_ACTIVE], ["K", LETTER_ACTIVE], ["L", LETTER_ACTIVE],
                        ["M", LETTER_ACTIVE], ["N", LETTER_ACTIVE], ["O", LETTER_ACTIVE],
                        ["P", LETTER_ACTIVE], ["Q", LETTER_ACTIVE], ["R", LETTER_ACTIVE],
                        ["S", LETTER_ACTIVE], ["T", LETTER_USED], ["U", LETTER_ACTIVE],
                        ["V", LETTER_ACTIVE], ["W", LETTER_ACTIVE], ["X", LETTER_ACTIVE],
                        ["Y", LETTER_ACTIVE], ["Z", LETTER_ACTIVE], ["Ą", LETTER_ACTIVE],
                        ["Ć", LETTER_ACTIVE], ["Ę", LETTER_ACTIVE], ["Ł", LETTER_ACTIVE],
                        ["Ń", LETTER_ACTIVE], ["Ó", LETTER_ACTIVE], ["Ś", LETTER_ACTIVE],
                        ["Ź", LETTER_ACTIVE], ["Ż", LETTER_ACTIVE]]

@app.route('/')
def index():
    return render_template("main_page.html",
                           letters=current_letters,
                           word_list=current_word_list, category=current_category,
                           plsyer1=PLAYER1, payer2=PLAYER2,
                           mistakes=current_mistakes, max_mistakes=MAX_MISTAKES_EASY)

def choose_letter():
    return render_template("main_page.html",
                           word=current_word_list, category=current_category,
                           plsyer1=PLAYER1, payer2=PLAYER2,
                           mistakes=current_mistakes, max_mistakes=MAX_MISTAKES_EASY)


if __name__ == '__main__':
    app.run()
