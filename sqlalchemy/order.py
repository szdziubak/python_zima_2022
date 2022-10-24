from main import Session, engine, User

local_session = Session(bind=engine)

users = local_session.query(User).order_by(User.username.asc()).all()
print("Ascending:")
for user in users:
    print(user.username)


users_desc = local_session.query(User).order_by(User.username.desc()).all()
print("Descending:")
for user in users_desc:
    print(user.username)
