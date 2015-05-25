import mmap
from carseour.definitions import GameInstance, SHARED_MEMORY_VERSION

def _get_mmapped():
    # could we use ctypes.sizeof(GameInstance) instead here? A too large value results in access denied,
    # 8k works for now
    return mmap.mmap(0, 8000, tagname='$pcars$')

def _validate_instance(instance):
    if instance.mVersion != SHARED_MEMORY_VERSION:
        raise InvalidSharedMemoryVersionException("""
            Mismatch between library data structure version and game data structure version.
            Retrieve new SharedMemory.h and run bin/generate_classes.py to regenerate the definitions file.
            """)

    return instance

def get_live():
    return _validate_instance(GameInstance.from_buffer(_get_mmapped()))

def get_snapshot():
    return _validate_instance(GameInstance.from_buffer_copy(_get_mmapped()))

class InvalidSharedMemoryVersionException(Exception):
    pass