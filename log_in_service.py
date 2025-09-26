from database import get_connection
import gui


def log_in(username,password):
    db=get_connection()
    corr=db.cursor()

    corr.execute("Select id from users where username=%s and password=%s",[username,password])
    result=corr.fetchone()
    if result:
        db.close()
        corr.close()
        return result[0]
    else:
        db.close()
        corr.close()
        return False




