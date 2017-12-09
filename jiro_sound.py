import pygame.mixer
import time

# 音をならす
def play_sound(level, sounds):
  for i in range(level):
    track = sounds[i]
    pygame.mixer.Channel(i).play(track)
  # 再生の終了
  pygame.mixer.music.stop()

sound_files = [
  "sound/se_maoudamashii_instruments_piano1_1do.wav",
  "sound/se_maoudamashii_instruments_piano1_2re.wav",
  "sound/se_maoudamashii_instruments_piano1_3mi.wav",
  "sound/se_maoudamashii_instruments_piano1_4fa.wav",
  "sound/se_maoudamashii_instruments_piano1_5so.wav",
  "sound/se_maoudamashii_instruments_piano1_6ra.wav",
  "sound/se_maoudamashii_instruments_piano1_7si.wav",
  "sound/se_maoudamashii_instruments_piano1_8do.wav"
]

# mixerモジュールの初期化
pygame.init()
pygame.mixer.set_num_channels(8)

# 音楽ファイルの読み込み
sounds = []
i = 0
for n in sound_files:
  sounds.append(pygame.mixer.Sound(sound_files[i]))
  i = i+1

#level = int(input('Input Level: '))
#level = 1
for level in range(8):
  print(level)
  play_sound(level, sounds)
  time.sleep(1)

time.sleep(60)
