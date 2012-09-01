import glob
import re

from keyword import kwlist
from nose import tools as nt
from underscore import _

KEYWORDS = set(kwlist) | {'type', 'xrange'}
IDENTIFER_REGEX = '[a-zA-Z][a-zA-Z0-9]*'

def testGenerator():
    for filename in glob.glob('examples/*.py'):
        yield _testFile, filename

def _ids(code):
    return re.findall(IDENTIFER_REGEX, code)

def _testFile(filename):
    error_msg = 'Id "{id}" on line {lineno} did not get converted'
    underscored = _(filename)
    last_line = len(underscored.splitlines()) - 1
    for lineno, line in enumerate(underscored.splitlines()):
        identifers = _ids(line)
        if lineno in (0,1, last_line) or 'import' in identifers:
            continue
        if 'class' in filename:
            continue
        for identifer in identifers:
            nt.assert_in(identifer, KEYWORDS,
                         error_msg.format(id=identifer, lineno=lineno))

