import os,sys,time,base64,pyperclip

from colorama import Fore,Style

# COLORS

cyan = Fore.CYAN
yellow = Fore.YELLOW
white = Fore.WHITE
red = Fore.RED
blue = Fore.BLUE
black = Fore.BLACK
green = Fore.GREEN

THIS_VER = '1.1'

def main():
    os.system('cls')

    banner = blue + f'''
    

                   _____  .____   __________  ___ ___    _____    ________   _____  
                  /  _  \ |    |  \______   \/   |   \  /  _  \  /  _____/  /  |  | 
                 /  /_\  \|    |   |     ___/    ~    \/  /_\  \/   __  \  /   |  |_
                /    |    \    |___|    |   \    Y    /    |    \  |__\  \/    ^   /
                \____|__  /_______ \____|    \___|_  /\____|__  /\_____  /\____   | 
                        \/        \/               \/         \/       \/      |__| 
                                            v{THIS_VER}


    '''

    options = cyan + f'''
    
    {yellow}[{red}1{yellow}]{red} Exit
    {yellow}[{green}2{yellow}]{red} Encrypt a message
    {yellow}[{green}3{yellow}]{red} Decrypt a message
    {yellow}[{green}4{yellow}]{red} Developer

    '''

    devvv = cyan + f'''
    
    A fancy base64 encryption tool made by Vez Codez

    {blue}Discord                 {yellow}-       {cyan}Sfyx#1222
    {blue}VezCodez's Community    {yellow}-       {cyan}https://discord.gg/PpqYechhcr
    {blue}Website                 {yellow}-       {cyan}http://vezcodez.c1.biz
    {blue}Github                  {yellow}-       {cyan}https://github.com/vezcodes/about
    
    '''

    print(banner)
    print(options)

    option = input(f"{yellow}[{green}>{yellow}]{cyan} option: ")

    if option == "1":
        os.system('cls')
        print(banner)
        input(green + " Press [ ENTER ] to exit :D")
        quit()

    elif option == "2":
        os.system('cls')
        print(banner)
        Encryptt = input(Fore.CYAN + f" Message to encrypt{yellow}:{cyan} ")
        # enc1 = base64.b64encode(Encryptt)
        # enc2 = base64.b64encode(enc1)

        sample_string = f"{Encryptt}"
        sample_string_bytes = sample_string.encode("ascii")
        
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    

        print(cyan + f"{yellow}[{green}>{yellow}]{cyan} {base64_string}")
        pyperclip.copy(base64_string)
        spam = pyperclip.paste()
        input(cyan + "\n\n  Press [ ENTER ] to return T.T")
        main()

    elif option == "3":
        os.system('cls')
        print(banner)
        Decryptt = input(cyan + f"  Message to decrypt{yellow}:{cyan} ")
        # de1 = base64.b64decode(Decryptt)
        # de2 = base64.b64decode(de1)

        base64_string = f"{Decryptt}"
        base64_bytes = base64_string.encode("ascii")
        
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        

        print(cyan + f"{yellow}[{green}>{yellow}]{cyan} {sample_string}")
        pyperclip.copy(sample_string)
        spam = pyperclip.paste()
        input(cyan + "\n\n  Press [ ENTER ] to return T.T")
        main()

    elif option == "4":
        os.system('cls')
        print(banner)
        print(devvv)
        input(cyan + "  Press [ ENTER ] to return :D")
        main()

    else:
        # print(red + "[!] invalid option!")
        # input(cyan + "Press [ ENTER ] to return :-D")
        main()

    main()


if __name__ == '__main__':
    main()