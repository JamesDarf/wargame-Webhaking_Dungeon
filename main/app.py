
from flask import Flask, send_from_directory, request, render_template, render_template_string, redirect, url_for
import re

app = Flask(__name__)
app.config.from_pyfile('config.py')

DATABASE = "{e.g}.db"

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"

# main_page
@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")


# About
@app.route("/about", methods = ["GET", "POST"])
def about():
    return render_template("about.html")


# # Stage1
# @app.route("/stage1", methods = ["GET", "POST"])
# def hawam():
#     input_1 = ""
#     if request.method == "POST":
#         input_1 = request.form['input_1']
#         # return input_1
#         m = re.match(r'i\d+like\d+icepork\d+205', input_1) # i12like12icepork12205
#         if m:
#             return redirect('/stage2')
#         else:
#             return render_template("stage1.html", input_1="NOPE!")
#     elif request.method == "GET":
#         return render_template("stage1.html")


# # Stage2
# @app.route("/stage2", methods = ["POST"])
# def AutomaticCity():
#     input_1 = ""
#     if request.method == "POST":
#         input_1 = request.form['input_1']
#         m = re.match(r'st2key205', input_1) # st2key205
#         if m:
#             return redirect('/stage3')
#         else:
#             return render_template("stage2.html", input_1="NOPE!")
#     elif request.method == "GET":
#         return render_template("stage2.html")
    

# # Stage3
# @app.route("/stage3", methods = ["POST"])
# def sweet_kingdom():
#     ssti = request.args.get('ssti', '')
#     html = '''
#     <div class="center">
#         <h1>Page Not Found.</h1>
#         <h3>%s</h3>
#     </div>
#     ''' %ssti
#     return render_template_string(html, ssti=ssti)

# ==================== prototype1


# Stage1
@app.route("/stage1", methods = ["GET", "POST"])
def sweet_kingdom():
    f = open("templates/stage_1.html", 'r')
    html = f.read()
    ssti = request.args.get('ssti', '')
    if request.method == "POST":
        input_1 = request.form['input_1']
        m = re.match('key1', input_1) # 
        if m:
            return render_template("stage_2.html", input_1="NOPE!")
        else:
              return render_template_string(html.format(ssti))
    elif request.method == "GET":
        return render_template_string(html.format(ssti))
    

# Stage2
@app.route("/stage2", methods = ["POST"])
def AutomaticCity():
    input_1 = ""
    if request.method == "POST":
        input_1 = request.form['input_1']
        m = re.match(r'st2key205', input_1) # st2key205
        if m:
            return render_template("stage_3.html", input_1="NOPE!")
        else:
            return render_template("stage_2.html", input_1="NOPE!")

# Stage3
@app.route("/stage3", methods = ["POST"])
def hawam():
    input_1 = ""
    if request.method == "POST":
        input_1 = request.form['input_1']
        # return input_1
        m = re.match(r'i\d+like\d+icepork\d+205', input_1) # i12like12icepork12205
        if m:
            return render_template("stage_3.html", input_1=FLAG)
        else:
            return render_template("stage_3.html", input_1="NOPE!")


# robots.txt
@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


