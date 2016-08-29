import logging
import pytest

from testfixtures import LogCapture

import watchmaker


@pytest.fixture
def setup_object():
    pass


class Arguments:
    noreboot = False
    sourceiss3bucket = False
    logger = False
    config = 'config.yaml'
    log_path = '.'
    saltstates = None

    def __init__(self):
        return


def test_default_params():
    with LogCapture(level=logging.WARNING) as l:
        arguments = Arguments()
        systemprep = watchmaker.Prepare(arguments)
        assert not systemprep.noreboot
        assert not systemprep.s3
        assert systemprep.log_path == arguments.log_path
        assert systemprep.config_path == arguments.config
        l.check(
            ('root', 'WARNING', 'Stream logger is not enabled!')
        )


def test_bad_logging_path():
    with LogCapture(level=logging.ERROR) as l:
        arguments = Arguments()
        arguments.log_path = 'z:/not_a_path.txt'
        arguments.logger = True
        watchmaker.Prepare(arguments)
        l.check(
            ('root', 'ERROR', '{0} does not exist'.format(arguments.log_path))
        )


def test_main():
    """Placeholder for tests"""
    # Placeholder
    assert watchmaker.__version__ == watchmaker.__version__
