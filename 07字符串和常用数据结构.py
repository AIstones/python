def main():
    str1 = 'hello, world!'
    print(len(str1))  # 13
    print(str1.capitalize()) #Hello, world!
    print(str1.upper())  #HELLO, WORLD!
    print(str1.find('or')) #8
    print(str1.find('shit')) #-1
    print(str1.startswith('He')) #False
    print(str1.startswith('hel')) #True

    print(str1.endswith('!'))
    print(str1.center(20, '*')) #***hello, world!****
    print(str1.rjust(20, ' '))
if __name__ == '__main__':
    main()