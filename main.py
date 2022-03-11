import os
from generate_hangul import get_random_hangul
from gtts import gTTS
from io import BytesIO
from tempfile import NamedTemporaryFile
from playsound import playsound

def main():
    command = ''
    while command != 'q':
        command = ''
        hangul = get_random_hangul()

        tmp_file = NamedTemporaryFile()
        voice = tmp_file.name
        gTTS(hangul, lang='ko').save(voice)

        while command != 'y' and command != 'q':
            os.system('clear')
            print("Response:", hangul)
            print("Press enter to repeat")
            print("Press y to go to the next one")
            print("Press q to quit")
            playsound(voice)
            command = input()

        tmp_file.close()

main()
