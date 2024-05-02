
import os
while True:
    print()
    print('Press X and Enter to continue.')
    print()
    
    checkInputf1 = input('')
    if checkInputf1.lower() == 'x':
        os.system('cls')
        def splitfunc(Num):
            Num = int(Num)  # Convert the value to an integer
            splitNumSyntax = [] # The values will be stored as [hundreds, tens, ones]
            while Num > 0: # Check if the value is greater than 0
                splitNumSyntax.append(Num % 10)
                Num //= 10
            return splitNumSyntax[::-1]
        
        Num = input('Enter a number: ')

        if int(Num) <= 100:
            
            digits = splitfunc(int(Num))
            num_digits = len(str(Num))

            if num_digits == 3:
                finalform = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digits[0] == 1:
                    roi = str('หนึ่งร้อย')
                else:
                    print('error')
                if digits[1] == 1:
                    sib = str('สิบ')
                elif digits[1] == 2:
                    sib = str('ยี่สิบ')
                elif digits[1] == 3:
                    sib = str('สามสิบ')
                elif digits[1] == 4:
                    sib = str('สี่สิบ')
                elif digits[1] == 5:
                    sib = str('ห้าสิบ')
                elif digits[1] == 6:
                    sib = str('หกสิบ')
                elif digits[1] == 7:
                    sib = str('เจ็ดสิบ')
                elif digits[1] == 8:
                    sib = str('แปดสิบ')
                elif digits[1] == 9:
                    sib = str('เก้าสิบ')
                elif digits[1] == 0:
                    sib = str('')
                else:
                    print('error')
                
                if digits[2] == 1:
                    nuay = str('เอ็ด')
                elif digits[2] == 2:
                    nuay = str('สอง')
                elif digits[2] == 3:
                    nuay = str('สาม')
                elif digits[2] == 4:
                    nuay = str('สี่')
                elif digits[2] == 5:
                    nuay = str('ห้า')
                elif digits[2] == 6:
                    nuay = str('หก')
                elif digits[2] == 7:
                    nuay = str('เจ็ด')
                elif digits[2] == 8:
                    nuay = str('แปด')
                elif digits[2] == 9:
                    nuay = str('เก้า')
                elif digits[2] == 0:
                    nuay = str('')
                else:
                    print('error')
                print((finalform) + "อ่านว่า" ,str(roi),str(sib),str(nuay))
            elif  num_digits == 2:
                finalform = str(digits[0]) + str(digits[1])
                if digits[0] == 1:
                    sib = str('สิบ')
                elif digits[0] == 2:
                    sib = str('ยี่สิบ')
                elif digits[0] == 3:
                    sib = str('สามสิบ')
                elif digits[0] == 4:
                    sib = str('สี่สิบ')
                elif digits[0] == 5:
                    sib = str('ห้าสิบ')
                elif digits[0] == 6:
                    sib = str('หกสิบ')
                elif digits[0] == 7:
                    sib = str('เจ็ดสิบ')
                elif digits[0] == 8:
                    sib = str('แปดสิบ')
                elif digits[0] == 9:
                    sib = str('เก้าสิบ')
                elif digits[0] == 0:
                    sib = str('')
                else:
                    print('error')
                if digits[1] == 1:
                    nuay = str('เอ็ด')
                elif digits[1] == 2:
                    nuay = str('สอง')
                elif digits[1] == 3:
                    nuay = str('สาม')
                elif digits[1] == 4:
                    nuay = str('สี่')
                elif digits[1] == 5:
                    nuay = str('ห้า')
                elif digits[1] == 6:
                    nuay = str('หก')
                elif digits[1] == 7:
                    nuay = str('เจ็ด')
                elif digits[1] == 8:
                    nuay = str('แปด')
                elif digits[1] == 9:
                    nuay = str('เก้า')
                elif digits[1] == 0:
                    nuay = str('')
                else:
                    print('error')
                print((finalform) , " อ่านว่า " , str(sib),str(nuay))
            elif  num_digits == 1:
                finalform = digits[0]
                if digits[0] == 1:
                    nuay = str('หนึ่ง')
                elif digits[0] == 2:
                    nuay = str('สอง')
                elif digits[0] == 3:
                    nuay = str('สาม')
                elif digits[0] == 4:
                    nuay = str('สี่')
                elif digits[0] == 5:
                    nuay = str('ห้า')
                elif digits[0] == 6:
                    nuay = str('หก')
                elif digits[0] == 7:
                    nuay = str('เจ็ด')
                elif digits[0] == 8:
                    nuay = str('แปด')
                elif digits[0] == 9:
                    nuay = str('เก้า')
                elif digits[0] == 0:
                    nuay = str('ศูนย์')
                print((finalform) , " อ่านว่า " , str(nuay))
            else:
                print('error')
        else:
            print('IM was so lazy and he decide to not coding for number that much than 100 at this time.')
    else:
        break