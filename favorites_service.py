import user_page
import favorites_page
from database import get_connection



def add_product(name,barcode,brand,ingredients):
    
    try:
    
        db=get_connection()
        curr=db.cursor()
        curr.execute("select id from products where name=%s and barcode=%s and brand=%s and ingredients=%s",[name,barcode,brand,ingredients])
        result = curr.fetchall()
        if result:
            curr.close()
            db.close()
            return False
        
        
        else:
            curr.execute("insert into products (name,barcode,brand,ingredients) values(%s,%s,%s,%s)",[name,barcode,brand,ingredients])
            product_id=curr.lastrowid
            db.commit()
            curr.close()
            db.close()
            return product_id
        

    except Exception as e:
        print(f"Error adding to products: {e}")
        return False
    
    finally:
        if db.is_connected():
            curr.close()
            db.close()



def add_ai_analyz(product_id,health_score,comment,category,suggestion):
        try:
        
            db=get_connection()
            curr=db.cursor()
            curr.execute("select id from ai_analysis where product_id=%s and health_score=%s and comment=%s and category=%s and suggestion=%s",[product_id,health_score,comment,category,suggestion])
            result = curr.fetchall()
            if result:
                curr.close()
                db.close()
                return False
            
            
            else:
                curr.execute("insert into ai_analysis (product_id,health_score,comment,category,suggestion) values(%s,%s,%s,%s,%s)",[product_id,health_score,comment,category,suggestion])
                ai_analyz_id=curr.lastrowid
                db.commit()
                curr.close()
                db.close()
                return ai_analyz_id
            

        except Exception as e:
            print(f"Error adding to ai_analysis: {e}")
            return False
        
        finally:
            if db.is_connected():
                curr.close()
                db.close()


def add_favorites(user_id,product_id,ai_analyz_id):
    try:
        db=get_connection()
        curr=db.cursor()
        curr.execute("select id from favorites where user_id=%s and product_id=%s and ai_analyz_id=%s",[user_id,product_id,ai_analyz_id])
        result=curr.fetchall()
        if result:
            curr.close()
            db.close()
            return False
        else:
            curr.execute("insert into favorites (user_id,product_id,ai_analyz_id) values(%s,%s,%s)",[user_id,product_id,ai_analyz_id])
            db.commit()
            curr.close()
            db.close()
            return True
        

    except Exception as e:
            print(f"Error adding to favorites: {e}")
            return False
        
    finally:
            if db.is_connected():
                curr.close()
                db.close()
