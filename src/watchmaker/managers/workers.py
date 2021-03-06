import json

from watchmaker.managers.base import (LinuxManager, WindowsManager,
                                      WorkersManagerBase)
from watchmaker.workers.salt import SaltLinux, SaltWindows
from watchmaker.workers.yum import Yum


class LinuxWorkersManager(WorkersManagerBase):
    """

    """

    def __init__(self, s3, system_params, execution_scripts, saltstates):
        super(LinuxWorkersManager, self).__init__()
        self.execution_scripts = execution_scripts
        self.manager = LinuxManager()
        self.s3 = s3
        self.system_params = system_params
        self.saltstates = saltstates

    def _worker_execution(self):
        pass

    def _worker_validation(self):
        pass

    def worker_cadence(self):

        for script in self.execution_scripts:
            configuration = json.dumps(
                self.execution_scripts[script]['Parameters']
            )

            if 'Yum' in script:
                yum = Yum()
                yum.install(configuration)
            elif 'Salt' in script:
                salt = SaltLinux()
                salt.install(configuration, self.saltstates)

    def cleanup(self):
        self.manager.cleanup()


class WindowsWorkersManager(WorkersManagerBase):
    """

    """

    def __init__(self, s3, system_params, execution_scripts, saltstates):
        super(WindowsWorkersManager, self).__init__()
        self.execution_scripts = execution_scripts
        self.manager = WindowsManager()
        self.s3 = s3
        self.system_params = system_params
        self.saltstates = saltstates

    def _worker_execution(self):
        pass

    def _worker_validation(self):
        pass

    def worker_cadence(self):
        for script in self.execution_scripts:
            configuration = json.dumps(
                self.execution_scripts[script]['Parameters']
            )

            if 'Salt' in script:
                salt = SaltWindows()
                salt.install(configuration, self.saltstates)

    def cleanup(self):
        self.manager.cleanup()
