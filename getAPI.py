import requests
import json
import datetime
# ดึงข้อมูลเบียร์จาก API
def extract_brewery_data(per_page= 10) :
    url =f"https://api.openbrewerydb.org/v1/breweries?per_page={per_page}"
# ใช้try เพื่อจัดการกับข้อผิดพลาดที่อาจเกิดขึ้น
    try : 
        print( f"กำลังดึงข้อมูลเบียร์จาก API: {per_page}รายการต่อหน้า" )
        response = requests.get(url)
        
        response.raise_for_status()  # ตรวจสอบว่าการตอบกลับเป็นสำเร็จหรือไม่
        
        data = response.json()  # แปลงข้อมูลจาก JSON เป็น Python dict
        print("ดึงข้อมูลสำเร็จ")
        return data
    
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการดึงข้อมูล: {e}")
        return None
    
# สร้างฟังชัน เพื่อ save ข้อมูลลงไฟล์ JSON
def save_raw_data(data_to_save, filename):
    if data_to_save != None:# เช็คก่อนว่ามีข้อมูลให้เซฟไหม 
        # เปิดไฟล์ขึ้นมาในโหมด "w" (Write = เขียนทับ)
        with open(filename, "w",encoding="utf-8") as file:
            # เอาข้อมูล Python ยัดกลับเป็นโครงสร้าง JSON แล้วเซฟลงไฟล์
            json.dump(data_to_save, file, indent=4, ensure_ascii=False)
        print(f"ข้อมูลถูกบันทึกลงไฟล์ {filename} เรียบร้อยแล้ว")
    else :
        print("ไม่มีข้อมูลให้บันทึก")
#ส่วนที่ 3: สั่งให้โปรแกรมเริ่มทำงานจริง (ผู้จัดการสั่งงาน)

if __name__ == "__main__":
    raw_data = extract_brewery_data(per_page=5)  # ดึงข้อมูลเบียร์จาก API

   # สร้างชื่อไฟล์โดยเอา "วันที่และเวลาปัจจุบัน"
    today_date = datetime.datetime.now().strftime("%y%m%d") 
    file_name = f"raw_brewery_data_{today_date}.json"  # ชื่อไฟล์ที่ต้องการบันทึก

    # save file
    save_raw_data(raw_data,filename=file_name)