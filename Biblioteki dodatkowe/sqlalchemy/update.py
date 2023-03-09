from main import User, Session, engine

local_session=Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username=="Jan").first()

user_to_update.username = "Adam"
user_to_update.email = "Adam@Kowalski.pl"

local_session.commit()