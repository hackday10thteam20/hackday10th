import os
import pygame.mixer
import time
import math
import numpy
from numpy.random import *
import threading

# JiroSound
class JiroSound:

  # Sound file names
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

  # Sound file names
  sound_files = []

  number_of_music = 7

  sounds = []

  previous_level = 0

  fade_time = 1.5

  # Init
  def __init__(self, sound_type=1):
    if sound_type == 2:
      self.sound_files = self.sound_files_1
    else:
      for n in range(self.number_of_music):
        file_path = str(n+1)+".ogg"
        self.sound_files.append(file_path)

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
          self.fadein_unpause(i)
        else:
          self.fadein_play(track, i)
        self.played_channels[i] = 1

    if self.previous_level > level:
      for i in range(level, self.previous_level):
        track = self.sounds[i]
        self.fadeout_pause(i)

    self.previous_level = level

  def __get_level(self, level, max_level):
    if level > max_level:
      level = max_level
    return math.ceil(level/max_level*len(self.sound_files))

  # Play sound for Tamefusa OpenCV caller
  def play_sound(self, level, max_level):
    played_level = self.__get_level(level, max_level)
    if played_level == 0:
      played_level = 1
    print("Played Level: "+str(played_level)+"\n")
    self.__play_sound(played_level)
    #time.sleep(60)

  # Fadein Play ( Thread execution )
  def fadein_play(self, track, channel_num):
    thread_name = "thread_fadein_play"+str(channel_num)
    channel = pygame.mixer.Channel(channel_num)
    thread_fadein_play = threading.Thread(target=self.__fadein_play, name=thread_name, args=(track, channel,))
    thread_fadein_play.start()

  def __fadein_play(self, track, channel):
    sleep = self.fade_time
    channel.play(track, -1)
    for n in range(0, 10):
      m = n+1
      volume = m/10
      channel.set_volume(volume)
      #print("fadein: volume = "+str(volume))
      pygame.time.wait(int(sleep/10*1000))

  # Fadein Unpause ( Thread execution )
  def fadein_unpause(self, channel_num):
    thread_name = "thread_fadein_unpause"+str(channel_num)
    channel = pygame.mixer.Channel(channel_num)
    thread_fadein_unpause = threading.Thread(target=self.__fadein_unpause, name=thread_name, args=(channel,))
    thread_fadein_unpause.start()

  def __fadein_unpause(self, channel):
    sleep = self.fade_time
    channel.unpause()
    for n in range(0, 10):
      m = n+1
      volume = m/10
      channel.set_volume(volume)
      #print("fadein: volume = "+str(volume))
      pygame.time.wait(int(sleep/10*1000))

  # Fadeout Pause ( Thread execution )
  def fadeout_pause(self, channel_num):
    thread_name = "thread_fadein_pause"+str(channel_num)
    channel = pygame.mixer.Channel(channel_num)
    thread_fadeout_pause = threading.Thread(target=self.__fadeout_pause, name=thread_name, args=(channel,))
    thread_fadeout_pause.start()

  def __fadeout_pause(self, channel):
    sleep = self.fade_time
    for n in range(0, 10):
      m = n+1
      volume = 1 - m/10
      channel.set_volume(volume)
      #print("fadeout: volume = "+str(volume))
      pygame.time.wait(int(sleep/10*1000))
    channel.pause()

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
      time.sleep(3)
    time.sleep(60)

  # Test to play increasing level sounds
  def test_to_play_level_increasing_sounds(self):
    len_sound_files = len(self.sound_files)
    for level in range(len_sound_files):
      played_level = len_sound_files-level
      print("Level: "+str(played_level))
      self.__play_sound(played_level)
      print("\n")
      time.sleep(3)
    time.sleep(60)

