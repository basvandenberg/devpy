import __builtin__
# import builtins <== python3

openfiles = set()
oldfile = __builtin__.file
# oldfile = builtins.file <== python3

class NewFile(oldfile):

    def __init__(self, *args):

        # store the file name
        self.file_path = args[0]

        # print that this file is going to be opened
        print("==> open %s" % str(self.file_path))

        # use builtin file to open file
        oldfile.__init__(self, *args)

        # add this file to the set of open files
        openfiles.add(self)

    def close(self):

        # print that this file is going to be closed
        print("==> close %s" % str(self.x))

        # use builtin file to close the file
        oldfile.close(self)

        # remove this file from the set of open files
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
    '''
    This function prints how many files are currently opened to the standard
    output, followed by a list with names of the open files.
    '''
    print("==> %d open files: [%s]" %
          (len(openfiles), ", ".join(f.x for f in openfiles)))
