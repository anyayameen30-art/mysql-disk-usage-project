import json
from cryptography.fernet import Fernet
import mysql.connector
import csv

jsonfile = "/Users/anyareyan/PycharmProjects/PythonProject2/mylinux.json"
csvpath  = "/Users/anyareyan/PycharmProjects/PythonProject2/mycsvfile.csv"

try:
    with open(jsonfile, "r", encoding="utf-8") as jf:
        print("We are fetching MYSQL password and encrypting and decrypting...")
        my_dict = json.load(jf)
        username_mysql = my_dict["username"]
        password_mysql = my_dict["password"]
        message = password_mysql.encode("utf-8")
        key = Fernet.generate_key()
        f_key = Fernet(key)
        encrypt = f_key.encrypt(message)
        decrypt = f_key.decrypt(encrypt)
        passwd_mysql = decrypt.decode("utf-8")

    # --- connect DB ---
    mydb = mysql.connector.connect(
        host="172.16.248.129",
        user="mysql_user",
        password=passwd_mysql,
        database="alnafi",
    )

    print("CSV file reading and storing into mysql DB")
    all_values = []

    # utf-8-sig eats BOM if present; newline='' lets csv handle newlines correctly
    with open(csvpath, "r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")

        for lineno, row in enumerate(reader, start=1):
            # Skip empty/whitespace-only lines
            if not row or all(cell.strip() == "" for cell in row):
                continue

            # Trim whitespace from each field
            row = [cell.strip() for cell in row]

            # Enforce exactly 9 columns; log and skip malformed lines
            if len(row) != 9:
                print(f"Skipping line {lineno}: expected 9 columns, found {len(row)} -> {row}")
                continue

            # Build tuple in the order your INSERT expects
            value = (
                row[0], row[1], row[2], row[3], row[4],
                row[5], row[6], row[7], row[8]
            )
            all_values.append(value)

    if not all_values:
        raise RuntimeError("No valid rows found in CSV after validation.")

    query = (
        "INSERT INTO my_df_data "
        "(filesystem,size,used,avail,usage_with_per,mounted_on,datetime,ip_address,hostname) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    )

    with mydb.cursor() as cur:
        cur.executemany(query, all_values)
    mydb.commit()
    print(f"Data has been imported into DB successfully ({len(all_values)} rows).")

except Exception as e:
    print("Something is causing an issue:", e)

finally:
    try:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
    except Exception:
        pass
