from main import User, Session, engine

local_session = Session(bind=engine)

users = local_session.query(User).all()

for user in users:
    print(user.username)

#query with filter
jan = local_session.query(User).filter(User.username == 'Jan').first()
print(jan)