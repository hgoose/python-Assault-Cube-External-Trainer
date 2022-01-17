from pymem import *
from pymem.process import *
import keyboard
import time
import os

client = Pymem('ac_client.exe')
module = module_from_name(client.process_handle, 'ac_client.exe').lpBaseOfDll

def getPointer(base, offsets):
	addr = client.read_int(base)
	for offset in offsets:
		if offset != offsets[-1]:
			addr = client.read_int(addr + offset)

	return addr + offsets[-1]



while True:

	os.system('cls')

	print("""

		Assualt Cube Scripts - made by noodl - 

		--usage

		1: Set all ammo 9999

		2: Set Heath/Armor 9999

		3: Disable Cooldown (Firing/knife)\n

			  : Type 9 to exit :

	""")

	mode = int(input('''

		\nSelect an option: 

	'''))

	if mode == 1:
		client.write_int(getPointer(module+ 0x0012CB90, [0x810,0x56C,0xA4,0x1D0]),1000)
		client.write_int(getPointer(module + 0x000FAB48, [0x228,0xF8,0x2B4,0x494]),1000)

	if mode == 2:
		client.write_int(getPointer(module + 0x000B8234, [0X24,0X58,0XF8]), 9999)
		client.write_int(getPointer(module + 0x0010A280, [0x8,0xC4,0x41C]), 9999)
	if mode ==8:
		while True:
			client.write_int(getPointer(module + 0x00100E90, [0xAC,0x284,0x4D0]),0)
			client.write_int(getPointer(module + 0x00100E88, [0x4,0xE4,0x7BC,0x6C,0x330]), 0)


	if mode == 3:
		while True:
			client.write_int(getPointer(module + 0x00100E90, [0xAC,0x284,0x4D0]),0)
			client.write_int(getPointer(module + 0x00100E88, [0x4,0xE4,0x7BC,0x6C,0x330]), 0)

			os.system('cls')

			print("""

				Assualt Cube Scripts - made by noodl - 

				--usage

				1: Set all ammo 9999

				2: Set Health and Armor to 9999

					  : Type 9 to exit : 

	
			""")

			mode = int(input('''

			\nSelect an option: 

			'''))

			if mode == 1: 
				client.write_int(getPointer(module+ 0x0012CB90, [0x810,0x56C,0xA4,0x1D0]),1000)
				client.write_int(getPointer(module + 0x000FAB48, [0x228,0xF8,0x2B4,0x494]),1000)

			if mode == 2: 
				client.write_int(getPointer(module + 0x000B8234, [0X24,0X58,0XF8]), 9999)
				client.write_int(getPointer(module + 0x0010A280, [0x8,0xC4,0x41C]), 9999)

			if mode == 9: 
				break


	if mode == 9:
		break








