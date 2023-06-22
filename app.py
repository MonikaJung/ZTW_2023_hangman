from flask import Flask, render_template

app = Flask(__name__)

MAX_MISTAKES_EASY: int = 13
CATEGORY_NAME: str = "category name"

current_mistakes: int = 0

@app.route('/')
def index():
    return render_template("main_page.html", category=CATEGORY_NAME, mistakes=current_mistakes, max_mistakes=MAX_MISTAKES_EASY)

def choose_letter():
    return render_template("main_page.html", category=CATEGORY_NAME, mistakes=current_mistakes, max_mistakes=MAX_MISTAKES_EASY)

if __name__ == '__main__':
    app.run()
