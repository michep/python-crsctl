import io
import json
from crsctl import parser, checker

f = io.open('crsctl_output_2.txt').read()
config = json.load(io.open('config_2.json'))
crsctl_parser = parser.StatusResourceParser()
crsctl_checker = checker.StatusResourceChecker()
res = crsctl_parser.parse(f)
check = crsctl_checker.check(config, res)
print(check)
print("="*30)
f = io.open('crsctl_output_3.txt').read()
check_parser = parser.CheckCrsParser()
res = check_parser.parse(f)
print(res)