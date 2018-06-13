#!usr/bin/python
# Menu driven Program
import time
import os
import webbrowser
import urllib.request
import subprocess
x='''
Press 1:To check current date and time
Press 2:To check current time only
Press 3:To create a file
Press 4:To create a directory
Press 5:To search something on google
Press 6:To logout you account
Press 7:To shutdown your OS
Press 8:To check internet connection on your PC
Press 9:To login whatapp on browser
'''
print (x)
choice=input(" Enter your choice: ")

if choice=='1':
	print ("CURRENT DATE AND TIME") 
	print (time.ctime())#time is the library and ctime is the function within time library

elif choice=='2':
	print ("CURRENT TIME")
	print (time.ctime().split()[3])#split change the strings into the list

elif choice=='3':
	print ("CREATING A FILE")
	f= open ("Myfile5.txt","x")#x show the error if file name already exist
	f= open ("Myfile6.txt","w")#w will  create a file, if exist then it will remove all the content of that file and crezate a empty file
	f= open ("Myfile7.txt","a")#a will create a file if there is no file with existing name

elif choice=='4':
	print("CREATING A FOLDER")
	path='/home/drishti/6thjune18/directory_name'
	os.makedirs(path, exist_ok=True)

elif choice=='5':
	print ("SEARCHING ON GOOGLE")
	msg=input("TYPE TO WHAT TO SEARCH:")
	webbrowser.open_new_tab('https://www.google.com/search?q'+msg)#open the webbrowser and a new tab will open and searching proceed

elif choice=='6':
	print ("LOGOUT YOUR ACCOUNT")
	os.system('gnome-session-quit')#system is the function of os library

elif choice=='7':
	print ("SHUTDOWN OS")
	time.sleep(2)
	os.system("poweroff")

elif choice=='8':
	print ("CHECKING INTERNET CONNECTION")
	url="https://www.google.com"
	urllib.request.urlopen(url)#urlopen is the function of urllib.request library
	status="Connected"
	print (status)

elif choice=='9':
	print ("LOGIN WHATSAPP FROM BROWSER")
	webbrowser.open_new_tab('https://web.whatsapp.com/')#open_new_tab is the function in webbrowser library


else :
	print ("Wrong choice")


