class TheSilent:
    def __init__(self,data,a=-1,verbose=False):
        self.data = data
        self.a = a
        self.verbose = verbose

    def chain(self):
        hits = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                hits.append(self.data[i][j])
        return hits;
            
    def flatten(self):
        new_data = self.data
        if self.a == -1:
            while True:
                if self.verbose:
                    print(f"{new_data}\n")

                if isinstance(new_data, dict):
                    new_data = list(new_data.items())
                    
                if isinstance(new_data[0], list) or isinstance(new_data[0], tuple):
                    new_data = list(TheSilent(new_data).chain())

                if any([True if isinstance(i,dict) else False for i in new_data]):
                    add = []
                    for i in new_data:
                        if isinstance(i,dict):
                            add += list(i.items())

                        else:
                            add.append(i)

                    new_data = list(add[:])

                if any([True if isinstance(i,list) or isinstance(i,tuple) else False for i in new_data]):
                    add = []
                    for i in new_data:
                        if isinstance(i,list) or isinstance(i,tuple):
                            add += i

                        else:
                            add.append(i)

                    new_data = list(add[:])

                else:
                    break
        else:
            for i in range(self.a):
                if self.verbose:
                    print(f"{new_data}\n")
                    
                if isinstance(new_data, dict):
                    new_data = list(new_data.items())

                if isinstance(new_data[0], list) or isinstance(new_data[0], tuple):
                    new_data = list(TheSilent(new_data).chain())

                if any([True if isinstance(i,dict) else False for i in new_data]):
                    add = []
                    for i in new_data:
                        if isinstance(i,dict):
                            add += list(i.items())

                        else:
                            add.append(i)
                    new_data = list(add[:])

                if any([True if isinstance(i,list) or isinstance(i,tuple) else False for i in new_data]):
                    add = []
                    for i in new_data:
                        if isinstance(i,list) or isinstance(i,tuple):
                            add += i

                        else:
                            add.append(i)

                    new_data = list(add[:])

        return new_data

    def mean(self):
        return sum(self.data) / len(self.data)
