import sqlite3

class Databaseaccess:
    @staticmethod
    def findUserwithemail(email):
        try:
            conn = sqlite3.connect('db1.db')
            cursor=conn.cursor()
            email=(email,)
            cursor.execute(" SELECT * from Persons where email = ? ",(email))
            row = cursor.fetchone()
            users=[]
            while row:
                users.append(row)
                row = cursor.fetchone()
            cursor.close()
            conn.close()
            return users
        except Exception as e:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            print str(e)
            raise
            