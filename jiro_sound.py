import pygame.mixer
import time

# JiroSound
class JiroSound:

  # Sound file paths
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

  sounds = []

  # Init
  def __init__(self):
    # Init mixer module
    pygame.init()
    pygame.mixer.set_num_channels(8)

    # Read sound files
    i = 0
    for n in self.sound_files:
      self.sounds.append(pygame.mixer.Sound(self.sound_files[i]))
      i = i+1

  # Play sound
  def play_sound(self, level):
    for i in range(level):
      track = self.sounds[i]
      print(track)
      pygame.mixer.Channel(i).play(track)
    # Stop sound
    pygame.mixer.music.stop()

  # Play demo sounds
  def play_demo_sounds(self):
    for level in range(8):
      print(level)
      self.play_sound(level+1)
      time.sleep(1)
    time.sleep(60)


jiroSound = JiroSound()
jiroSound.play_demo_sounds()
