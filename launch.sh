# kill signal キャッチ
trap 'last' {1,2,3,15}

last() {
  aplay './sounds/panic.wav' &&
	kill `ps aux | grep "push_recode_main" | grep -v "grep" | awk '{print $2}'` &>/dev/null
	kill `ps aux | grep "subscribe_card_main" | grep -v "grep" | awk '{print $2}'` &>/dev/null

	exit 1
}

main(){
  cd push_record/
  echo 'start push_recode_main'
  python3 -u push_recode_main.py &
  cd ../subscribe_card/
  echo 'start subscribe_card_main'
  python3 -u subscribe_card_main.py
}

main 2>&1 | tee -a log.txt
