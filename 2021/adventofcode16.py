# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:26:50 2021

@author: August
"""

raw_packet = "420D598021E0084A07C98EC91DCAE0B880287912A925799429825980593D7DCD400820329480BF21003CC0086028910097520230C80813401D8CC00F601881805705003CC00E200E98400F50031801D160048E5AFEFD5E5C02B93F2F4C11CADBBB799CB294C5FDB8E12C40139B7C98AFA8B2600DCBAF4D3A4C27CB54EA6F5390B1004B93E2F40097CA2ECF70C1001F296EF9A647F5BFC48C012C0090E675DF644A675DF645A7E6FE600BE004872B1B4AAB5273ED601D2CD240145F802F2CFD31EFBD4D64DD802738333992F9FFE69CAF088C010E0040A5CC65CD25774830A80372F9D78FA4F56CB6CDDC148034E9B8D2F189FD002AF3918AECD23100953600900021D1863142400043214C668CB31F073005A6E467600BCB1F4B1D2805930092F99C69C6292409CE6C4A4F530F100365E8CC600ACCDB75F8A50025F2361C9D248EF25B662014870035600042A1DC77890200D41086B0FE4E918D82CC015C00DCC0010F8FF112358002150DE194529E9F7B9EE064C015B005C401B8470F60C080371460CC469BA7091802F39BE6252858720AC2098B596D40208A53CBF3594092FF7B41B3004A5DB25C864A37EF82C401C9BCFE94B7EBE2D961892E0C1006A32C4160094CDF53E1E4CDF53E1D8005FD3B8B7642D3B4EB9C4D819194C0159F1ED00526B38ACF6D73915F3005EC0179C359E129EFDEFEEF1950005988E001C9C799ABCE39588BB2DA86EB9ACA22840191C8DFBE1DC005EE55167EFF89510010B322925A7F85A40194680252885238D7374C457A6830C012965AE00D4C40188B306E3580021319239C2298C4ED288A1802B1AF001A298FD53E63F54B7004A68B25A94BEBAAA00276980330CE0942620042E3944289A600DC388351BDC00C9DCDCFC8050E00043E2AC788EE200EC2088919C0010A82F0922710040F289B28E524632AE0"

#raw_packet = "9C0141080250320F1802104A08"



def parse(package,I,versions):
    i = I
    messages = []
    VERSION = package[i+0:i+3]
    versions.append(int(VERSION,2))
    TYPE = package[i+3:i+6]
    print(TYPE)
    if TYPE == "100": 
        MESSAGE = ""
        i += 6
        while package[i] == "1":
            MESSAGE += package[i+1:i+5]
            i += 5
        MESSAGE += package[i+1:i+5]
        i += 5
        MESSAGE = int(MESSAGE,2)
        messages.append(MESSAGE)
    else:
        if(package[i+6] == "0"):
            LENGTH = int(package[i+7:i+22],2)
            last_i = i + 22 + LENGTH
            i += 22
            while i < last_i:
                MESSAGE,i = parse(package,i,versions)
                messages.append(MESSAGE)
        else:
            NUM_PACKAGES = int(package[i+7:i+18],2)
            i += 18
            for __ in range(NUM_PACKAGES):
                MESSAGE,i = parse(package,i,versions)
                messages.append(MESSAGE)
        if TYPE == "000":
            #sum
            newmessage = 0
            for message in messages:
                if type(message) == list:
                    newmessage += sum(message)
                else:
                    newmessage += message
        elif TYPE == "001":
            #product
            newmessage = 1
            for message in messages:
                if type(message) == list:
                    newmessage *= sum(message)
                else:
                    newmessage *= message
        elif TYPE == "010":
            #min
            newmessage = []
            for message in messages:
                if type(message) == list:
                    newmessage.append(sum(message))
                else:
                    newmessage.append(message)
            newmessage = min(newmessage)
        elif TYPE == "011":
            #max
            newmessage = []
            for message in messages:
                if type(message) == list:
                    newmessage.append(sum(message))
                else:
                    newmessage.append(message)
            newmessage = max(newmessage)
        elif TYPE == "101":
            #greater than
            if messages[0] > messages[1]:
                newmessage = 1
            else:
                newmessage = 0
        elif TYPE == "110":
            #less than
            if messages[0] < messages[1]:
                newmessage = 1
            else:
                newmessage = 0
        elif TYPE == "111":
            #equal
            if messages[0] == messages[1]:
                newmessage = 1
            else:
                newmessage = 0
        messages = newmessage
    return(messages,i)
            

packet = bin(int("1"+raw_packet,16))[3:]
        
versions = []
print(parse(packet,0,versions))