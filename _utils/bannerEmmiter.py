def bannerEmmiter(authors, info, aditional_nfo):
    print()
    print("  ______   ______   _   __  ______   ______   ")
    print(" |_    _| |  __  | | | / / |  ____| |  __  |  ")
    print("   |  |   | |  | | | |/ /  | |__    | |__| |  ")
    print("   |  |   | |  | | |   <   |  __|   |     <   ")
    print("  _|  |   | |__| | | |\ \  | |____  |  |\  \  ")
    print(" |____|   |______| |_| \_\ |______| |__| \__\ ")
    print()

    print("[Info] %s" % info)
    print("  || %s" % aditional_nfo)
    if len(authors) > 1:
        print("  || Autores:")
        for author in authors:
            print("  ||   %s" % author)
    else:
        print("  || Autor: %s" % authors[0])