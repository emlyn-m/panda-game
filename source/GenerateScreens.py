from BinaryTree import BinaryTree

NUM_SCREENS = 15  # Total
EXISTING_SCREENS = 30
SCREENPATH = "../assets/lvlScreens/"

def bubblesort(lst):
    pass  # Sort by difficulty tag

def genScreen(fPath):
    pass

def generateScreens():
    screens = []
    for x in range(NUM_SCREENS):
        screenNum = random.randint(EXISTING_SCREENS)
        screens += genScreen(SCREENPATH + screenNum)

    screens = bubblesort(screens)  # Fix if byref

    # TODO: Convert to binary tree
    gameBTree = BinaryTree()
    while screens != []:
        instruction = random.choose(["lr", "l", "r", ""])

        if instruction == "lr" and len(screens) > 2:
            gameBTree.insertLeft(screens[0])
            gameBTree.insertRight(screens[1])
            screens = screens[2:]

        elif instruction == "l":
            gameBTree.insertLeft(screens[0])
            screns = screens[1:]

        elif instruction == "r":
            gameBTree.insertRight(screens[0])
            screens = screens[1:]

    return gameBTree
