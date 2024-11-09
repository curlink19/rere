import os
import glob
import logging
from functools import partial

logger = logging.getLogger(__name__)


def test_each_test_attached_to_file(caplog):
    """
    Each test file in rere test subdirectory must correspond in \
        relative path to a file from rere and must test the code in this file.
    """
    caplog.set_level(logging.INFO)

    assert "tests" in glob.glob("*"), "can't identify tests directory"

    _get_relative_path = lambda root_path, x: x[len(root_path) + 1 :].replace(
        "test_", ""
    )

    _get_python_files = lambda root_path: list(
        map(
            partial(_get_relative_path, root_path),
            glob.glob(os.path.join(root_path, "**/*.py"), recursive=True),
        )
    )

    rere_files = _get_python_files("rere")
    test_files = _get_python_files("tests/rere")

    for relative_path in test_files:
        assert relative_path in rere_files, str(relative_path) + " not found in rere"

    logger.info(
        str(len(test_files))
        + " out of "
        + str(len(rere_files))
        + " files somehow tested"
    )
