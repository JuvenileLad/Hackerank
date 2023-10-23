import re
if __name__ == '__main__':
    N = int(input())
    userInp = []
    for n in range(N):
        # split the 'command' and 'arguments'
        userInp.append(re.split(r'\s+', input(), 1))

    # commands that require arguments
    attrib_commands = ["insert", "remove", "append"]

    main_list = []

    for action in userInp:
        if len(action) > 1:
            # split the arguments further if more than one arguments like in insert
            attribs = action[1].split()
            if action[0] == "insert":
                function = f"main_list.{ action[0] }({ int(attribs[0])}, {int(attribs[1]) })"
            else:
                function = f"main_list.{action[0]}({ attribs[0] })"
        elif action[0] == "print":
            function = f"print(main_list)"
        else:
            function = f"main_list.{ action[0] }()"
        eval(function)
