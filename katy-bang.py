import os
import sys
import time
mrx ='''\x1b[1;92m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
▓──────────────────────────────────────▓
▓────▄▀────────────▄▀───────────▄▀─────▓
▓────▀▄───────────▐█────────────▀▄─────▓
▓────▄█▄───────────▀▄───────────▄█▄────▓
▓──▄▀░░░▀▄──────────▌─────────▄▀░░░▀▄──▓
▓─▐░░░░░░░▌──────▄▄▀▀▄▄──────▐░░░░░░░▌─▓
▓──▀▄░░░▄▀─────▄▀░░░░░░▀▄─────▀▄░░░▄▀──▓
▓───▐███▌─────▐█░░░░░░░░█▌─────▐███▌───▓
▓───▐░░░▌─────██▀▀▀▀▀▀▀▀██─────▐░░░▌───▓
▓▄▄▄▐░█░▌▄▄▄▄▄████████████▄▄▄▄▄▐░█░▌▄▄▄▓
▓──────────────────────────────────────▓
▓─██▀▀▄ ─▄▄─ █▀▄▀█ ─▄▄─ █▀▀▄ ─▄▄─ █▄──██ ──▓
▓─██▄▄▀ █▄▄█ █─█─█ █▄▄█ █──█ █▄▄█ █─█─██ ──▓
▓─██──█ █──█ █───█ █──█ █──█ █──█ █─█─██ ──▓
▓─██──█ █──█ █───█ █──█ █▄▄▀ █──█ █─█─██ ──▓
▓─██──█ ──── ───── ──── ──── ──── █──▀██ ──▓
▓──────────────────────────────────────▓
▓───██───██─█─█─██▄─▄█▄─█▀▀▄─▄█▄─█─────▓
▓───███─███─█─█─█─█─█─█─█──█─█─█─█─█▀──▓
▓───█──█──█─█─█─█▀█─█▀█─█▐█▀─█▀█─█▀▄───▓
▓───█─────█─█─█─█─█─█─█─█─█──█─█─█─█───▓
▓───█─────█─███─██▀─█─█─█─█▄─█─█─█─█▄──▓
▓──────────────────────────────────────▓
▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
              by @i4m_mrx
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ '''
print (mrx)
print('\033[92m KAT' '  ' + time.ctime(time.time()))
print("1-kirkuk")
print("2-hawlir")
print("3-slimany")
print("4-dhok")
print("5-halabja")
halo =input("HALBZHER : ")
if halo == '1':
	os.system("clear")
	os.system("python kirkuk.py")
if halo == '2':
	os.system("clear")
	os.system("python hawlir.py")
if halo == '3':
	os.system("clear")
	os.system("python slimany.py")
if halo == '4':
	os.system("clear")
	os.system("python dhok.py")
if halo == '5':
	os.system("clear")
	os.system("python halabja.py")

	
