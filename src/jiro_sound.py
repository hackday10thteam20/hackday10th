import os
import pygame.mixer
import time
import math

# JiroSound
class JiroSound:

  basedir = os.path.dirname(__file__)
  # Sound file paths
  sound_files = [
    basedir + "/../sound/bgm_maoudamashii_ethnic11.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic12.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic25.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic15.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic16.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic17.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic18.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic19.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic20.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic21.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic22.ogg",
    basedir + "/../sound/bgm_maoudamashii_ethnic23.ogg",
  ]

  sounds = []

  # Init
  def __init__(self):
    # Init mixer module
    pygame.init()
    pygame.mixer.set_num_channels(len(self.sound_files))

    # Read sound files
    print("Loading sound files...")
    i = 0
    for n in self.sound_files:
      self.sounds.append(pygame.mixer.Sound(self.sound_files[i]))
      i = i+1
    print("Finish loading sound files...\n")

  # Play sound (Private)
  def __play_sound(self, level):
    # Reset sound
    for i in range(len(self.sound_files)):
      pygame.mixer.Channel(i).stop()

    for i in range(level):
      track = self.sounds[i]
      file_path = self.sound_files[i]
      print(file_path)
      pygame.mixer.Channel(i).play(track)

  # Play sound for Tamefusa OpenCV caller
  def play_sound(self, level, max_level):
    played_level = math.ceil(level/max_level*len(self.sound_files))
    print("Played Level: "+str(played_level))
    self.__play_sound(played_level)
    #time.sleep(60)

  # Play demo sounds
  def play_demo_sounds(self):
    len_sound_files = len(self.sound_files)
    for level in range(len_sound_files):
      played_level = len_sound_files-level
      print("Level: "+str(played_level))
      self.__play_sound(played_level)
      print("\n")
      time.sleep(1)
    time.sleep(60)
