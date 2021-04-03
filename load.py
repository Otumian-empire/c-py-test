import importlib
import uuid

import cffi

# In an instace where a static variable is used the values will
#  be cached and used throught the test. this is not what we
# expect and as such we would have to import a new module
# everytime the function is called

# In an instance that there are multiple depencies then we need
# handle the headers with a preprocessor directive

# There is a whole lot of hacks so the best thing is to try a
# C/C++ testing framework


def load(filename):
    # generate a random name
    name = filename + "_" + uuid.uuid4().hex

    # load source code
    # with open(filename+".c") as srcfp:
    #     source = srcfp.read()
    with open(filename+".c") as srcfp:
        source = srcfp.read()

    # load header code
    with open(filename+".h") as hdrfp:
        header = hdrfp.read()

    # build source
    ffibuilder = cffi.FFI()
    ffibuilder.cdef(header)

    # ffibuilder.set_source(filename+"_", source)
    ffibuilder.set_source(name+"_", source)
    ffibuilder.compile()

    # import and return resulting module
    module = importlib.import_module(name+"_")
    return module.lib
