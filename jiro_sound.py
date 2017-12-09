
import pygame.mixer
import time

sound_dic = { "d":"sound/se_maoudamashii_instruments_piano1_1do.mp3",
"r" : "sound/se_maoudamashii_instruments_piano1_2re.mp3",
"m" : "sound/se_maoudamashii_instruments_piano1_3mi.mp3",
"f" : "sound/se_maoudamashii_instruments_piano1_4fa.mp3",
"s" : "sound/se_maoudamashii_instruments_piano1_5so.mp3",
"l" : "sound/se_maoudamashii_instruments_piano1_6ra.mp3",
"t" : "sound/se_maoudamashii_instruments_piano1_7si.mp3",
"hd" : "sound/se_maoudamashii_instruments_piano1_8do.mp3"}

# mixerモジュールの初期化
pygame.init()
pygame.mixer.set_num_channels(8)


# 音楽ファイルの読み込み
do = pygame.mixer.Sound("sound/se_maoudamashii_instruments_piano1_1do.wav")
re = pygame.mixer.Sound("sound/se_maoudamashii_instruments_piano1_2re.wav")
mi = pygame.mixer.Sound("sound/se_maoudamashii_instruments_piano1_3mi.wav")
fa = pygame.mixer.Sound("sound/se_maoudamashii_instruments_piano1_4fa.wav")
so = pygame.mixer.Sound("sound/se_maoudamashii_instruments_piano1_5so.wav")
la = pygame.mixer.Sound("sound/se_maoudamashii_instruments_piano1_6ra.wav")
ti = pygame.mixer.Sound("sound/se_maoudamashii_instruments_piano1_7si.wav")
h_do = pygame.mixer.Sound("sound/se_maoudamashii_instruments_piano1_8do.wav")

pygame.mixer.Channel(0).play(do)
pygame.mixer.Channel(1).play(re)
pygame.mixer.Channel(2).play(mi)
pygame.mixer.Channel(3).play(fa)
pygame.mixer.Channel(4).play(so)
pygame.mixer.Channel(5).play(la)
pygame.mixer.Channel(6).play(ti)
pygame.mixer.Channel(7).play(h_do)
time.sleep(60)
# 再生の終了
pygame.mixer.music.stop()
