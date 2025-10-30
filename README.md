# MySQL Disk Usage Project

A Python-based automation tool that collects Linux disk usage metrics
and logs them into a MySQL database for monitoring and analysis.

------------------------------------------------------------------------

## Overview

This project automates the process of collecting Linux disk usage data
(`df -h`), converting it into CSV format, and securely inserting that
data into a MySQL database using Python.\
It demonstrates password encryption, CSV ingestion, and automated
database integration --- ideal for DevOps, system monitoring, or data
pipeline automation.

------------------------------------------------------------------------

## File Purpose

-   `My_Project.py` --- Main automation script that reads disk usage CSV
    data, encrypts MySQL credentials, and inserts data into the
    database.\
-   `mylinux.json` --- Configuration file containing MySQL credentials
    and the Linux command used to collect disk usage data.\
-   `mycsvfile.csv` --- Example CSV file with disk usage details
    including filesystem, size, used, available space, mount point, IP,
    and hostname.\
-   `mysql_credentials.py` --- Demonstrates how credentials can be
    securely handled within the project.

------------------------------------------------------------------------

## Requirements

### Install Dependencies

``` bash
pip install cryptography mysql-connector-python
```

**Libraries used:** - cryptography.Fernet --- for encrypting and
decrypting passwords\
- mysql.connector --- for MySQL database operations\
- json, csv, os --- standard Python modules

------------------------------------------------------------------------

## Environment Setup

Before running the script:

1.  Ensure your MySQL server is up and running.\

2.  Update file paths in `My_Project.py` to match your environment:

    ``` python
    jsonfile = "/path/to/mylinux.json"
    csvpath = "/path/to/mycsvfile.csv"
    ```

3.  Create the MySQL table using the schema below:

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

## Try It Yourself

1.  Run `df -h` on your Linux or Ubuntu system.\
2.  Copy the output into a CSV file following the same format as
    `mycsvfile.csv`.\
3.  Edit `mylinux.json` with your own MySQL credentials.\
4.  Run `python3 My_Project.py` and verify that the data is successfully
    inserted into your MySQL table.

------------------------------------------------------------------------

## Key Features

-   Secure password encryption using cryptography.Fernet\
-   Automated MySQL data insertion from CSV files\
-   Real-time Linux disk usage monitoring via `df -h`\
-   Cross-platform support (macOS & Ubuntu)\
-   Tracks both IP address and hostname for multiple servers

------------------------------------------------------------------------

## Directory Structure

    mysql-disk-usage-project/
    ├── My_Project.py           # Main automation script
    ├── mylinux.json            # MySQL credentials + df command
    ├── mycsvfile.csv           # Disk usage data file
    ├── mysql_credentials.py    # Credentials handling example
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

## Author & License

**Author:** Anya Yameen\
*DevOps \| Python \| Automation \| Scripting*\
GitHub: [anyayameen30-art](https://github.com/anyayameen30-art)

**License:** MIT --- Free to use, modify, and share for personal or
educational purposes.



