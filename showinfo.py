FG_BLACK   = "\x1b[90m"
FG_RED     = "\x1b[91m"
FG_GREEN   = "\x1b[92m"
FG_YELLOW  = "\x1b[93m"
FG_BLUE    = "\x1b[94m"
FG_MAGENTA = "\x1b[95m"
FG_CYAN    = "\x1b[96m"
FG_WHITE   = "\x1b[97m"
FG_DEFAULT = "\x1b[39m"

BG_BLACK   = "\x1b[100m"
BG_RED     = "\x1b[101m"
BG_GREEN   = "\x1b[102m"
BG_YELLOW  = "\x1b[103m"
BG_BLUE    = "\x1b[104m"
BG_MAGENTA = "\x1b[105m"
BG_CYAN    = "\x1b[106m"
BG_WHITE   = "\x1b[107m"
FG_DEFAULT = "\x1b[49m"
    
BOLD       = "\x1b[1m"
ITALIC     = "\x1b[3m"
UNDERLINE  = "\x1b[4m"

NORMAL     = "\x1b[0m"


class ShowInfo:
    def __init__(self, mode=True):
        self.mode = mode

    def show(self, msg, type="info"):
        if self.mode:
            type = type.upper()
    
            if type == "WARNING":
                print(FG_RED + "["+type+"] " + FG_WHITE + msg)
            elif type == "PROCESS":
                print(FG_CYAN + "["+type+"] " + FG_WHITE + msg)
            else:
                print(FG_GREEN + "["+type+"] " + FG_WHITE + msg)
