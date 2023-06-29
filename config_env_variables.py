# import enviromentsVariable.json

import os
import json
import sys

# enviromentsVariable.json
variables_to_load = json.load(open("enviromentsVariable.json"))

def success_message(message):
    print("\033[92m[+]\033[0m " + message)

def error_message(message):
    print("\033[91m[-]\033[0m " + message)

def warning_message(message):
    print("\033[93m[!]\033[0m " + message)

def info_message(message):
    print("\033[94m[i]\033[0m " + message)

def input_value(message):
    return input("\033[95m[?]\033[0m " + message)


def check_if_variable_exist(variable_name, folder_name, file_name):
    path = os.path.join("..",folder_name, file_name)
    try:
        with open(path, "r") as f:
            for line in f.readlines():
                if variable_name in line:
                    return True
    except:
        return False
    
def check_if_file_exist(folder_name, file_name):
    path = os.path.join("..",folder_name, file_name)
    try:
        with open(path, "r") as f:
            return True
    except:
        return False

def create_file(folder_name, file_name):
    path = os.path.join("..",folder_name, file_name)
    # write nothing
    with open(path, "w") as f:
        f.write("")
    return True

def create_variable(variable_name, folder_name, file_name):
    path = os.path.join("..",folder_name, file_name)
    # write nothing
    with open(path, "a") as f:
        f.write(variable_name + "=")
    return True

def write_variable(variable_name, variable_value, folder_name, file_name):
    path = os.path.join("..",folder_name, file_name)
    # write in a new line
    with open(path, "a") as f:
        line = "\n" + variable_name + "=" + variable_value
        f.write(line)

   
    return True

def rewrite_variable(variable_name, variable_value, folder_name, file_name):
    path = os.path.join("..",folder_name, file_name)
    # write nothing
    with open(path, "r") as f:
        lines = f.readlines()
    with open(path, "w") as f:
        for line in lines:
            if variable_name in line:
                line = variable_name + "=" + variable_value + "\n"
            f.write(line)
    return True

def delete_variable(variable_name, folder_name, file_name):
    path = os.path.join("..",folder_name, file_name)
    # write nothing
    with open(path, "r") as f:
        lines = f.readlines()
    with open(path, "w") as f:
        for line in lines:
            if variable_name not in line:
                f.write(line)
    return True

def show_help():
    print("Usage:")
    print("python3 config_env_variables.py [OPTION]")
    print("")
    print("Options:")
    print("--help\t\t\tShow this help message")
    print("--clear\t\t\tDelete all variables")
    print("")
    print("Variables to load:")

   
    for variable in variables_to_load:
        variable_name = variable["varName"]
        folder_name = variable["folders"]
        file_name = variable["fileName"]
        print(variable_name + ":") 
        # bold
        print("\t" + "\033[1m" + "Description:" + "\033[0m")
        print("\t" + variable["description"])
        print("\t" + "\033[1m" + "File:" + "\033[0m")
        for folder in folder_name:
            print("\t\t\t\t\t\t" + folder["folderName"] + "/" + file_name)

# main  

def get_variable_value_if_exist_in_other_file(variable_name, folder_name, file_name):
    path = os.path.join("..",folder_name, file_name)
    try:
        with open(path, "r") as f:
            for line in f.readlines():
                if variable_name in line:
                    return line.split("=")[1]
    except:
        return None

if __name__ == "__main__":
    

    if sys.version_info[0] < 3:
        error_message("Please use Python version 3 or greater.")
        exit(1)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            show_help()
            exit(0)

    # clean: delete all variables
    if len(sys.argv) > 1:
        if sys.argv[1] == "--clear":
            for variable in variables_to_load:
                variable_name = variable["varName"]
                folders = variable["folders"]
                file_name = variable["fileName"]
                for folder in folders:
                    folder_name = folder["folderName"]
                    if check_if_file_exist(folder_name, file_name):
                        if check_if_variable_exist(variable_name, folder_name, file_name):
                            delete_variable(variable_name, folder_name, file_name)
                            success_message("Variable " + variable_name + " was deleted in " + folder_name + "/" + file_name)
                        else:
                            success_message("Variable " + variable_name + " was not deleted in " + folder_name + "/" + file_name + " because it does not exist")
                    else:
                        success_message("File " + folder_name + "/" + file_name + " was not deleted because it does not exist")
            exit(0)
    


    for variable in variables_to_load:
        variable_name = variable["varName"]
        folders = variable["folders"]
        file_name = variable["fileName"]

        variable_value = None
        variable_found_in_other_file = False

        for folder in folders:
            folder_name = folder["folderName"]
            if check_if_file_exist(folder_name, file_name):
                if check_if_variable_exist(variable_name, folder_name, file_name):
                    variable_value = get_variable_value_if_exist_in_other_file(variable_name, folder_name, file_name)
                    break


        if variable_value == None:
            variable_value = input_value("Enter value for " + variable_name + ":")
        

        for folder in folders:
            
            folder_name = folder["folderName"]

            # revisa si la variable está definida en otro archivo (folder y file) y si es así, entonces se utiliza ese valor
            
            



            if folder["required"]:
                if check_if_file_exist(folder_name, file_name):
                    if check_if_variable_exist(variable_name, folder_name, file_name):
                        success_message("Variable " + variable_name + " was rewritten in " + folder_name + "/" + file_name)
                    else:
                        path_file = os.path.join("..",folder_name, file_name)
                        write_variable(variable_name, variable_value, folder_name, file_name)
                        success_message("Variable " + variable_name + " was written in " + folder_name + "/" + file_name)
                else:
                    create_file(folder_name, file_name)
                    success_message("File " + folder_name + "/" + file_name + " was created")
                    create_variable(variable_name, folder_name, file_name)
                    path_file = os.path.join("..",folder_name, file_name)
                    write_variable(variable_name, variable_value, folder_name, file_name)
                    success_message("Variable " + variable_name + " was written in " + folder_name + "/" + file_name)
            else:
                if check_if_file_exist(folder_name, file_name):
                    if check_if_variable_exist(variable_name, folder_name, file_name):
                        success_message("Variable " + variable_name + " was rewritten in " + folder_name + "/" + file_name)
                    else:
                        path_file = os.path.join("..",folder_name, file_name)
                        write_variable(variable_name, variable_value, folder_name, file_name)
                        success_message("Variable " + variable_name + " was written in " + folder_name + "/" + file_name)
                else:
                    success_message("File " + folder_name + "/" + file_name + " was not created because it is not required")
    

        # for folder in folders:
        #     folder_name = folder["folderName"]
        #     if folder["required"]:
        #         if check_if_file_exist(folder_name, file_name):
        #             if check_if_variable_exist(variable_name, folder_name, file_name):
        #                 success_message("Variable " + variable_name + " was rewritten in " + folder_name + "/" + file_name)
        #             else:
        #                 path_file = os.path.join("..",folder_name, file_name)
        #                 variable_value = input_value("Enter value for " + variable_name + " ("+ path_file+") : ")
        #                 write_variable(variable_name, variable_value, folder_name, file_name)
        #                 success_message("Variable " + variable_name + " was written in " + folder_name + "/" + file_name)
        #         else:
        #             create_file(folder_name, file_name)
        #             success_message("File " + folder_name + "/" + file_name + " was created")
        #             create_variable(variable_name, folder_name, file_name)
        #             path_file = os.path.join("..",folder_name, file_name)
        #             variable_value = input_value("Enter value for " + variable_name + " ("+ path_file+") : ")
        #             write_variable(variable_name, variable_value, folder_name, file_name)
        #             success_message("Variable " + variable_name + " was written in " + folder_name + "/" + file_name)
        #     else:
        #         if check_if_file_exist(folder_name, file_name):
        #             if check_if_variable_exist(variable_name, folder_name, file_name):
        #                 success_message("Variable " + variable_name + " was rewritten in " + folder_name + "/" + file_name)
        #             else:
        #                 path_file = os.path.join("..",folder_name, file_name)
        #                 variable_value = input_value("Enter value for " + variable_name + " ("+ path_file+") : ")
        #                 write_variable(variable_name, variable_value, folder_name, file_name)
        #                 success_message("Variable " + variable_name + " was written in " + folder_name + "/" + file_name)
        #         else:
        #             success_message("File " + folder_name + "/" + file_name + " was not created because it is not required")

