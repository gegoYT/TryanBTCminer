#DISCLAIMER!: This is Just an Simulation, Wallet mining Doen't Exsist!
#PUBLISHED BY "@gegoYT on Youtube and Tiktok!"
import time

print("\033[1m" + '\033[32m' + 'Started Programm: (state: 1)')
time.sleep(0.75)
print("Program Version: 1.0.0")
time.sleep(0.25)

import itertools
import threading
import time
import sys

done = False


#here is the animation
def animate():
    for c in itertools.cycle(['.', '..', '...']):
        if done:
            break
        sys.stdout.write("\033[31m" + '\rAttempting to Start ' + c)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\033[32m" + '\rStarted!, no problems found!')
    time.sleep(3)


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(4.10)
done = True

time.sleep(3)
import time

print(
    '\033[36m' +
    "▀▀█▀▀ ▒█▀▀█ ▒█░░▒█ ░█▀▀█ ▒█▄░▒█ 　 ▒█░░▒█ ░█▀▀█ ▒█░░░ ▒█░░░ ▒█▀▀▀ ▀▀█▀▀ 　 ▒█▀▄▀█ ▀█▀ ▒█▄░▒█ ▒█▀▀▀ ▒█▀▀█ "
)
print(
    '\033[36m' +
    "                            ░▒█░░ ▒█▄▄▀ ▒█▄▄▄█ ▒█▄▄█ ▒█▒█▒█ 　 ▒█▒█▒█ ▒█▄▄█ ▒█░░░ ▒█░░░ ▒█▀▀▀ ░▒█░░ 　 ▒█▒█▒█ ▒█░ ▒█▒█▒█ ▒█▀▀▀ ▒█▄▄▀ "
)
print(
    '\033[36m' +
    "                            ░▒█░░ ▒█░▒█ ░░▒█░░ ▒█░▒█ ▒█░░▀█ 　 ▒█▄▀▄█ ▒█░▒█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄ ░▒█░░ 　 ▒█░░▒█ ▄█▄ ▒█░░▀█ ▒█▄▄▄ ▒█░▒█ "
)

print('\033[33m' + "Auto Installing Components in 3 Seconds")
time.sleep(3)

import itertools
import threading
import time
import sys

done = False


#here is the animation
def animate():
    for c in itertools.cycle(['.', '..', '...']):
        if done:
            break
        sys.stdout.write("\033[31m" + '\rInstalling Plugins ' + c)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\033[32m" + '\rPlugins Installed! [v1.10]')


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True

from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep


class Loader:  #Fixed Color issue that shows only Green Font.
    def __init__(self,
                 desc="\033[36m" + "[TryanSYSTEM:]" + "\033[31m"
                 "Installing...",
                 end="\033[36m" + "[TryanSYSTEM:]" + "\033[32m"
                 "Installation succed!",
                 timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("\033[32m" + "Plugins Installed![v1.10]"):
        for i in range(10):
            sleep(0.25)

    loader = Loader(
        "\033[31m" + "Waiting for response...",
        "\033[36m" + "[TryanSYSTEM:]" + "\033[32m"
        "TryanBTC Libary Installed!", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()

if __name__ == "__main__":
    with Loader("\033[31m" + "Getting Data for mining..."):
        for i in range(10):
            sleep(0.15)

    loader = Loader(
        "\033[36m" + "[TryanSYSTEM:]" + "\033[32m"
        "got enough data to start Mining BTC!", ).start()
    for i in range(10):
        sleep(0.45)
    loader.stop()

input("Type /start tryan to mine!: ")

print(
    "   ████████╗██████╗░██╗░░░██╗░█████╗░███╗░░██╗  ██████╗░████████╗░█████╗░  ███╗░░░███╗██╗███╗░░██╗███████╗██████╗░"
)
print(
    "   ╚══██╔══╝██╔══██╗╚██╗░██╔╝██╔══██╗████╗░██║  ██╔══██╗╚══██╔══╝██╔══██╗  ████╗░████║██║████╗░██║██╔════╝██╔══██╗"
)
print(
    "   ░░░██║░░░██████╔╝░╚████╔╝░███████║██╔██╗██║  ██████╦╝░░░██║░░░██║░░╚═╝  ██╔████╔██║██║██╔██╗██║█████╗░░██████╔╝"
)
print(
    "   ░░░██║░░░██╔══██╗░░╚██╔╝░░██╔══██║██║╚████║  ██╔══██╗░░░██║░░░██║░░██╗  ██║╚██╔╝██║██║██║╚████║██╔══╝░░██╔══██╗"
)
print(
    "   ░░░██║░░░██║░░██║░░░██║░░░██║░░██║██║░╚███║  ██████╦╝░░░██║░░░╚█████╔╝  ██║░╚═╝░██║██║██║░╚███║███████╗██║░░██║"
)
print(
    "   ░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═════╝░░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝"
)

import string, random, time


def main():
    adress = input("Enter /start to continue!: ")
    print("starting...")
    characters = string.ascii_lowercase + string.digits
    for _ in range(17500):
        print("\033[31m" + "[BTC] %s | 0.00000 BTC" %
              "".join(random.sample(characters, 32)))
    print("\033[32m" +
          "[BTC] %s | 0.12383 BTC" % "".join(random.sample(characters, 32)))
    time.sleep(1)
    print("\033[33m" + "[BTC] transfer to User BTC Wallet...")
    time.sleep(0.75)
    print("\033[36m" + "[BTC] TOTAL | 0.12383 BTC")
    time.sleep(0.25)
    print("[BTC] IN $ | 4441.21 $ ")
    time.sleep(0.85)
    print("\033[32m" + "[BTC] ACCOUNT BALANCE | 0.12383 BTC > 4441.21 $")


main()

#Published VERSION! [v1.0.0]
