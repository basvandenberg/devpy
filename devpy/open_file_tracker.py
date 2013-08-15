import __builtin__
# import builtins <== python3

openfiles = set()
oldfile = __builtin__.file
# oldfile = builtins.file <== python3

class NewFile(oldfile):

    def __init__(self, *args):

        self.x = args[0]

        print("==> open %s" % str(self.x))

        oldfile.__init__(self, *args)
        openfiles.add(self)

    def close(self):

        print("==> close %s" % str(self.x))

        oldfile.close(self)
        openfiles.remove(self)

oldopen = __builtin__.open
# oldopen = builtins.open <== python3


def newopen(*args):
    return NewFile(*args)

__builtin__.file = NewFile
# builtins.file = NewFile <== python3
__builtin__.open = newopen
# builtins.open = newopen <== python3


def print_open_files():
    print("==> %d open files: [%s]" %
          (len(openfiles), ", ".join(f.x for f in openfiles)))
