import os
import pygame.mixer
import time
import math
import numpy
from numpy.random import *

# JiroSound
class JiroSound:

  # Sound file paths

  sound_files_1 = [
    "bgm_maoudamashii_ethnic11.ogg",
    "bgm_maoudamashii_ethnic12.ogg",
    "bgm_maoudamashii_ethnic25.ogg",
    "bgm_maoudamashii_ethnic15.ogg",
    "bgm_maoudamashii_ethnic16.ogg",
    "bgm_maoudamashii_ethnic17.ogg",
    "bgm_maoudamashii_ethnic18.ogg",
    "bgm_maoudamashii_ethnic19.ogg",
    "bgm_maoudamashii_ethnic20.ogg",
    "bgm_maoudamashii_ethnic21.ogg",
    "bgm_maoudamashii_ethnic22.ogg",
    "bgm_maoudamashii_ethnic23.ogg",
  ]

  sound_files_2 = [
    "1_piano.ogg",
    "2_wood_bass.ogg",
    "3_boss_level_beat.ogg",
    "4_conga.ogg",
    "5_triangle.ogg",
    "7_constraction_bot_topper.ogg",
    "8_chaos_guiter.ogg",
  ]

  sound_files = []

  sounds = []

  previous_level = 0

  # Init
  def __init__(self, sound_type=1):
    if sound_type == 2:
      self.sound_files = self.sound_files_2
    else:
      self.sound_files = self.sound_files_1

    # Init mixer module
    pygame.init()
    pygame.mixer.set_num_channels(len(self.sound_files))

    self.played_channels = numpy.zeros(len(self.sound_files))

    # Read sound files
    print("Loading sound files...")
    for n in self.sound_files:
      full_file_path = self.__full_file_path(n)
      self.sounds.append(pygame.mixer.Sound(full_file_path))
    print("Finish loading sound files...\n")

  # Play sound (Private)
  def __play_sound(self, level):
    if self.previous_level == level:
      return

    if self.previous_level < level:
      for i in range(self.previous_level, level):
        track = self.sounds[i]
        if self.played_channels[i] == 1:
          pygame.mixer.Channel(i).unpause()
        else:
          pygame.mixer.Channel(i).play(track)
        self.played_channels[i] = 1

    if self.previous_level > level:
      for i in range(level, self.previous_level):
        track = self.sounds[i]
        pygame.mixer.Channel(i).pause()

    self.previous_level = level

    # Reset sound
#    for i in range(len(self.sound_files)):
#      pygame.mixer.Channel(i).fadeout(500)

#    for i in range(level):
#      track = self.sounds[i]
#      file_path = self.sound_files[i]
#      print(file_path)
#      pygame.mixer.Channel(i).play(track)

  def get_level(self, level, max_level):
    if level > max_level:
      level = max_level
    return math.ceil(level/max_level*len(self.sound_files))

  # Play sound for Tamefusa OpenCV caller
  def play_sound(self, level, max_level):
    played_level = self.get_level(level, max_level)
    if played_level == 0:
      played_level = 1
    print("Played Level: "+str(played_level))
    self.__play_sound(played_level)
    #time.sleep(60)

  # Generate file path
  def __full_file_path(self, file_path):
    basedir = os.path.dirname(__file__)
    return basedir + "/../sound/" + file_path

  # Test to play random level sounds
  def test_to_play_random_level_sounds(self):
    len_sound_files = len(self.sound_files)
    while True:
      max_level = 9600
      random = randint(max_level)
      print("Input Level: "+str(random))
      self.play_sound(random, max_level)
      time.sleep(2)
    time.sleep(60)

  # Test to play increasing level sounds
  def test_to_play_level_increasing_sounds(self):
    len_sound_files = len(self.sound_files)
    for level in range(len_sound_files):
      played_level = len_sound_files-level
      print("Level: "+str(played_level))
      self.__play_sound(played_level)
      print("\n")
      time.sleep(2)
    time.sleep(60)

  # Test to play garageband sound
  def test_to_play_garageband_sound(self):
    #pygame.mixer.music.load("1_piano.wav")
    file_path = self.__play_sound("bgm_maoudamashii_ethnic23.ogg")
    pygame.mixer.music.load("bgm_maoudamashii_ethnic23.ogg")
    #pygame.mixer.music.play()
    time.sleep(60)

