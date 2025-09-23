import os
import webbrowser
import time

print("Python Pc Crasher")
print("\t\t\t\t\t\t\t\t\t\t\t\tBy KacperSob")
print("")
print("")

time.sleep(3)

a = 1
full = input('Do you want to fill up (full) disk? 1 - Yes, 0 - No (specific amount) (WARNING! if you fill up full disk no crashing will apear!): ')
b = input('Enter how many gigabytes of data must script generate: ')
rick = input('Do you want to open rick roll tabs (1)? Or you want to open terminals (2)? Or open tabs with your link? (3)? Or crash it by opening txt files(4) (beta)?: ')
if (int(rick) == 3):
	link = input('What\'s your link? Just paste it here: ')

time.sleep(3)



if (int(full) == 1):
	while a == 1:
		ib = i + 1
		name = 'YouGotHackedBro_' + str(ib) + '.txt'
		fp = open(name, 'w')
		print("Created file n " + str(ib))
		for x in range(10):
			xb = x + 1
			fp.write("X"*1024*1024*10)
			print("Writing... " + str(xb))
else: 
	c = int(b)*10
	for i in range(int(c)):
		ib = i + 1
		name = 'víces' + str(ib) + '.txt'
		fp = open(name, 'w')
		print("Created file n " + str(ib))

		for x in range(10):
			xb = x + 1
			fp.write("X"*1024*1024*10)
			print("Writing... " + str(xb))

# for i in range(10):
	# os.system("start")
	
# webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

if (int(rick) == 1):
	print("Ok browser. Here it comes")
	while a == 1:
		webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
	# webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
elif (int(rick) == 2):
	print("You choosed third option. Let's go")
	yup = input("Are you on linux (1) or windows (2)?: ")
	match int(yup):
		case 1:
			while a == 1:
				os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
		case 2:
			while a == 2:
				os.system("start")

	# os.system("start")
elif (int(rick) == 3):
	print("Let's see how your link looks like...")
	while a == 1:
		webbrowser.open(link)
	# webbrowser.open(link)
elif (int(rick) == 4):
	name = "demofile.txt"
	fp = open(name, 'w')
	for x in range(10):
		xb = x + 1
		fp.write("X"*1024*1024*10)
		print("Writing... " + str(xb))
	f = open(name, "rt") 
	while a == 1:
		f = open(name, "rt")

fp.close()