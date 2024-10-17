from flask import Flask, render_template_string
import random

app = Flask(__name__)


def generate_daily_fortune():
    random.seed(0)  # 确保每次访问时数字不变
    career_fortune = random.randint(0, 100)
    love_fortune = random.randint(0, 100)
    wealth_fortune = random.randint(0, 100)

    return career_fortune, love_fortune, wealth_fortune


@app.route('/')
def index():
    career, love, wealth = generate_daily_fortune()
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="zh">
    <head>
        <meta charset="UTF-8">
        <title>每日运势</title>
    </head>
    <body>
        <h1>今日运势</h1>
        <ul>
            <li>事业运: {{ career }}</li>
            <li>桃花运: {{ love }}</li>
            <li>财运: {{ wealth }}</li>
        </ul>
    </body>
    </html>
    ''', career=career, love=love, wealth=wealth)


if __name__ == '__main__':
    app.run(debug=True)