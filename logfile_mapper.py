#!/usr/bin/env python
#
# This file has been provided as a starting point. You need to modify this file.
# Reads whole lines stdin; writes key/value pairs to stdout
# http://docs.aws.amazon.com/emr/latest/ReleaseGuide/UseCase_Streaming.html
# --- DO NOT MODIFY ANYTHING ABOVE THIS LINE ---

import sys
import time
import datetime

        for line in sys.stdin:
            line = line.rstrip()
            words = line.split('[')
   		words = words[1].split(' -0800') #Sample Output 07/Mar/2004:16:10:02
   		time = datetime.datetime.strptime(words[0], "%d/%b/%Y:%H:%M:%S")
   		print time.strftime('%Y-%m')+"\t1"
