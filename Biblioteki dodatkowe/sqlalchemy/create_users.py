from main import User, Session, engine

local_session = Session(bind = engine) #create session in bind database, engine is variable defined in main

new_user = User(username = "Jan", email = "Jan@Kowalski.pl") #define user

local_session.add(new_user) #add user to session
local_session.commit() #commit operations


#add multiple users
users = [{
        "username":"Anna","email" : "anna@sgh.waw.pl"
    },{
        "username":"Kasia","email" : "kasia@sgh.waw.pl"
    }]

for u in users:
    new_user = User(username = u['username'], email = u['email'])
    print(new_user)
    local_session.add(new_user)
    local_session.commit()
    print(f"Added {u['username']}")