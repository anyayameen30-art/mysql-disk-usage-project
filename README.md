# MySQL Disk Usage Project

## Overview

This project automates the process of collecting Linux disk usage data
(`df -h`), converting it into CSV format, and securely inserting that
data into a MySQL database using Python.\
It demonstrates encryption of credentials, automated CSV ingestion, and
database integration --- ideal for DevOps or monitoring pipelines.

------------------------------------------------------------------------

## File Overview

  ----------------------------------------------------------------------------
  File                       Description
  -------------------------- -------------------------------------------------
  **My_Project.py**          Main automation script that reads CSV data,
                             encrypts MySQL credentials, and inserts the
                             parsed disk usage information into a database.

  **mylinux.json**           Configuration file containing MySQL login details
                             and the Linux command used to extract disk usage
                             data (`df -h`).

  **mycsvfile.csv**          Generated CSV file containing disk usage metrics
                             such as filesystem, used space, available space,
                             and host information.

  **mysql_credentials.py**   Example script showing how credentials can be
                             defined and imported securely.
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

## Requirements

### Install Dependencies

``` bash
pip install cryptography mysql-connector-python
```

This script uses: - `cryptography.Fernet` for encryption/decryption of
passwords\
- `mysql.connector` for database connection and insertion\
- Built-in modules: `json`, `csv`, and `os`

------------------------------------------------------------------------

## Environment Setup

Before running the script: 1. Ensure your MySQL server is running and
accessible.\
2. Update file paths in `My_Project.py` to match your environment:
`python    jsonfile = "/path/to/mylinux.json"    csvpath = "/path/to/mycsvfile.csv"`
3. Confirm that your MySQL table structure matches this schema:
`sql    CREATE TABLE my_df_data (        filesystem VARCHAR(255),        size VARCHAR(50),        used VARCHAR(50),        avail VARCHAR(50),        usage_with_per VARCHAR(10),        mounted_on VARCHAR(100),        datetime DATETIME,        ip_address VARCHAR(50),        hostname VARCHAR(100)    );`

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

- **Secure password encryption** using `cryptography.Fernet`\
- **Automated MySQL insertion** of CSV rows\
- **Disk monitoring** based on real-time Linux `df -h` output\
- **Cross-platform tested** on macOS and Ubuntu environments\
- **Supports IP and hostname tracking** for multiple servers

------------------------------------------------------------------------

## Directory Structure

    mysql-disk-usage-project/
    ├── My_Project.py           # Main Python script
    ├── mylinux.json            # MySQL credentials + df command
    ├── mycsvfile.csv           # Example disk usage data
    ├── mysql_credentials.py    # Example credentials file
    └── README.md               # Documentation

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
DevOps \| Python \| Automation \| Scripting\
GitHub: [anyayameen30-art](https://github.com/anyayameen30-art)

------------------------------------------------------------------------

## License

This project is licensed under the **MIT License**.\
You are free to modify, distribute, or use it for personal and
educational purposes.
