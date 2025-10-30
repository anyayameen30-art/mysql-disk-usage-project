import json
from  cryptography.fernet import Fernet
import mysql.connector
import csv

try:
    jsonfile="/Users/anyareyan/PycharmProjects/PythonProject2/mylinux.json"
    csvpath="/Users/anyareyan/PycharmProjects/PythonProject2/mycsvfile.csv"
    with open(jsonfile) as jf:
        print("We are fetching MYSQL password and encrypting and decrypting...")
        my_dict = json.load(jf)
        username_mysql = (my_dict['username'])
        password_mysql = (my_dict['password'])

        message = password_mysql.encode("utf-8")
        key = Fernet.generate_key()
        f_key = Fernet(key)
        encrypt = f_key.encrypt(message)

        decrypt= f_key.decrypt(encrypt)
        passwd_mysql = decrypt.decode('utf-8')

        mydb = mysql.connector.connect (
        host = "172.16.248.129",
        user= "mysql_user",
        password = passwd_mysql,
        database = "alnafi"
        )

    print("CSV file reading and storing into mysql DB")
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        all_rows = []
        for row in csvreader:
            value=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            all_rows.append(value)
    query = "insert into my_df_data (filesystem,size,used,avail,usage_with_per,mounted_on,datetime,ip_address,hostname) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor = mydb.cursor()
    mycursor.executemany(query,all_rows)
    mydb.commit()
    mydb.close()
    print("Data has been imported into DB successfully")
except Exception as e:
    print("Something is casuing an issue ", e)

