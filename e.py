import subprocess, time, os

with open("out.txt","w") as f:
    p = subprocess.Popen(["./stockfish/STOCKFISH_WIN.exe"],stdin=subprocess.PIPE,stdout=f,encoding="utf-8")

    p.stdin.write("position startpos a2a3\n")
    p.stdin.flush()

    p.stdin.write("d\n")
    p.stdin.flush()

    time.sleep(1)
    file= open("out.txt","r")
    content = file.read()
    print(content)
    file.close()


    p.stdin.write("go movetime 1000\n")

    p.stdin.flush()
time.sleep(1)
with open("out.txt", 'rb') as f:
        num_newlines = 0
        try:
            f.seek(-2, os.SEEK_END)    
            while num_newlines < 1:
                f.seek(-2, os.SEEK_CUR)
                if f.read(1) == b'\n':
                    num_newlines += 1
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
print(last_line)