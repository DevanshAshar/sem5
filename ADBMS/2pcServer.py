import socket
def ServerSoc():
    host = "127.0.0.1"
    port = 8000
    print("Server is running!")
    msg = "PREPARE"
    log = msg
    over = 0
    s_soc = socket.socket()
    s_soc.bind((host,port))
    s_soc.listen(2)
    while(1):
        replies = []
        print(f"Coordinator : {msg.upper()}")
        for i in range(3):
            conn,add = s_soc.accept()
            conn.send(msg.encode())
            data = conn.recv(1024).decode()
            replies.append(data.upper())
            print(f"Subordinator {i} {add} : {data.upper()}")
        if over == 1:
            break
        if ("ABORT" in replies) or (len(replies)<3) :
            msg = "ABORT"
            print("TRANSACTION ABORTED!\nThe final log is: ", log+" "+msg)
            over = 1
        elif "SUCCESS" in replies:
            msg = "COMPLETE"
            print("TRANSACTION COMPLETED!\nThe final log is: ", log+" "+msg)
            over = 1
        else:
            msg = "COMMIT"
        log += " "+msg
ServerSoc()
