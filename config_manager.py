
class config:
    def __init__(self, filename):
        self.filename = filename
        self.filedata = ""
        with open(filename) as f:
            self.filedata = f.read()
        self.data = {}
        current_point = ""
        for s in self.filedata.split(' '):
            if self.data == {}:
                self.data[s] = []
                current_point = s
            elif len(s.split('\n')) > 1:
                self.data[current_point].append(s.split('\n')[0])
                self.data[s.split('\n')[1]] = []
                current_point = s.split('\n')[1]
            else:
                self.data[current_point].append(s)
    def get_point(self, datapoint, default=[]):
        if not datapoint in self.data:
            print("ircsome: Couldn't find '" + datapoint + "' in config. Defaulting.")
            return default
        return self.data[datapoint]