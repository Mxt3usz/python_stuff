from optimizer import opt_all, show_node
from expr_parser import parse

while True:
    written = ""
    user_input = input(">  ")
    written += user_input
    if user_input == "quit":
        print("Good bye!")
        break
    else:
        a = opt_all(parse(written))
        if a[0] == None:
            print("Invalid Input.")
        else:
            for nodes in a:
                print("=",show_node(nodes))
        
