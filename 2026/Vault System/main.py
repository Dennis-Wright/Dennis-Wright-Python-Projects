import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
# End function

def display_banner():
    banner = r"""
             __     __   ______   __    __  __     ________         ______   __      __  ______   ________  ________  __       __ 
            /  |   /  | /      \ /  |  /  |/  |   /        |       /      \ /  \    /  |/      \ /        |/        |/  \     /  |
            $$ |   $$ |/$$$$$$  |$$ |  $$ |$$ |   $$$$$$$$/       /$$$$$$  |$$  \  /$$//$$$$$$  |$$$$$$$$/ $$$$$$$$/ $$  \   /$$ |
            $$ |   $$ |$$ |__$$ |$$ |  $$ |$$ |      $$ |         $$ \__$$/  $$  \/$$/ $$ \__$$/    $$ |   $$ |__    $$$  \ /$$$ |
            $$  \ /$$/ $$    $$ |$$ |  $$ |$$ |      $$ |         $$      \   $$  $$/  $$      \    $$ |   $$    |   $$$$  /$$$$ |
             $$  /$$/  $$$$$$$$ |$$ |  $$ |$$ |      $$ |          $$$$$$  |   $$$$/    $$$$$$  |   $$ |   $$$$$/    $$ $$ $$/$$ |
              $$ $$/   $$ |  $$ |$$ \__$$ |$$ |_____ $$ |         /  \__$$ |    $$ |   /  \__$$ |   $$ |   $$ |_____ $$ |$$$/ $$ |
               $$$/    $$ |  $$ |$$    $$/ $$       |$$ |         $$    $$/     $$ |   $$    $$/    $$ |   $$       |$$ | $/  $$ |
                $/     $$/   $$/  $$$$$$/  $$$$$$$$/ $$/           $$$$$$/      $$/     $$$$$$/     $$/    $$$$$$$$/ $$/      $$/                                                                                                                                                                                
    """

    print(banner)
# End function


# This is to be changed to look better, just a placeholder atm for testing.
def display_options():
    print("\n             [1] Login")
    print("             [2] Register")
    print("             [3] Exit")
# End function

if __name__ == "__main__":
    clear_screen()
    display_banner()
    display_options()
