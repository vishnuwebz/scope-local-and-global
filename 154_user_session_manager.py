# 3 user session manager

# simulate user session with local scope
def create_session(user_id):
    session = {"user_id":user_id, "active": True} # local
    def end_session():
        session["active"] = False
        return session
    return end_session

session = create_session(1)
print(session())
# {'user_id': 1, 'active': False}

# uses local scope to manage user session, common in web apps.