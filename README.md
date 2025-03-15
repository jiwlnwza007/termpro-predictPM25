# PM2.5 And Hudimity Prediction Dashboard
การพยากรณ์ค่าความเข้มของฝุ่นละอองขนาดเล็ก (PM2.5) และค่าความชื้น โดยใช้ระบบการแสดงผลข้อมูล (Dashboard) สามารถแสดงผลคุณภาพอากาศสำหรับ 7 วันข้างหน้า จากข้อมูลในอดีตและโมเดลที่ได้รับการฝึกมาแล้ว เพื่อให้ผู้คนสามารถติดตาม ตรวจสอบและวางแผนเกี่ยวกับการป้องกันฝุ่นละอองและการดูแลสุขภาพล่วงหน้าได้

# Progamming Language
- Python พัฒนาโมเดลและจัดการข้อมูล
- JavaScript (HTML) สร้าง UI สำหรับการแสดงผลข้อมูล (Dashboard)

# Libraries
- pycaret พัฒนา เปรียบเทียบ ทดสอบโมเดล และเลือกโมเดลที่ดีที่สุด 
- padas จัดการและวิเคราะห์ข้อมูลในรูปแบบ DataFrame
- numpy คำนวณทางคณิตศาสตร์และจัดการอาเรย์
- matplotlib สร้างกราฟและภาพข้อมูล
- os อ่านและเขียนไฟล์ จัดการโฟลเดอร์

# Features
1.หน้าเว็บ
- แสดงลิงค์ไปยังหน้าอื่นๆ
- แสดงภาพและข้อความต้อนรับ

2.กราฟพยากรณ์ค่าความเข้มของฝุ่นละอองขนาดเล็ก (PM2.5) สำหรับ 7 วันข้างหน้า
- โหลดโมเดลที่ฝึกแล้วและแสดงผลลัพธ์การพยากรณ์ในรูปแบบ กราฟเส้น ด้วย Plotly

3.กราฟพยากรณ์ค่าความชื้น สำหรับ 7 วันข้างหน้า
- โหลดโมเดลที่ฝึกแล้วและแสดงผลลัพธ์การพยากรณ์ในรูปแบบ กราฟเส้น ด้วย Plotly

4.ข้อมูลรวม
- แสดงข้อมูลจากไฟล์ CSV ที่ได้รับการทำความสะอาดแล้วในรูปแบบตาราง โดยใช้ Dash DataTable

5.กราฟค่าความเข้มของฝุ่นละอองขนาดเล็ก (PM2.5) และความชื้นตามช่วงเวลา
- ใช้ DatePickerRange ในการเลือกช่วงเวลาและแสดงกราฟ PM2.5 หรือความชื้นในช่วงเวลานั้นๆ

6.การเชื่อมโยงหน้า
- สามารถเลือกดูข้อมูลต่างๆ ผ่านลิงค์ที่แสดงในหน้าแรก โดยใช้ dcc.Location และ dcc.Link เพื่อการนำทางระหว่างหน้า

7.การใช้งานโมเดลที่ฝึกแล้ว
- โมเดลที่ฝึกแล้วจะถูกบันทึกด้วย pickle และโหลดมาพยากรณ์ค่า PM2.5 และความชื้น

8.สไตล์และการออกแบบ
- ปรับแต่งรูปแบบการแสดงผล เช่น สี, ขนาด และรูปแบบของตารางหรือกราฟ โดยการใช้ CSS

# Directory Structure

```sh
/termpro-predictPM25
│
├── /assets
│   ├── carmeme.jpg             # รูปภาพที่ใช้ในหน้าแรกของแดชบอร์ด
│
├── /clean_data                     
│   ├── cleandata.py            # การทำความสะอาดข้อมูล
│   ├── cleaned_data.csv        # ข้อมูลที่ผ่านการทำความสะอาด
│   ├── data.py                 # จัดการข้อมูล
│   └── pm-data.csv             # ข้อมูลก่อนการทำความสะอาด
│
├── /pm-data                    # ข้อมูล PM25 ที่ใช้ในการฝึก
│
├── app.py                      # แอป Dash
├── styles.css                  # ตกแต่งแดชบอร์ด
├── train_humidity.ipynb        # ฝึกโมเดลความชื้น
├── train_pm25.ipynb            # ฝึกโมเดล PM2.5
│                          
├── README.md                  # คำอธิบายโปรเจกต์                
└── LICENSE.md                 # ระบุลิขสิทธิ์ของโปรเจกต์ 
```

# Setup

- ติดตั้ง Libraries โดยใช้คำสั่งด้านล่างนี้ใน terminal หรือ command prompt
```sh
pip install pycaret pandas numpy matplotlib os
```
# Usage

1.การจัดการข้อมูล (Data Handling)
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
2.การฝึกฝนโมเดล (Model Training)
- เตรียมข้อมูล

```sh
pm_data = pd.read_csv("clean_data\\cleaned_data.csv")
pm_data["timestamp"] = pd.to_datetime(pm_data["timestamp"])
print(pm_data)
```

- เปรียบเทียบโมเดล

```sh
best = compare_models()

```

- เลือกโมเดลที่ดีที่สุด

```sh
ensem_best_model = ensemble_model(best_model_tune, n_estimators = 50)
```

- ทดสอบโมเดล


```sh
predict = predict_model(ensem_best_model, data=next_data)
data_plot = pd.DataFrame(predict, columns=['timestamp', 'prediction_label'])
data_plot["prediction_label"] = data_plot["prediction_label"].round(2)
data_plot
```

3.สร้างกราฟและแสดงผล (Visualization)

```sh
plt.plot(next_week, predict['prediction_label'])
plt.xlabel('Date')
plt.ylabel('PM2.5')
plt.title('PM2.5 IN NEXT 7 DAYS')
plt.grid(True)
plt.show()
```

```sh
plt.plot(next_week, predict['prediction_label'])
plt.xlabel('Date')
plt.ylabel('Humidity')
plt.title('Humidity IN NEXT 7 DAYS')
plt.grid(True)
plt.show()
```

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
