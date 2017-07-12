class StatusResourceParser(object):

    def parse(self, crsctl_output):
        result_map = {}
        output_parts = crsctl_output.split('\n\n')
        for part in output_parts:
            part_lines = part.split('\n')
            if part_lines[0].startswith('NAME'):
                name = part_lines[0].split('=')[1]
                states = list(map(str.strip, part_lines[3].split('=')[1].split(',')))
                if name not in result_map:
                    result_map[name] = {}
                for state in states:
                    if state.startswith('OFFLINE'):
                        astate = ['OFFLINE', '?']
                    else:
                        astate = list(map(str.strip, state.split('on')))
                    if astate[0] not in result_map[name]:
                        result_map[name][astate[0]] = []
                    result_map[name][astate[0]].append(astate[1])
            else:
                continue

        return result_map


class CheckCrsParser(object):

    _services = {'Oracle High Availability Services': 'HAS', 'Cluster Ready Services': 'CRS',
                 'Cluster Synchronization Services': 'CSS', 'Event Manager': 'EM'}

    def parse(self, crsctl_output):
        result_map = {}
        lines = crsctl_output.split('\n')
        for line in lines:
            for service in self._services:
                if (service in line) and 'online' in line:
                    result_map[self._services[service]] = 'ONLINE'

        for service in self._services:
            if self._services[service] not in result_map:
                result_map[self._services[service]] = 'OFFLINE'

        return result_map
