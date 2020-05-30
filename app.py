from flask import Flask, render_template, request, redirect

app =  Flask(__name__)

linguagens  = [
    'python', 'javascript', 'C++', 'PHP', 'Golang', 'Reactnative'
]

@app.route('/')

def index():
   return render_template('index.html', linguagens = linguagens)


@app.route('/add', methods=['POST'])
def add():
    linguagem = request.form['linguagem']
    linguagens.append(linguagem)
    return redirect('/')

if __name__ == '__main__':
    app.run()