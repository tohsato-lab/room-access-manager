import datetime
from pathlib import Path
import time

import nfc
from nfc.tag import tt3

from make_txt import make_text
from sound import play_sound

sound_dir = '../sounds'


def on_connect_nfc(tag):
    try:
        servc = 0x1A8B
        service_code = [tt3.ServiceCode(servc >> 6, servc & 0x3F)]
        print(tag.dump())  # これがないと何故かうまくいかなかった
        bc_id = [tt3.BlockCode(0)]
        bd_id = tag.read_without_encryption(service_code, bc_id)
        student_id = int(bd_id[2:-3].decode("utf-8"))
        bc_name = [tt3.BlockCode(1)]
        student_name = (
            tag.read_without_encryption(service_code, bc_name).decode("shift-jis").rstrip("\x00")
        )
        # return student_id, student_name
        dt_now = datetime.datetime.now()
        print(dt_now.strftime('%H:%M'))
        print(student_id, student_name)
        make_text(student_id=student_id, name=student_name, time=dt_now.strftime('%H:%M'))
        play_sound(str(Path(sound_dir).joinpath("thank_you.wav")))
    except Exception as e:
        print("error: %s" % e)
        play_sound(str(Path(sound_dir).joinpath("i_do_not_understand.wav")))


def main():
    clf = nfc.ContactlessFrontend('usb')
    while True:
        clf.connect(rdwr={'on-connect': on_connect_nfc})
        time.sleep(3)


if __name__ == "__main__":
    main()
