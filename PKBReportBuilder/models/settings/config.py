import os, sys
import modules.logging.logging as logging_config

import json
import logging

# root dir
root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

#logs dir full path
logs_dir_full_path =""

#logs dir name
logs_dir_name ="logs"

#configs dir full path
configs_dir_full_path =""

#configs dir name
configs_dir_name ="configs"

#data dir full path
data_dir_full_path =""

#data dir name
data_dir_name ="data"

# engine version code
version_code = "0.1"

#build version code
build_version_code =-1

# engine name
engine_name = "PKB Report Builder"

# system name
system_name = "PKB Report Builder Engine"

# show all info when running
show_system_info_on_start = False

#logging config file name
logging_config_file_name = "logging.yaml"

#logging config file full pat
logging_config_file_full_path = ""


#buildcode file name
build_code_file_name = "build_code.json"

#logging config file full pat
build_code_file_full_path = ""

#test parse file
test_parse_file_name = "78477.xml"

#test parse file full path
test_parse_file_full_path = ""

#configs dir full path
exports_dir_full_path =""

#configs dir name
exports_dir_name ="exports"

#export json file full path
export_json_file_full_path = ""

#export json file name
export_json_file_name = "data.json"

# all versions
versions_container = [
    ["0.1", "Leonardo"],
    ["0.2", "Donatello"],
    ["0.3", "Raphael"],
    ["0.4", "Michelangelo"],
    ["0.5", "Splinter"],

]


# --------------- methods---------------#
#load and increase build version
def load_build_version():
    try:

        with open(build_code_file_full_path) as f:
            data = json.load(f)
            global build_version_code
            build_version_code= int(data["build_version_code"])
            build_version_code+=1
            data["build_version_code"] = build_version_code

        with open(build_code_file_full_path, "w") as jsonFile:
            json.dump(data, jsonFile)
            t=0
        pass
    except Exception as e:
        pass

def get_version_name():
    try:
        versions = versions_container
        current_version_code = version_code

        for version in versions:
            if (version[0] == current_version_code):
                return version[1]

        pass
    except Exception as e:
        return str(e)
        pass

#join system paths
def join_path(paths):
    try:
        path = os.path.join(*paths)
        path =os.path.normpath(path)
        # path =os.path.normcase(path)
        return path
    except Exception as e:
        return str(e)


# show start info
def show_system_info():
    try:
        print("Start init configuration")
        print("Root dir : "+root_dir)
        print("System name : "+system_name)
        print("Engine name : "+engine_name)
        print("Engine version code: "+version_code)
        print("Engine version name: "+get_version_name())
        print("Build version code: "+str(build_version_code))


        pass
    except Exception as e:
        pass

#config system paths
def config_paths():
    try:
        global configs_dir_full_path
        configs_dir_full_path = join_path([root_dir,configs_dir_name])

        global logging_config_file_full_path
        logging_config_file_full_path =join_path([configs_dir_full_path,logging_config_file_name])

        global build_code_file_full_path
        build_code_file_full_path = join_path([configs_dir_full_path,build_code_file_name])

        global logs_dir_full_path
        logs_dir_full_path = join_path([root_dir,logs_dir_name])

        global data_dir_full_path
        data_dir_full_path = join_path([root_dir, data_dir_name])

        global test_parse_file_full_path
        test_parse_file_full_path = join_path([data_dir_full_path,test_parse_file_name])

        global exports_dir_full_path
        exports_dir_full_path = join_path([root_dir, exports_dir_name])

        global export_json_file_full_path
        export_json_file_full_path = join_path([exports_dir_full_path, export_json_file_name])

        t=0
        pass
    except Exception as e:
        pass

# init config
def init_config():
    try:
        config_paths()
        load_build_version()
        logging_config.setup_logging(default_path=logging_config_file_full_path)


        if (show_system_info_on_start == True):
            show_system_info()

        logging.info("Config init successful")

    except Exception as e:
        logging.error(str(e))
        pass
