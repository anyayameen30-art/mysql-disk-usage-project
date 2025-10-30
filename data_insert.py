try:
    import mysql.connector
    from datetime import *


    #User Input
    user_input = input("Enter the fname which you want to remove from mysql database: ")
    user_input = user_input.lower()
    #adding custom date/time
    time=datetime.now()
    custom_date=time.strftime("%Y-%m-%d %I:%M:%S")

    from datetime import *
    mydb=mysql.connector.connect(host="172.16.248.128",user="mysql_user",passwd="test123",database="alnafi")

    #Converting mydb into an object
    cursor=mydb.cursor()

    #Passing a command
    data="'zoyahala45@gmail.com'"
    sql = (f"delete from trainer_details where fname='{user_input}'")
    cursor.execute(sql)
    mydb.commit()

    #Executing a command
    cursor.execute(sql)
    mydb.commit() #this will save the data in the mysql

    #Fetching mysql data
    select_sql="select * from trainer_details where t_id=7"
    cursor.execute(select_sql)
    result = cursor.fetchall()

    for data in result:
        print(data)

    mydb.close()
except Exception as e:
    print("Make sure the input is entered correctly", e)