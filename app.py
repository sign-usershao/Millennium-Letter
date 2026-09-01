from flask import Flask,render_template,request,session

import json

from dialogue import get_reply

from memory import add_memory,get_recent_memory


app=Flask(__name__)

app.secret_key="libai"


@app.route("/")
def index():

    return render_template(
        "index.html"
    )



@app.route("/choose",methods=["POST"])
def choose():

    choice=request.form["character"]

    session["character"]=choice


    return render_template(
        "chat.html",
        character=choice
    )



@app.route("/chat",methods=["POST"])
def chat():

    question=request.form["message"]


    character=session.get(
        "character"
    )


    if character=="young":

        filename="characters/libai_young.json"


    elif character=="changan":

        filename="characters/libai_changan.json"


    else:

        filename="characters/libai_old.json"



    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        libai=json.load(file)



    history=get_recent_memory()


    reply=get_reply(
        question,
        libai,
        history
    )


    add_memory(
        question,
        reply
    )


    return render_template(
    "chat.html",
    question=question,
    reply=reply,
    character=character
    )



if __name__=="__main__":

    app.run(
        debug=True
    )


