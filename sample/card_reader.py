import binascii
import nfc
import time

# 学生証のサービスコード
service_code = 0x200B

def on_connect_nfc(tag):
  # タグのIDなどを出力する
  # print tag
  
  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
        sc = nfc.tag.tt3.ServiceCode(service_code >> 6 ,service_code & 0x3f)
        bc1 = nfc.tag.tt3.BlockCode(0, service=0)
        bc2 = nfc.tag.tt3.BlockCode(1, service=0)
        block_data = tag.read_without_encryption([sc], [bc1, bc2])
        print(int(block_data[14:14+11]))
    except Exception as e:
      print("error: %s" % e)
  else:
    print("error: tag isn't Type3Tag")
  
def main():
  clf = nfc.ContactlessFrontend('usb')
  while True:
    clf.connect(rdwr={'on-connect': on_connect_nfc})
    time.sleep(3)
  
if __name__ == "__main__":
  main()
