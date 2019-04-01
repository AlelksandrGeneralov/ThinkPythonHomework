import psutil

# Return system CPU times as a named tuple. Every attribute represents the seconds the CPU has spent in the given mode.
print(psutil.cpu_times(percpu=False))

# Return a float representing the current system-wide CPU utilization as a percentage. When interval is > 0.0 compares system CPU times elapsed before and after the interval (blocking). When interval is 0.0 or None compares system CPU times elapsed since last call or module import, returning immediately. That means the first time this is called it will return a meaningless 0.0 value which you are supposed to ignore. In this case it is recommended for accuracy that this function be called with at least 0.1 seconds between calls. When percpu is True returns a list of floats representing the utilization as a percentage for each CPU. First element of the list refers to first CPU, second element to second CPU and so on. The order of the list is consistent across calls.
print(psutil.cpu_percent(interval=1))
print(psutil.cpu_percent(interval=None))
print(psutil.cpu_percent(interval=1, percpu=True))

# Same as cpu_percent() but provides utilization percentages for each specific CPU time as is returned by psutil.cpu_times(percpu=True). interval and percpu arguments have the same meaning as in cpu_percent(). On Linux “guest” and “guest_nice” percentages are not accounted in “user” and “user_nice” percentages.
print(psutil.cpu_times_percent(interval=1, percpu=False))

# Return the number of logical CPUs in the system (same as os.cpu_count in Python 3.4) or None if undetermined. If logical is False return the number of physical cores only (hyper thread CPUs are excluded) or None if undetermined.
print(psutil.cpu_count(logical=True))

# Return various CPU statistics as a named tuple:

# ctx_switches: number of context switches (voluntary + involuntary) since boot.
# interrupts: number of interrupts since boot.
# soft_interrupts: number of software interrupts since boot. Always set to 0 on Windows and SunOS.
# syscalls: number of system calls since boot. Always set to 0 on Linux.
print(psutil.cpu_stats())

# Return CPU frequency as a nameduple including current, min and max frequencies expressed in Mhz. On Linux current frequency reports the real-time value, on all other platforms it represents the nominal “fixed” value. If percpu is True and the system supports per-cpu frequency retrieval (Linux only) a list of frequencies is returned for each CPU, if not, a list with a single element is returned. If min and max cannot be determined they are set to 0.
print(psutil.cpu_freq(percpu=True))
