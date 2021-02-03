from subprocess import Popen,PIPE,STDOUT
import datetime
time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

file = time + 'Monkey日志输出.txt'

def run_shell(cmd):
    p = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    i = 1
    for line in iter(p.stdout.readline, 'b'):
        line = line.decode("utf-8").strip()
        with open(file, 'a', encoding='utf-8') as f:
            f.write(line + "\n")
            print(i)
            i += 1
            print(line)
        if not p.poll():
            if line == '':
                break

i = 0

while i <10:
    run_shell('adb shell monkey -p cn.mainto.maintoapp -v -v -v 10000')
    i += 1
    from time import sleep
    sleep(3)
    import os
    # os.system('adb shell am force-stop cn.mainto.maintoapp')