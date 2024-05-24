from flask import Flask, request, render_template

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return a

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    n = int(request.form['number'])
    result = fibonacci(n)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
