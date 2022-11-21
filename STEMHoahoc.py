import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os
from pyowm import OWM

def H():
    temp = "Hydrogen"
    print("Tên Tiếng Anh: Hydrogen")
    print("Kí hiệu: H")
    print("Số hiệu nguyên tử: 1")
    print("Nguyên Tử khối trung bình: 1,008")
    print("Độ âm điện: 2,20")
    print("Số oxi hóa: -1,1")
    print("Nhóm 1A")
    print("Chu kì: 1")
    wb.open('https://vi.wikipedia.org/wiki/' + temp)
def He():
    temp = Helium
    print("Tên Tiếng Anh: Helium")
    print("Kí hiệu: He")
    print("Số hiệu nguyên tử: 2")
    print("Nguyên Tử khối trung bình: 4,003")
    print("Độ âm điện: Không có")
    print("Số oxi hóa: Không có")
    print("Nhóm: 8A")
    print("chu kì: 1")
    wb.open('https://vi.wikipedia.org/wiki/' + temp)
def Li():
    print("Tên Tiếng Anh: Lithium")
    print("Kí hiệu: Li")
    print("Số hiệu nguyên tử: 3")
    print("Nguyên Tử khối trung bình: 6,94")
    print("Độ âm điện: 0,98")
    print("Số oxi hóa: 1")
    print("Nhóm: 1A")
    print("chu kì: 2")
def Be():
    print("Tên Tiếng Anh: Berylium")
    print("Kí hiệu: Be")
    print("Số hiệu nguyên tử: 4")
    print("Nguyên Tử khối trung bình: 9,01")
    print("Độ âm điện: 1,57")
    print("Số oxi hóa: 2")
    print("Nhóm: 2A")
    print("chu kì: 2")
def B():
    print("Tên Tiếng Anh: Boron")
    print("Kí hiệu: B")
    print("Số hiệu nguyên tử: 5")
    print("Nguyên Tử khối trung bình: 10,81")
    print("Độ âm điện: 2,04")
    print("Số oxi hóa: 3")
    print("Nhóm: 3A")
    print("chu kì: 2")     
while True:
    user = str(input("Nhập dữ liệu bạn cần tìm: ")).lower()
    if (user == 'h') or (user == '1') or (user == 'Hydrogen') or (user == '2,20'):
        H()
    elif (user == "He") or (user == "2") or (user == "Helium"):
        He()
    elif (user == "quit") or (user == 'thoát') or (user == "exit"):
        print('<-------------------------------->')
        print("Chương Trình đã tắt, chào tạm biệt")
        print('Made by Tony')
        print('<-------------------------------->')
        quit()    