
#!/usr/bin/env python
# encoding:utf-8
import sys
from pylint.lint import Run
from pylint.reporters.text import TextReporter
from cStringIO import StringIO
filename = sys.argv[1]
args = ['--errors-only', filename]
my_output = StringIO()
reporter = TextReporter(output=my_output)
Run(args, reporter=reporter, exit=False)
output_str = my_output.getvalue()
print "len %d characters" % len(output_str)
print "Got %s characters" % output_str