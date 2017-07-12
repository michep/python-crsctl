class StatusResourceChecker(object):

    def check(self, config, crsctl):
        result = {'True':[], 'False':[]}
        nodes = config['nodes']
        for cfg in config:
            if cfg == 'nodes':
                continue
            opt = config[cfg]
            if cfg not in crsctl:
                result['False'].append(cfg)
                continue
            if 'ONLINE' not in crsctl[cfg]:
                result['False'].append(cfg)
                continue
            online = crsctl[cfg]['ONLINE']
            if opt == 'all':
                res = self._checkALL(nodes, online)
            elif opt == 'any':
                res = self._checkANY(nodes, online)
            else:
                res = self._checkALL(opt, online)
            result[str(res)].append(cfg)
        return result

    def _checkALL(self, nodes, online):
        opts = nodes.split(',')
        if len(online) != len(opts):
            return False
        for node in opts:
            if node not in online:
                return False
        return True

    def _checkANY(self, nodes, online):
        for node in online:
            if node not in nodes:
                return False
        return True


class CheckCrsChecker(object):

    def check(self, crsctl):
        result = {'True':[], 'False':[]}
        for service in crsctl:
            if crsctl[service] == 'ONLINE':
                result['True'].append(service)
            else:
                result['False'].append(service)
        return result
