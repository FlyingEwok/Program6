'''Write a Python program to convert an integer to a roman numeral. '''

#Make class that determines the roman numeral
class convintroman:
    def intToRoman(self, num):
        #make lists that have the changes in the roman numeral at the right int
        value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        romanNum = ''
        i = 0
        
        #Cycle through value list till appropriate number is found
        while  num > 0:
            for _ in range(num // value[i]):
                #Make romanNum variable be the value of i in the symbol list
                romanNum += symbol[i]
                #Reset num value to zero
                num -= value[i]
            i += 1
        return romanNum

#Print the roman numeral of the number inputed by user
print(convintroman().intToRoman(int(input("Enter a number: "))))