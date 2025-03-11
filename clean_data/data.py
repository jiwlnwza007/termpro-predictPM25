import os
import pandas as pd

# กำหนด path ของโฟลเดอร์ที่มีไฟล์ Excel
folder_path = "d://7//66-psu//year2//semester2//ba ai//termpro-predictPM25//pm-data"
output_file = "d://7//66-psu//year2//semester2//ba ai//termpro-predictPM25//data//pm-data.csv"

# ค้นหาไฟล์ Excel ทั้งหมดในโฟลเดอร์
excel_files = [f for f in os.listdir(folder_path) if f.endswith((".xlsx", ".xls"))]

# อ่านและรวมข้อมูล
df_list = []
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)  # อ่านไฟล์ Excel
    df_list.append(df)

# รวมข้อมูลทั้งหมด
merged_df = pd.concat(df_list, ignore_index=True)

# บันทึกเป็นไฟล์ CSV
merged_df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"รวมไฟล์เสร็จสิ้น ไฟล์ถูกบันทึกที่: {output_file}")
