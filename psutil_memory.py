import psutil

# Return statistics about system memory usage as a named tuple including the following fields, expressed in bytes.

#     total: total physical memory.
#     available: the memory that can be given instantly to processes without the system going into swap. This is calculated by summing different memory values depending on the platform and it is supposed to be used to monitor actual memory usage in a cross platform fashion.

# Other metrics:

#     used: memory used, calculated differently depending on the platform and designed for informational purposes only. total - free does not necessarily match used.
#     free: memory not being used at all (zeroed) that is readily available; note that this doesn’t reflect the actual memory available (use available instead). total - used does not necessarily match free.
#     active (UNIX): memory currently in use or very recently used, and so it is in RAM.
#     inactive (UNIX): memory that is marked as not used.
#     buffers (Linux, BSD): cache for things like file system metadata.
#     cached (Linux, BSD): cache for various things.
#     shared (Linux, BSD): memory that may be simultaneously accessed by multiple processes.
#     slab (Linux): in-kernel data structures cache.
#     wired (BSD, macOS): memory that is marked to always stay in RAM. It is never moved to disk.

# The sum of used and available does not necessarily equal total. On Windows available and free are the same. See meminfo.py script providing an example on how to convert bytes in a human readable form.
print(psutil.virtual_memory())

# Return system swap memory statistics as a named tuple including the following fields:

#     total: total swap memory in bytes
#     used: used swap memory in bytes
#     free: free swap memory in bytes
#     percent: the percentage usage calculated as (total - available) / total * 100
#     sin: the number of bytes the system has swapped in from disk (cumulative)
#     sout: the number of bytes the system has swapped out from disk (cumulative)

# sin and sout on Windows are always set to 0. See meminfo.py script providing an example on how to convert bytes in a human readable form.
print(psutil.swap_memory())
