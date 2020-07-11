
class config:
    def __init__(self, filename):
        self.filename = filename
        self.filedata = ""
        # get file data
        with open(filename) as f:
            self.filedata = f.read()
        
        
        self.data = {}
        current_point = ""
        # store each datapoint. A datapoint is the first word on any given line.
        for s in self.filedata.split(' '):
            if self.data == {}:
                # start a new datapoint
                self.data[s] = []
                current_point = s
            elif len(s.split('\n')) > 1:
                # Because we only split at spaces, if we find a '\n' we need to start a new datapoint
                # store last data to the datapoint
                self.data[current_point].append(s.split('\n')[0])
                # start a new datapoint
                self.data[s.split('\n')[-1]] = []
                current_point = s.split('\n')[-1]
            else:
                # append data to datapoint
                self.data[current_point].append(s)
    def get_datapoint(self, datapoint, default=[]):
        # make sure we have that datapoint
        if not datapoint in self.data:
            # error if we couldn't find it and return default
            print("ircsome: Couldn't find '" + datapoint + "' in config. Defaulting to " + default + ".")
            return default
        # return the datapoint they were looking for
        return self.data[datapoint]