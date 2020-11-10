from flask import Flask, request, Response
import mariadb
import json
import random

app = Flask(__name__)

animals = ["cat", "dog", "monkey", "chimpanzee", "walrus", "goat", "sheep", "lama",
 "lion", "tiger", "crow", "eagle", "crocadile", "aligator", "elephant", "zebra", "toad",
 "wolf"
]

@app.route('/animallist', methods=["GET", "POST", "PATCH", "DELETE"])
def listofanimals():
    if request.method == "GET":
        random_animal_list = []
        for animal in animals:
            random_number = random.randrange(0,17)
            random_animal = animals[random_number]
            random_animal_list.append(random_animal)
        animal = {"animal":random_animal_list}
        return Response(json.dumps( animal, default=str), mimetype ="application/json", status=200)
    
    elif request.method == "POST":
        newanimal = "snake"
        animals.append(newanimal)
        return Response("You have added a snake", mimetype ="text/html", status=201 )
    
     
    elif request.method == "PATCH":
        animals[2] == "big monkey"
        return Response("You have updated the monkey to a bigger monkey", mimetype ="text/html", status=201 )
    
    elif request.method == "DELETE":
        animals.remove("zebra")
        return Response("You have deleted the zebra from your array", mimetype ="text/html", status=201 )


