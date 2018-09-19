p = r'E:\code\python\aiporc\main_page.ui'

import re

reg = re.compile(r'.*\.ui$')
r = reg.match(p)
print(r)
