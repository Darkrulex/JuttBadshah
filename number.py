import platform
bit=platform.architecture()[0]
if bit == '64bit':
    from number64 import reg
    reg()
elif bit == '32bit':
    from number32 import reg
    reg()
