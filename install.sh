# python3 ライブラリ導入
sudo apt-get install python3-dev portaudio19-dev
sudo pip3 install -r requirements.txt

# カードリーダをsudoなしで認識させる設定
sudo sh -c 'echo SUBSYSTEM=="usb", ACTION=="add", ATTRS{idVendor}=="04cc", ATTRS{idProduct}=="2533", GROUP="plugdev" >> /etc/udev/rules.d/nfcdev.rules'
