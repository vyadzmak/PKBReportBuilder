import sys
import modules.shell_starter_modules.shell_starter_module as shell_starter
import models.settings.config as config
import modules.xml_parser.xml_parser as xml_parser
import datetime
import logging
import models.export_models.export_styles as styles

# init system settings
def init_system():
    try:
        # init config
        config.init_config()
        #init styles
        styles.init_styles()
    except Exception as e:
        logging.error("Crash init system procedure. " + str(e))


# entry point project
if __name__ == '__main__':
    try:
        result =""
        t = datetime.datetime.now()
        start_time = datetime.datetime.now()
        init_system()
        args_count = len(sys.argv)
        if (args_count > 1):
            shell_starter.cli()
        else:
            xml_parser.parse_file(config.test_parse_file_full_path)

        execution_time = datetime.datetime.now() - start_time
        logging.info("Execution time = " + str(execution_time))

    except Exception as e:
        logging.error("Error core procedure. " + str(e))
