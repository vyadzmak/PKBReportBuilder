import sys
import modules.shell_starter_modules.shell_starter_module as shell_starter
import models.settings.config as config

def init_system():
    try:
        #init config
        config.init_config()
        pass
    except Exception as e:
        pass

#entry point project
if __name__ == '__main__':
    try:
        init_system()
        args_count =len(sys.argv)
        if (args_count>1):
            shell_starter.cli()
    except Exception as e:
        pass
