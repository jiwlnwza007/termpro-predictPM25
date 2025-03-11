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
  
  ```sh
  df_list = []
  for file in excel_files:
      file_path = os.path.join(folder_path, file)
      df = pd.read_excel(file_path)  
      df_list.append(df)
  ```

- clean data
  - ลบคอลัมน์ที่มี NaN มากกว่า 50%

  ```sh
  data.dropna(axis=1, thresh=1, inplace=True)
  ```

# Getting Started
# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
