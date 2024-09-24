from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'flaviof', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000004, 'gfetch', [c for c in 'git fetch --all --prune']),
        (0x000000, 'edit', [c for c in 'emacs /Volumes/CIRCUITPY*/macros/flaviof.py']),
        (0x000000, 'CP Lnk', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, 'c']),
        # 2nd row ----------
        (0x000000, 'k8', [c for c in 'kubectl get pod -o wide -A']),
        (0x000000, 'ok8', [c for c in ';ok8']),
        (0x000000, 'Emoji', [Keycode.CONTROL, Keycode.COMMAND, ' ']),
        # 3rd row ----------
        (0x000000, 'ctlbld', [';', '1']),
        (0x000000, 'northd', [';', '2']),
        (0x000000, 'ovnmon', [';', '3']),
        # 4th row ----------
        (0x000000, 'ctllog', [';', '4']),
        (0x000000, 'lga', [c for c in 'git log --oneline --decorate --graph --all']),
        (0x000000, 'euuid', [c for c in ';euuid']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}

