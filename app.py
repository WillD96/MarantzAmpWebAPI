from flask import Flask, render_template, redirect
import os

DEV = "/dev/lirc0"
IRCTLBIN = "/usr/bin/ir-ctl"


commands = {
    "TogglePower": ("rc5", "0x100c"),
    "VolumeUp": ("rc5", "0x1010"),
    "VolumeDown": ("rc5", "0x1011"),
    "InputOptical": ("rc5x_20", "0x10011a"),
    "InputCoaxial": ("rc5x_20", "0x100119"),
    "InputPhono": ("rc5x_20", "0x153f"),
    "Mute": ("rc5", "0x100d"),
    "SourceDirect":  ("rc5", "0x1022")
}


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/amp/<command>")
def execCommand(command):
    toExec = formCommand(command)
    if toExec:
        res = os.system(toExec)
        if res == 0:
            print("Command '{}' executed successfully.".format(toExec))
        else:
            print("Issue executing command. Status code: {}".format(res))
    return redirect("/")


def formCommand(command):
    if command in commands:
        return "{} -S {}:{} -d {}".format(IRCTLBIN, commands[command][0], commands[command][1], DEV)
    return None
