#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from cuckoo.main import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.argv[0] = sys.argv[0] + '-d' # Enable verbose logging
    sys.exit(main())
