
class StatusResourceParser(object):

    def parse(self, crsctl_output):
        crsctl_map = {}
        output_parts = crsctl_output.split('\n\n')
        for part in output_parts:
            part_lines = part.split('\n')
            if part_lines[0].startswith('NAME'):
                name = part_lines[0].split('=')[1]
                states = list(map(str.strip, part_lines[3].split('=')[1].split(',')))
                if not name in crsctl_map:
                    crsctl_map[name] = {}
                for state in states:
                    astate = list(map(str.strip, state.split('on')))
                    if not astate[0] in crsctl_map[name]:
                        crsctl_map[name][astate[0]] = []
                    crsctl_map[name][astate[0]].append(astate[1])
            else:
                continue

        return crsctl_map
