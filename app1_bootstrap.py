from flask import Flask,render_template,request
app = Flask(__name__)
def controlla(a,b,c,d,e,f,g):
    if a!="" and b!="" and c!="" and d!="" and d==e and f.find("@")and g!="":
        return True
    else:
        return False

@app.route('/', methods=['GET'])
def tour():
  return render_template("NiceAdmin/pages-register copy.html")

@app.route('/login', methods=['POST'])
def login():
    nm=request.form["nm"]
    cm=request.form["cm"]
    nazione=request.form["nazione"]
    usnm=request.form["usnm"]
    pas=request.form["pas"]
    conpas=request.form["conpas"]
    mail=request.form["mail"]
    data=request.form["compleanno"]
    try:
        lingua=request.form["lingua"]
        accetto=request.form["accetto"]
    except:
        return render_template("ok.html",testo="errore controlla i parametri")
  
    if controlla(nm,cm,usnm,pas,conpas,mail,accetto):
        return render_template("ok.html",testo=nm,testo2=cm,testo3=nazione,testo4=usnm,testo5=pas,testo6=conpas,testo7=mail,testo8=lingua,testo9=accetto,testo10=data)
    else:
        return render_template("ok.html",testo="errore controlla i parametri")  
 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)