'''
Created on Apr 6, 2021

@author: martinyanev
'''

import os

#FPS

FPS = 60

SCREENWIDTH = 288
SCREENHEIGHT = 512

PIPE_GAP_SIZE = 100


NUMBER_IMAGE_PATHS = {
    '0': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/0.png'),
    '1': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/1.png'),
    '2': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/2.png'),
    '3': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/3.png'),
    '4': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/4.png'),
    '5': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/5.png'),
    '6': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/6.png'),
    '7': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/7.png'),
    '8': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/8.png'),
    '9': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/9.png')
}



BIRD_IMAGE_PATHS = {
    'red': {
        'up': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/redbird-upflap.png'),
        'mid': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/redbird-midflap.png'),
        'down': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/redbird-downflap.png')
    },
    'blue': {
        'up': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/bluebird-upflap.png'),
        'mid': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/bluebird-midflap.png'),
        'down': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/bluebird-downflap.png')
    },
    'yellow': {
        'up': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/yellowbird-upflap.png'),
        'mid': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/yellowbird-midflap.png'),
        'down': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/yellowbird-downflap.png')
    }
}

BACKGROUND_IMAGE_PATHS = {
    'day': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/background-day.png'),
    'night': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/background-night.png')
}


PIPE_IMAGE_PATHS = {
    'green': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/pipe-green.png'),
    'red': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/pipe-red.png')
}

OTHER_IMAGE_PATHS = {
    'gameover': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/gameover.png'),
    'message': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/message.png'),
    'base': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/images/base.png')
}


AUDIO_PATHS = {
    'die': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/audios/die.wav'),
    'hit': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/audios/hit.wav'),
    'point': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/audios/point.wav'),
    'swoosh': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/audios/swoosh.wav'),
    'wing': os.path.join(os.getcwd(), 'D:/18110168_GITHUBS/PythonRealWorldGames/Some/Game8_Flappy_Bird/resources/audios/wing.wav')
}