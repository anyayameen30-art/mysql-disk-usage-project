# MySQL Disk Usage Project

## Overview

This project automates the process of collecting **Linux disk usage data
(`df -h`)**, converting it into **CSV format**, and securely inserting
that data into a **MySQL database** using Python.\
It demonstrates **password encryption**, **CSV ingestion**, and
**automated database integration** --- ideal for **DevOps**, **system
monitoring**, or **data pipeline automation**.

------------------------------------------------------------------------

## File Overview

  ----------------------------------------------------------------------------
  File                       Description
  -------------------------- -------------------------------------------------
  **My_Project.py**          Main Python automation script --- reads CSV data,
                             encrypts MySQL credentials, and inserts parsed
                             disk usage information into the database.

  **mylinux.json**           Configuration file containing MySQL login
                             credentials and the Linux command used to extract
                             disk usage data (`df -h`).

  **mycsvfile.csv**          CSV file containing disk usage metrics like
                             filesystem, size, used, available space, and
                             hostname.

  **mysql_credentials.py**   Example script showing how credentials can be
                             defined and securely handled within the project.
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

## Requirements

### Install Dependencies

``` bash
pip install cryptography mysql-connector-python
```

**Modules used:** - `cryptography.Fernet` → for password encryption &
decryption\
- `mysql.connector` → for database connection and data insertion\
- Built-in: `json`, `csv`, `os`

------------------------------------------------------------------------

## Environment Setup

Before running the script:

1.  **Ensure your MySQL server is running and accessible.**\

2.  **Update file paths** in `My_Project.py` to match your local
    environment:

    ``` python
    jsonfile = "/path/to/mylinux.json"
    csvpath = "/path/to/mycsvfile.csv"
    ```

3.  **Create the target MySQL table** using the schema below:

    ``` sql
    CREATE TABLE my_df_data (
        filesystem VARCHAR(255),
        size VARCHAR(50),
        used VARCHAR(50),
        avail VARCHAR(50),
        usage_with_per VARCHAR(10),
        mounted_on VARCHAR(100),
        datetime DATETIME,
        ip_address VARCHAR(50),
        hostname VARCHAR(100)
    );
    ```

------------------------------------------------------------------------

## Usage

### Clone the Repository

``` bash
git clone https://github.com/anyayameen30-art/mysql-disk-usage-project.git
cd mysql-disk-usage-project
```

### Run the Script

``` bash
python3 My_Project.py
```

### Expected Output

    We are fetching MYSQL password and encrypting and decrypting...
    CSV file reading and storing into mysql DB
    Data has been imported into DB successfully

------------------------------------------------------------------------

## Features

-   🔒 Secure password encryption with `cryptography.Fernet`
-   💾 Automatic MySQL data insertion from CSV
-   📊 Real-time Linux disk usage (`df -h`) monitoring
-   🖥️ Compatible with both **macOS** and **Ubuntu**
-   🌐 Captures **IP address** and **hostname** for multi-system
    tracking

------------------------------------------------------------------------

## 🗂️ Directory Structure

    mysql-disk-usage-project/
    ├── My_Project.py           # Main Python script
    ├── mylinux.json            # MySQL credentials + df command
    ├── mycsvfile.csv           # Example disk usage data
    ├── mysql_credentials.py    # Example credentials file
    └── README.md               # Project documentation

------------------------------------------------------------------------

## Example CSV Data

  -------------------------------------------------------------------------------------------------------------
  filesystem       size   used   avail   usage_with_per   mounted_on   datetime     ip_address       hostname
  ---------------- ------ ------ ------- ---------------- ------------ ------------ ---------------- ----------
  /dev/nvme0n1p2   19G    11G    7.2G    60               /            2025-10-24   172.16.248.129   vmone
                                                                       20:15:03                      

  /dev/nvme0n1p1   952M   6.6M   945M    1                /boot/efi    2025-10-24   172.16.248.129   vmone
                                                                       20:05:10                      
  -------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Author

**Anya Yameen**\

------------------------------------------------------------------------

## 🪪 License

This project is licensed under the **MIT License**.\
You are free to modify, distribute, or use it for personal and
educational purposes.
