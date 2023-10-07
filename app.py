from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/lab2/example")
def example():
    name= "Юрий Комаров"
    number="2"
    group="ФБИ-11"
    course="3 курс"
    return render_template("example.html", name=name, number=number, group=group, course=course)

@app.route('/')
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <ol>
        <li><a href="http://127.0.0.1:5000/lab1" target="_blank">Первая лабораторная</a></li>
        </ol>

        <h2>Реализованные роуты</h2>

        <ol>
        <li><a href="http://127.0.0.1:5000/lab1/oak" target="_blank">/lab1/oak - дуб</a></li>
        <li><a href="http://127.0.0.1:5000/lab1/student" target="_blank">/lab1/student - студент</a></li>
        <li><a href="http://127.0.0.1:5000/lab1/python" target="_blank">/lab1/python - python</a></li>
        </ol>

        <footer>
            &copy; ФИО, группа, курс, год
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <head>
        <title>Комаров Юрий Павлович, лабораторная №1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <div>
        Flask — фреймворк для создания веб-приложений на языке программирования Python.
        </div>

        <ol>
        <li><a href="http://127.0.0.1:5000/menu">Меню<a/></li>
        </ol>

        <footer>
            &copy; Юрий Комаров, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/student")
def stud():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
      <h1>Комаров Юрий Павлович</h1>
      <img src="''' + url_for('static', filename='logo.png') + '''">
    </body>
</html>
'''

@app.route("/lab1/python")
def pyth():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>

        <div>
        Python (МФА: в русском языке встречаются названия пито́н[23] или па́йтон[24]) — высокоуровневый язык программирования общего назначения с 
        динамической строгой типизацией и автоматическим управлением памятью[25][26], ориентированный на повышение производительности разработчика, читаемости кода и его качества,
        а также на обеспечение переносимости написанных на нём программ[27]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[25]. 
        Необычной особенностью языка является выделение блоков кода пробельными отступами[28]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает 
        необходимость обращаться к документации[27]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[25]. Недостатками языка являются 
        зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, 
        таких как C или C++[25][27].
        </div>

        <div>
        Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование[25], 
        метапрограммирование[29] и функциональное программирование[25]. Задачи обобщённого программирования решаются за счёт динамической типизации[30][31]. 
        Аспектно-ориентированное программирование частично поддерживается через декораторы[32], более полноценная поддержка обеспечивается дополнительными фреймворками[33]. 
        Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений[34]. Основные архитектурные черты — динамическая типизация, 
        автоматическое управление памятью[25], полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL)[35], 
        высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты[36].
        </div>

        <div>
        Эталонной реализацией Python является интерпретатор CPython, который поддерживает большинство активно используемых платформ[37] и являющийся стандартом де-факто языка[38]. 
        Он распространяется под свободной лицензией Python Software Foundation License, позволяющей использовать его без ограничений в любых приложениях, включая проприетарные[39]. 
        CPython компилирует исходные тексты в высокоуровневый байт-код, который исполняется в стековой виртуальной машине[40]. К другим трём основным реализациям языка относятся 
        Jython (для JVM), IronPython (для CLR/.NET) и PyPy[25][41]. PyPy написан на подмножестве языка Python (RPython) и разрабатывался как альтернатива CPython с целью повышения 
        скорости исполнения программ, в том числе за счёт использования JIT-компиляции[41]. Поддержка версии Python 2 закончилась в 2020 году[42]. На текущий момент активно развивается 
        версия языка Python 3[43]. Разработка языка ведётся через предложения по расширению языка PEP (англ. Python Enhancement Proposal), в которых описываются нововведения, 
        делаются корректировки согласно обратной связи от сообщества и документируются итоговые решения[44].
        </div>

        <img src="''' + url_for('static', filename='pyt.png') + '''">
    </body>
</html>
'''

@app.route("/lab1/romant")
def roma():
    return '''
<!doctype html>
<html>
    <body>
      <div>
      Романти́зм (фр. romantisme) — идейное и художественное направление в европейской и американской культуре 
      конца XVIII века — первой половины XIX века, характеризуется утверждением самоценности духовно-творческой жизни личности
      </div>

      <div>
      Романтизм сменяет эпоху Просвещения и совпадает с промышленной революцией, обозначенной появлением паровой машины, паровоза, парохода, фотографии и фабрично-заводских окраин.
      Если Просвещение характеризует культ разума и основанной на его началах цивилизации
      </div>

      <div>
      Категория возвышенного, центральная для романтизма, сформулирована Кантом в работе «Критика способности суждения». 
      По Канту, есть позитивное наслаждение прекрасным, выражающееся в спокойном созерцании, и есть негативное наслаждение возвышенным, 
      бесформенным, бесконечным, вызывающее не радость, а изумление и осмысление.
      </div>

      <img src="''' + url_for('static', filename='rom.jpg') + '''">
    </body>
</html>
'''