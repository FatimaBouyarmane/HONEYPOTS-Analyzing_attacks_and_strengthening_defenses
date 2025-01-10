import pyseccomp
import os
import time

# List of allowed syscalls (Cowrie-specific syscalls)
allowed_syscalls = [
    "access", "arch_prctl", "bind", "brk", "chdir", "clone", "close", "dup", "dup2", "epoll_create1", 
    "epoll_ctl", "execve", "faccessat", "fcntl", "fstat", "futex", "getcwd", "getdents64", "getegid", 
    "geteuid", "getgid", "getpgrp", "getpid", "getppid", "getrandom", "gettid", "getuid", "ioctl", "kill", 
    "lseek", "lstat", "mmap", "mprotect", "munmap", "openat", "pipe", "pipe2", "pread64", "prlimit64", "read", 
    "readlink", "rt_sigaction", "rt_sigprocmask", "rt_sigreturn", "sched_getaffinity", "set_robust_list", 
    "set_tid_address", "sigaltstack", "socket", "stat", "statx", "syscall", "sysinfo", "uname", "wait4", "write",
    "futex", "clone", "mmap", "open", "read", "write", "select", "poll"
]

# Creating a seccomp filter context (default action: kill process on syscall violation)
seccomp_filter = pyseccomp.SyscallFilter(defaction=pyseccomp.KILL)

# Adding allowed syscalls to the filter
for syscall in allowed_syscalls:
    try:
        seccomp_filter.add_rule(pyseccomp.ALLOW, syscall)
    except ValueError as e:
        print(f"Error adding syscall {syscall}: {e}")

# Applying the filter
try:
    seccomp_filter.load()
    print("Seccomp filter applied. Program will now restrict syscalls.")
except Exception as e:
    print(f"Failed to apply seccomp filter: {e}")
    exit(1)

time.sleep(10)
