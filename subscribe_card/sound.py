import glob
import wave

import pyaudio


def play_sound(file_name=None):
    CHUNK = 1024
    # filename="sound_folder/thank_you.wav"
    wf = wave.open(file_name, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    """
       format  : ストリームを読み書きするときのデータ型
       channels: ステレオかモノラルかの選択 1でモノラル 2でステレオ
       rate    : サンプル周波数
       output  : 出力モード
    """
    # 1024個読み取り
    data = wf.readframes(CHUNK)
    while data != b'':
        stream.write(data)  # ストリームへの書き込み(バイナリ)
        data = wf.readframes(CHUNK)  # ファイルから1024個*2個の
    stream.stop_stream()
    stream.close()
    p.terminate()


def main():
    folder_name = "../sounds"
    file_name_list = glob.glob(folder_name + "/*.wav")
    for file_name in file_name_list:
        print(file_name[13:])
        play_sound(file_name)
    pass


if __name__ == '__main__':
    main()
