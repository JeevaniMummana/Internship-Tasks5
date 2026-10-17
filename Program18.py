def minion_game(string):
    # your code goes here
    vowels = "AEIOU"

    kevin = 0
    stuart = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)