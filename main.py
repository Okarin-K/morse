from pickletools import optimize

from morse3 import Morse as morse
from PIL import Image

CODE_TO_SIGNAL = {
    '.': '_ ',
    '-':'___ ',
    ' ': '  '
}

# 時系列ON/OFF信号用
IS_SIGNAL_ON = {
    '_': True,
    '_': True,
    ' ': False
}

inputMessage = input()

# 文字列をモールス符号文字列に変換し、"."と"_"の継続時間
morse_message = morse(inputMessage).stringToMorse()
time_codes = ''.join([CODE_TO_SIGNAL[message] for message in morse_message])
signals = [IS_SIGNAL_ON[code] for code in time_codes]

# モールス符号として表示したり、時系列ON/OFF符号を表示したり
print(morse_message); print(time_codes)

# モールス信号の信号がONなら「白画像」、OFFなら「黒画像」にするためのテーブル
w=600
h = 1200
IMAGE = {
    True: Image.new('RGB', (w, h), (255, 255, 255)),
    False: Image.new('RGB', (w, h), (0, 0, 0))
}

images = [IMAGE[signal] for signal in signals]

# アニメーションをGIFで保存
images[0].save('message.gif', save_all=True, append_images=images[1:], optimize=True, duration=100, loop=1)
