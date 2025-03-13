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
│   ├── cleandata.py            # การทำความสะอาดข้อมูล
│   ├── cleaned_data.csv        # ข้อมูลที่ผ่านการทำความสะอาด
│   ├── data.py                 # จัดการข้อมูล
│   └── pm-data.csv             # ข้อมูลก่อนการทำความสะอาด
├── /pm-data                    # ข้อมูล PM25 ที่ใช้ในการฝึก
├── train_pm25.ipynb            # ฝึกโมเดล PM25
│                          
├── /README.md                  # คำอธิบายโปรเจกต์                
└── /LICENSE.md                 # ระบุลิขสิทธิ์ของโปรเจกต์ 
```

# Setup

- ติดตั้ง Libraries โดยใช้คำสั่งด้านล่างนี้ใน terminal หรือ command prompt
```sh
pip install pycaret pandas numpy matplotlib os
```
# Usage

- pm data
- อ่านและรวบรวมข้อมูลจากไฟล์ Excel

```sh
df_list = []
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)  
    df_list.append(df)
```

- รวมข้อมูลทั้งหมด

```sh
merged_df = pd.concat(df_list, ignore_index=True)
```


- clean data
- ลบคอลัมน์ที่มี NaN มากกว่า 50%

```sh
data.dropna(axis=1, thresh=1, inplace=True)
```

- แทนที่ค่า NaN ด้วยค่าเฉลี่ย

```sh
data['temperature'].fillna(data['temperature'].mean(), inplace=True)
data['pm_2_5'].fillna(data['pm_2_5'].mean(), inplace=True)
```

- ลบคอลัมน์ที่ไม่จำเป็น

```sh
columns_to_drop = ["timezone", "pm_10", "pm_2_5_sp"]
data.drop(columns=columns_to_drop, inplace=True, errors="ignore")
```

- แทนที่ค่า 0 ด้วยค่าเฉลี่ย

```sh
columns_to_handle_zeros = ['humidity', 'pm_2_5', 'temperature']
```

- ลบแถวที่ไม่ต้องการ

```sh
new_data = data.drop(index=range(2000, len(data)))
```


- train pm 2.5

# Getting Started
# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
