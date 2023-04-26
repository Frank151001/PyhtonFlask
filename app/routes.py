from flask import Flask #From the flask modulo import the flask class



app = Flask(__name__) #create an instance of flask into our variable "app"

@app.get("/")   #We can now use our objects method "get" as a decorator
def index():    #A decorator wraps a functrion (more on this in a bitt)
    me ={       #On line 8, We create a new dictionary with key/Value pairs.
        "first_name":flassk"Francisco",
        "last_name":"Ibarra",
        "hobbies":"Watch movies",
        "is_active": True
    }
    return me   #When you return a dictionary from a view function,
                # flask automatically converts it to JSON for compatibility.