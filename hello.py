from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("stop.html")
@app.route('/', methods=['POST'])
def my_form_post():
    text = escape(request.form['text'])
    finalouts = dict(text)
    finalout = "<strong>Just copy paste this into excel, ballin chew</strong><br>"
    finalout+= "Reload the page to do other lists...<br><img src=\"data:image/jpeg;base64,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\" height=\"150\"><br>"
    for i in range(len(finalouts)):
        finalout+=finalouts[i] + "<br/>"
    return finalout

def dict(txt):
    tones = [["ā", "á", "ǎ", "à", "a"],["ē", "é", "ě", "è", "e"],["ī", "í", "ǐ", "ì", "i"],["ō", "ó", "ǒ", "ò", "o"],["ū", "ú", "ǔ", "ù", "u"],["","","","","",""]]
    toneDeaf = {"a":0, "e":1, "i":2, "o":3, "u":4}
    inputs = txt.split(" ")
    finalouts = []
    output = []
    for jk in inputs:
      dict = open("cedict_ts.txt", "r")
      i = 1
      while i < 123078:
        line = dict.readline().split(' ')
        i+=1
        if line[1] == jk:
          if len(line[1]) == 1:
            skib = line[2][1:-1]
            output.append(skib)
            break
          skib = line[2][1:]
          for j in range(len(line[1])-2):
            skib += " " + line[j+3]
          skib += " " + line[len(line[1])+1][:-1]
          output.append(skib)
          break
        if i == 123078:
          output.append("NOTFOUND5")
    for i in output: # "ba1 zi4 mei2 yi4 pie3"
      k = i.split(" ") #["ba1", "zi4", "mei2", "yi4", "pie3"]
      lp = ""
      for o in k: # "ba1"
        lowest = 5
        position = -1
        tone = o[-1]
        o = o[:-1]
        if o == "r":
          lp+="r"
          continue
        for p in range(len(o)):
          if o[p] in toneDeaf:
            if toneDeaf[o[p]] < lowest:
              lowest = toneDeaf[o[p]]
              position = p
        o = o[0:position] + tones[lowest][int(tone)-1] + o[position+1:]
        lp += o
      finalouts.append(lp.lower())
    return finalouts
