import io
from crsctl import parser, checker


config = {
    'nodes': 'dbrac1,dbrac2',
    'ora.dbrac1.vip':'dbrac1',
    'ora.dbrac2.vip': 'dbrac2',
    'ora.LISTENER.lsnr': 'all',
    'ora.asm': 'all',
    'ora.CRSDATA.dg': 'all',
    'ora.DATA.dg': 'all',
    'ora.VOTENFS.dg': 'all',
    'ora.testdb.db': 'all',
    'ora.testdb.testdbinst1.svc': 'dbrac2',
    'ora.testdb.testdbinst2.svc': 'dbrac2',
    'ora.testdb.testdbsrv.svc': 'all',
    'ora.LISTENER_SCAN1.lsnr': 'any',
    'ora.LISTENER_SCAN2.lsnr': 'any',
    'ora.scan1.vip': 'any',
    'ora.scan2.vip': 'any'
}

file = io.open('crsctl_output.txt')
f = file.read()
crsctl_parser = parser.StatusResourceParser()
crsctl_checker = checker.StatusResourceChecker()
res = crsctl_parser.parse(f)
check = crsctl_checker.check(config, res)

print(check)
