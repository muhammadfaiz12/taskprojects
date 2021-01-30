#logic
def show_all_day(db):
    cursor = db.get_db().cursor()
    query = "select name, allowed_hours from days;"

    cursor.execute(query)
    query_result = cursor.fetchall()
    # [
    #     [monday, 12],
    #     [tuesday, 8]
    # ]
    res = []
    for row in query_result:
        temp = {
            "day_name": row[0],
            "allowed_hours": row[1]
        }
        res.append(temp)
    cursor.close()
    return res

def insert_day(db, day, allowed_hours):
    cursor = db.get_db().cursor()
    query = "INSERT into days(name, allowed_hours) values('{0}', {1});".format(day, allowed_hours)
    print(query)

    cursor.execute(query)
    db.get_db().commit()
    return 
    