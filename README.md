# Progamming Language
- Python
- JavaScript (HTML)
# Libraries
- pycaret
- padas
- numpy
- matplotlib
- os
# Features
# Directory Structure

```sh
/termpro-predictPM25
│
├── /clean_data
│   ├── cleandata.py
│   ├── cleaned_data.csv
│   ├── data.py
│   └── pm-data.csv          
├── /pm-data
├── train_pm25.ipynb                               
├── /README.md                  
└── /LICENSE.md                  
```

# Setup

- ติดตั้ง Libraries โดยใช้คำสั่งด้านล่างนี้ใน terminal หรือ command prompt
```sh
pip install pycaret pandas numpy matplotlib os
```
# Usage

- pm data
- อ่านและรวบรวมข้อมูลจากไฟล์ Excel
- รวมข้อมูลทั้งหมด

- clean data
- ลบคอลัมน์ที่มี NaN มากกว่า 50%
- แทนที่ค่า NaN ด้วยค่าเฉลี่ย
- ลบคอลัมน์ที่ไม่จำเป็น
- แทนที่ค่า 0 ด้วยค่าเฉลี่ย
- ลบแถวที่ไม่ต้องการ

- train pm 2.5

# Getting Started
# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
