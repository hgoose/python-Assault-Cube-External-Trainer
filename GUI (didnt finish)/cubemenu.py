from tkinter import *
from pymem import *
from pymem.process import *
import keyboard

client = Pymem('ac_client.exe')
module = module_from_name(client.process_handle, 'ac_client.exe').lpBaseOfDll

def getPointer(base, offsets):
	addr = client.read_int(base)
	for offset in offsets:
		if offset != offsets[-1]:
			addr = client.read_int(addr + offset)

	return addr + offsets[-1]


def unlimitedAmmo():
	client.write_int(getPointer(module + 0x0012CB90, [0x810,0x56C,0xA4,0x1D0]),9999)
	client.write_int(getPointer(module + 0x000FAB48, [0x228,0xF8,0x2B4,0x494]),9999)


root = Tk()		
root.title('Assualt Cube MENU')
root.geometry("1200x900")

IMG = PhotoImage(file='wp2487379_1200x900.png')

mycanvas = Canvas(root, width=1200, height=900)
mycanvas.pack(fill='both', expand=True)
mycanvas.create_image(0,0, anchor=NW, image=IMG)

activate_unlimited_ammo = Button(root, text='Set ALL Ammo 9999 ',padx=50, pady=50, font=('Calibri', 20),activebackground='black', activeforeground='white', relief=SUNKEN, command=unlimitedAmmo)

activate_unlimited_ammo_window = mycanvas.create_window(10,10,anchor=NW,window=activate_unlimited_ammo,)


if __name__ == '__main__':
	root.mainloop()
