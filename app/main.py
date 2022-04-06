from flask import Flask, request, abort

from pymongo import MongoClient

import management

import spartan

from management import all_spartan_dictionary





while True:
    try:
        client = MongoClient("mongodb://db.abishake.devops106:27017")
        break
    except Exception as e:
        print("Trying to create a connection to the database")
        time.sleep(2)

db = client.spartans
flask_object = Flask(__name__)
# GET for homepage
@flask_object.route("/", methods=["GET"])

def home_page():
    with open("log/user_action.txt", "a+") as user_action_file:
        user_action_file.write("User accessed the Home Page\n")
    return """Welcome to Sparta Global's Employee Management System
    Use the following APIs to navigate through web application:
    /spartan/add : To Add a Spartan
    /spartan/<spartan_id> : To View a Spartan, by Spartan ID
    /spartan/remove?id=<spartan_id> : To Remove a Spartan
    /spartan : To View All Spartans"""

# POST for add spartan
@flask_object.route("/spartan/add", methods=["POST"])

def spartan_add():
    with open("log/user_action.txt", "a+") as user_action_file:
        user_action_file.write("User wants to add a Spartan to the database\n")

    spartan_file = request.json
    spartan_id = spartan_file["spartan_id"]
    first_name = spartan_file["first_name"]
    last_name = spartan_file["last_name"]
    birth_day = spartan_file["birth_day"]
    birth_month = spartan_file["birth_month"]
    birth_year = spartan_file["birth_year"]
    course = spartan_file["course"]
    stream = spartan_file["stream"]

    spartan_object = spartan.Spartan(spartan_id, first_name, last_name, birth_day, birth_month, birth_year,
                                     course, stream)

    #spartan_object.print_spartan_data()

    all_spartan_dictionary[spartan_id] = spartan_object

    spartan_dict = spartan_object.__dict__

    record =db.spartan_data.insert_one(spartan_dict)
    print(record)

    with open("log/user_action.txt", "a+") as user_action_file:
        user_action_file.write(f"User successfully added a Spartan, {first_name} {last_name}, with Spartan ID: {spartan_id}, to the database\n")

    return f"The Spartan, {first_name} {last_name}, with Spartan ID: {spartan_id} will be added to the database."

# GET for to view certain spartan
@flask_object.route("/spartan/<spartan_id>", methods=["GET"])

def spartan_file_getter(spartan_id):
    with open("log/user_action.txt", "a+") as user_action_file:
        user_action_file.write("User wants to view a Spartan from the database\n")
    record =db.spartan_data.find_one({"spartan_id": int(spartan_id)})


    with open("log/user_action.txt", "a+") as user_action_file:
        user_action_file.write(f"User viewed the details of a Spartan, with Spartan ID {spartan_id}, from the database\n")
    return f"{record}"


# POST to remove spartan
@flask_object.route("/spartan/remove", methods=["POST"])

def spartan_file_remover():
    with open("log/user_action.txt", "a+") as user_action_file:
        user_action_file.write("User wants to remove a Spartan from the database\n")

    spartan_id = request.args.get("id")
    record =db.spartan_data.delete_one({"spartan_id": int(spartan_id)})

    with open("log/user_action.txt", "a+") as user_action_file:
        user_action_file.write(f"User removed the details of a Spartan, with Spartan ID {spartan_id}, from the database\n")
    return f"The Spartan, with Spartan ID: {spartan_id}, has been successfully removed from the system"

# GET to view spartan list
@flask_object.route("/spartan", methods=["GET"])

def all_spartan_file_getter():
    with open("log/user_action.txt", "a+") as user_action_file:
        user_action_file.write("User viewed all Spartans from the database\n")

    records =db.spartan_data.find()
    list = []

    for record in records:
        list.append(record)

    return f"{list}"



if __name__ == "__main__":

    flask_object.run(port = 8080, host = "0.0.0.0")
