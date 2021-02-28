import socket
import time
import threading
import sys
import select
import tty
import termios
import threading

EXIT_FLAG = False
NAME = ""
END_CHAT = False

# in class baraye non-blocking input estefade mishe. yani ham zaman ke payam mokhatab ro toye console neshon midim betonim payam befrestim
class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk=None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            global EXIT_FLAG
            if EXIT_FLAG:
                break
            self.input_cbk(input())  # waits to get input + Return


# baraye chat kardan be kar borde mishe ham payam mokhatab ro migire ham payam maro neshon mide
def chat(s):
    global EXIT_FLAG
    global END_CHAT
    END_CHAT = False
    EXIT_FLAG = False
    print(
        "****************************************************************************    ANONYMOUS CHAT   ****************************************************************************************")
    print("type exit to close chat")

    # send message
    def my_callback(inp):
        # evaluate the keyboard input
        global EXIT_FLAG
        if ~EXIT_FLAG:
            if inp == "exit":
                EXIT_FLAG = True
                inp = "<the chat closeing>"
                s.sendall(bytes(inp.encode('utf-8')))
                s.close()
            else:
                if END_CHAT == False:
                    s.sendall(bytes(inp.encode('utf-8')))

    # start the Keyboard thread for non-blocking input
    KeyboardThread(my_callback)
    # recive message
    while True:
        if EXIT_FLAG:
            break
        data = recivedmsg_to_str(s.recv(1024))
        if data == "''":
            pass
        else:
            print("new message:\t" + data)
        if data == "'<the chat closeing>'":
            EXIT_FLAG = True
            break
    print(
        "*****************************************************************************************************************************************************************************************")

    s.close()
    END_CHAT = True

# broadcast baraye pyda kardane mokhatab
def UDP_broadcaster(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    try:
        # Enable broadcasting mode
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Set a timeout so the socket does not block
        # indefinitely when trying to receive data.
        sock.settimeout(0.2)
        sock.sendto(message, ('<broadcast>', 37020))
        time.sleep(1)
    finally:
        sock.close()

# listen mikone ta yeki bekhad ba broadcast payam nashnas bede
def udp_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        # Enable broadcasting mode
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(("", 37020))
        data, addr = sock.recvfrom(1024)
    finally:
        sock.close()
    data = str(data)
    # avale string ferestade shode 'b' vojod darad ke hazfesh mikonim
    if data[0] == 'b':
        data = data[1:]
    return data


def UDP_send_msg(msg, IP, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Send data
        sent = sock.sendto(msg, (IP, port))
    finally:
        # print('closing  socket')
        sock.close()


def UDP_recive_msg(IP, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.bind((IP, port))
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    data = str(data)
    if data[0] == 'b':
        data = data[1:]
    sock.close()
    return data, addr


def UDP_recive_msg_with_timeout(IP, port, timeout):
    flag = False
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        sock.bind((IP, port))
        sock.setblocking(False)
        sock.settimeout(timeout)
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = str(data)
        if data[0] == 'b':
            data = data[1:]
        flag = True
        return flag, data, addr
    except:
        return flag, None, None


def recivedmsg_to_str(msg):
    data = str(msg)
    if data[0] == 'b':
        data = data[1:]
    return data


def get_random_port():
    with socket.socket() as s:
        s.bind(('', 0))
        return s.getsockname()[1]


def decode_msg(msg):  # return command and data
    msg = msg.split('$!')
    command = msg[1]
    data = msg[2:-1]
    return command, data


def TCP_decode_msg(msg):  # return command and data
    msg = msg.split('$!')
    command = msg[1]
    data = msg[2]
    return command, data


def send_TCP_msg(s):
    msg = input("your message:\t").encode('utf-8')
    s.sendall(msg)


def recive_TCP_msg(s):
    data = recivedmsg_to_str(s.recv(1024))
    print("new message:\t" + data)


def reject_other_message(IP, port):
    while True:
        data, addr = UDP_recive_msg(IP, port)
        command, data = decode_msg(data)
        if command == "<anonymouschat>":
            type = data[0]
            sender_ip = data[1]
            sender_port = int(data[2])
            if type == "accept":  # user with addr address accepted anonymous chat request connect to him by tcp connection
                detail=NAME+"is chating with someone"
                msg = "$!<anonymouschat>$!" + "refuse" + "$!" + NAME + "$!" + detail+ "$!"  # anonymous chat request message
                msg=msg.encode('utf-8')
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((sender_ip, sender_port))
                    s.sendall(msg)
                    s.close()


NAME = input("enter your name:\t")
while (True):
    mode = input("press 1 for create anonymous chat or 2 for communicate \t")
    if mode == '1':
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        port = get_random_port()
        msg = "$!<anonymouschat>$!" + "request" + "$!" + NAME + "$!" + str(IPAddr) + "$!" + str(
            port) + "$!"  # anonymous chat request message
        msg = msg.encode('utf-8')
        print("create anonymous chat")
        while True:
            UDP_broadcaster(msg)  # broadcast msg
            reciver_flag, data, addr = UDP_recive_msg_with_timeout(IPAddr, port, timeout=10)  # recive response
            if reciver_flag:
                break
        # reject_other_thread = threading.Thread(target=reject_other_message(IPAddr, port),daemon=True)
        reject_other_thread = threading.Thread(target=reject_other_message, args=(IPAddr,port,))
        reject_other_thread.start()
        command, data = decode_msg(data)
        if command == "<anonymouschat>":
            type = data[0]
            sender_ip = data[1]
            sender_port = int(data[2])
            if type == "accept":  # user with addr address accepted anonymous chat request connect to him by tcp connection
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((sender_ip, sender_port))
                    msg = "$!<anonymouschat>$!" + "startchat" + "$!"
                    msg = msg.encode('utf-8')
                    s.sendall(msg)
                    data = s.recv(1024)
                    data = recivedmsg_to_str(data)
                    command, data = TCP_decode_msg(data)
                    if command == "<anonymouschat>":
                        if data == "acceptstart":
                            chat(s)


    elif mode == '2':
        while True:
            print("waiting for sender")
            recived_data = udp_listener()
            command, data = decode_msg(recived_data)
            if command == "<anonymouschat>":
                type = data[0]
                sender_name = data[1]
                sender_ip = data[2]
                sender_port = int(data[3])
                if type == "request":
                    communicate = input(
                        sender_name + " create anonymous chat! if you want to communicate with him press 1 otherwise press 0 \t")
                    if communicate == str(1):
                        hostname = socket.gethostname()
                        IPAddr = socket.gethostbyname(hostname)
                        port = get_random_port()
                        msg = "$!<anonymouschat>$!" + "accept$!" + str(IPAddr) + "$!" + str(
                            port) + "$!"  # anonymous chat request message
                        msg = msg.encode("utf-8")
                        UDP_send_msg(msg, sender_ip, sender_port)

                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.bind((IPAddr, port))
                            s.listen()
                            conn, addr = s.accept()
                            with conn:
                                data = conn.recv(1024)
                                data = recivedmsg_to_str(data)
                                command, data = TCP_decode_msg(data)
                                if command == "<anonymouschat>":
                                    if data == "startchat":
                                        msg = "$!<anonymouschat>$!" + "acceptstart$!"
                                        msg = msg.encode("utf-8")
                                        conn.sendall(msg)
                                        chat(conn)
                                    elif data == "refuse":
                                        print(sender_name + "is chatting with someone, please try later")
                                        conn.close()

            out = input("waiting for another press 1\ngo to menu press 0 \t ")
            if out == str(0):
                break



    else:
        print("invalid input")
