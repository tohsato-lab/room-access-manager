#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nfc

def connected(tag):
  # IDm, PMM等を出力
  print(tag)

  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
      # 内容を16進数で出力する
      print(('  ' + '\n  '.join(tag.dump())))
    except Exception as e:
      print("error: %s" % e)
  else:
    print("error: tag isn't Type3Tag")

# タッチ時のハンドラを設定して待機する
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
