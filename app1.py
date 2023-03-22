from flask import Flask,render_template,request
app = Flask(__name__)
def controlla():
    nm=request.form["nm"]
    cm=request.form["cm"]
    nazione=request.form["nazione"]
    usnm=request.form["usnm"]
    pas=request.form["pas"]
    conpas=request.form["conpas"]
    mail=request.form["mail"]
    try:
        lingua=request.form["lingua"]
        accetto=request.form["accetto"]
    except:
        return False
    if nm!="" and cm!="" and usnm!="" and pas!="" and pas==conpas and mail.find("@")and accetto!="":
        return True
    else:
        return False

@app.route('/', methods=['GET'])
def tour():
  return render_template("home.html")

@app.route('/login', methods=['POST'])
def login():
  if controlla():
    return render_template("ok.html",testo="benvenuto/a")
  else:
    return render_template("ok.html",testo="errore controlla i parametri")  
 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)