# 京都大学学生証 学籍番号と名前（半角カナ）を返す
import binascii
import nfc
import time
import datetime
def on_connect_nfc(tag):
    try:
        servc = 0x1A8B
        service_code = [nfc.tag.tt3.ServiceCode(servc >> 6, servc & 0x3F)]
        print(tag.dump()) # これがないと何故かうまくいかなかった
        bc_id = [nfc.tag.tt3.BlockCode(0)]
        bd_id = tag.read_without_encryption(service_code, bc_id)
        student_id = int(bd_id[2:-3].decode("utf-8"))
        bc_name = [nfc.tag.tt3.BlockCode(1)]
        student_name = (
        tag.read_without_encryption(service_code, bc_name)
        .decode("shift-jis")
        .rstrip("\x00")
        )
        #return student_id, student_name
        dt_now = datetime.datetime.now()
        print(dt_now.strftime('%H:%M'))
        print(student_id, student_name)
        return student_id, student_name, dt_now.strftime('%H:%M')
    except Exception as e:
        print("error: %s" % e)
def main():
  clf = nfc.ContactlessFrontend('usb')
  while True:
    print(clf.connect(rdwr={'on-connect': on_connect_nfc}))
    time.sleep(3)
  
if __name__ == "__main__":
  main()
