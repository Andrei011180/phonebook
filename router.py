# Связь между view и db
from view import *
from db import *

def main():
    while True:
        ans = select_op()
        if ans == 1:
            name = get_name()
            res_str = write_name(name)
            print_info(res_str)
        elif ans == 2:
            char = get_som_info()
            full_lst, accept_lst, res_str = searh_name(char)
            print_info(accept_lst, res_str)
        elif ans == 3:
            char = get_som_info() 
            full_lst, accept_lst, res_str = searh_name(char) 
            print_info(accept_lst, res_str)
        
        elif ans == 4:
            selected_num = select_name()
            new_line = None
            new_line = get_name()
            res_str = change_name(full_lst, accept_lst[selected_num], new_line)
            prin_info(res_str)
        elif ans == 5:
            res_str = get_all
            print_info(res_str)
        elif ans == 6:
            break         

main()           
