import pyseccomp  # Importer pyseccomp avec son alias correct

# Créer un filtre Seccomp avec une action par défaut KILL
f = pyseccomp.SyscallFilter(defaction=pyseccomp.LOG)

# Liste des appels système nécessaires pour Dionaea
allowed_syscalls = [
    "read", "write", "open", "close", "stat", "fstat", "lstat", "poll",
    "lseek", "mmap", "mprotect", "munmap", "brk", "rt_sigaction", "rt_sigprocmask",
    "clone", "fork", "vfork", "execve", "wait4", "kill", "access", "pipe2",
    "epoll_ctl", "socket", "connect", "accept", "bind", "listen", "sendto", "recvfrom",
    "getsockname", "getpeername", "shutdown", "getpid", "getuid", "getgid",
    "gettimeofday", "settimeofday", "clock_gettime", "clock_settime", "select", "recvmsg",
    "sendmsg", "futex", "nanosleep", "getdents", "getdents64", "prctl", "getrandom"
]

# Ajouter des règles pour chaque appel système autorisé
for syscall in allowed_syscalls:
    try:
        f.add_rule(pyseccomp.ALLOW, syscall)
    except ValueError as e:
        print(f"Erreur lors de l'ajout de l'appel système '{syscall}': {e}")

# Charger le filtre Seccomp
f.load()

print("Filtrage Seccomp activé pour Dionaea")
