class dict_found(dict):
    def get(self, key):
        if key in self:
            return self[key]
        else:
            return 'Zero'


new_dict = dict_found()
new_dict[1] = 11
new_dict[2] = 22
new_dict[3] = 33
print(new_dict.get(4))