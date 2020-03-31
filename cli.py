"""CLI FOR DEVOPS"""
import os
import sys
import subprocess


# Ensure dependencies
need_install = []
try:
    from PyInquirer import prompt
except ImportError:
    need_install.append("PyInquirer")

try:
    import cprint
except ImportError:
    need_install.append("cprint")


class CLI:
    """系统devops脚手架,方便部署以及进入docker"""

    _VERSION = "0.0.1"
    # constants
    BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    BASE_SCRIPT_PATH = os.path.join(BASE_PATH, "scripts")
    # shell scripts
    CHECK_PROJECT_REPO_STATUS_SCRIPT = os.path.join(BASE_SCRIPT_PATH,
                                                    "check-project.sh")
    UPDATE_DOCKER_IMAGES = os.path.join(BASE_SCRIPT_PATH,
                                        "update-docker-images.sh")
    ENTER_DOCKER_CONTAINER_SCRIPT = os.path.join(BASE_SCRIPT_PATH,
                                                 "enter-docker-container.sh")
    DOCKER_COMPOSE_UP_SCRIPT = os.path.join(BASE_SCRIPT_PATH,
                                            "docker-compose-up.sh")
    DOCKER_COMPOSE_DOWN_SCRIPT = os.path.join(BASE_SCRIPT_PATH,
                                              "docker-compose-down.sh")

    def __get_check(self, configuration):
        return prompt(configuration).get('main')

    def __run_script(self, operation=None):
        if operation:
            subprocess.run(operation.split())

    def __check_project_repo_status(self):
        operation_expression = "bash {script}".format(
            script=self.CHECK_PROJECT_REPO_STATUS_SCRIPT
        )
        self.__run_script(operation=operation_expression)

    def __update_docker_images(self):
        pass

    def __enter_container(self):
        pass

    def __docker_compose_up(self):
        pass

    def __docker_compose_down(self):
        pass

    def __main(self):
        choices = [
            'Check project repo status',
            'Update docker images',
            'Enter a docker container'
            'Docker compose up',
            'Docker compose down',
        ]
        configuration = {
            'type': 'list',
            'name': 'main',
            'message': '选择一个操作',
            'choices': choices,
            'filter': lambda val: val.lower()
        }
        checked = self.__get_check(configuration)
        if checked == "check project repo status":
            self.__check_project_repo_status()
        elif checked == "update docker images":
            self.__update_docker_images()
        elif checked == "enter a docker container":
            self.__enter_container()
        elif checked == "docker compose up":
            self.__docker_compose_up()
        elif checked == "docker compose down":
            self.__docker_compose_down()
        sys.exit()

    def run(self):
        self.__main()
