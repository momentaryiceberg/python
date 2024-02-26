
def val0():
    print("Val 0 valið")

def val1():
    print("Val 1 valið")

def val2():
    print("Val 2 valið")

def val3():
    print("Val 3 valið")

def val4():
    print("Val 4 valið")

def val5():
    print("Val 5 valið")

def val6():
    print("Val 6 valið")

def val7():
    print("Val 7 valið")

def val8():
    print("Val 8 valið")

def val9():
    print("Val 9 valið")

def main():
    while True:
        print("Veldu eitthvað af þessu eða 'q' til að hætta: ")
        print("1 fyrir val 1")
        print("2 fyrir val 2")
        print("3 fyrir val 3")
        print("4 fyrir val 4")
        print("5 fyrir val 5")
        print("6 fyrir val 6")
        print("7 fyrir val 7")
        print("8 fyrir val 8")
        print("9 fyrir val 9")
        print("0 fyrir val 0")
        val = input("Hvað viltu? ")
        if val == '1':
            val1()
        elif val == '2':
            val2()
        elif val == '3': 
            val3()
        elif val == '4':
            val4()
        elif val == '5':
            val5()
        elif val == '6':
            val6()
        elif val == '7':
            val7()
        elif val == '8':
            val8()
        elif val == '9':
            val9()
        elif val.lower() == 'q':
            print("Fer út úr þessu....")
            break
        else:
            print("Eitthvað að, veldu aftur")

if __name__ == "__main__":
    main()