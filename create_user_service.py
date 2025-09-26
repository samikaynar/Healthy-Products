from database import get_connection
import create_username_gui




def create_user(username,password):
    db=get_connection()
    curr=db.cursor()

    curr.execute("select id from users where username=%s",[username])
    result = curr.fetchone()

    if result :
        curr.close()
        db.close()
        return False
    
    else:
        curr.execute("Insert into users (username, password) value(%s,%s)",[username,password])
        db.commit()

        curr.close()
        db.close()
        return True