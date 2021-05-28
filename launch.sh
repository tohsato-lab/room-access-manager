# kill signal キャッチ
trap 'last' {1,2,3,15}

last() {
  aplay '../sounds/panic.wav' &&
	kill `ps aux | grep "push_recode_main" | grep -v "grep" | awk '{print $2}'` &>/dev/null
	kill `ps aux | grep "subscribe_card_main" | grep -v "grep" | awk '{print $2}'` &>/dev/null

	exit 1
}

cd push_record/
python3 push_recode_main.py &
cd ../subscribe_card/
python3 subscribe_card_main.py
