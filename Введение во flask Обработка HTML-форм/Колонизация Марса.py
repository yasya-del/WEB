from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return 'Миссия Колонизация Марса'
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>
              Человечеству мала одна планета.<br>
              Мы сделаем обитаемыми безжизненные пока планеты.<br>
              И начнем с Марса!<br>
              Присоединяйся!"""
@app.route('/image_mars')
@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <p> Вот она какая, красная планета.</p>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                  </body>
                </html>"""
@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Колонизация</title>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-danger" role="alert">
                        Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-warning" role="alert">
                        Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-success" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-info" role="alert">
                        И начнем с Марса!
                        </div>
                        <div class="alert alert-primary" role="alert">
                        Присоединяйся!
                        </div>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                      </body>
                    </html>"""
@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>Варианты выбора</title>
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          </head>
                          <body>
                            <h1>Мое предложение: {planet_name}</h1>
                            <h2>Эта планета близка к Земле;<h2>
                            <div class="alert alert-danger" role="alert">
                            Она самая классная!
                            </div>
                            <div class="alert alert-warning" role="alert">
                            Самая крутая!
                            </div>
                            <div class="alert alert-success" role="alert">
                            И находится во Вселенной!
                            </div>
                            <div class="alert alert-info" role="alert">
                            Короче, самая лучшая!@
                            </div>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                          </body>
                        </html>"""
@app.route('/astronaut_selection')
def astronaut_selection():
    pass
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')