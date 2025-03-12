str = "sdfsdfds sdfsdf sdfdsfsd sdfdsf ydbangalore@gmail.com"

import re

print(re.findall(r'\w+@\w+.\w+', str))
