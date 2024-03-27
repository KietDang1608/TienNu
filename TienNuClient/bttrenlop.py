class Map:
    def __init__(self, number):
        self.list = []
        self.__mapAdd(number)
    def __mapAdd(self,number):
        for item in number:
            self.list.append(item)
            
class MapSubClass(Map):
    def mapAdd(self, keys,values):
        for i in zip(keys, values):
            self.list.append(i)
def main():
    number_list = [1,2,3,4,5]
    map_instance = Map(number_list)
    print("Map list =", map_instance.list)
    key = ['one','two','three']
    map_subclass_instance = MapSubClass([])
    map_subclass_instance.mapAdd(key,number_list)
    print(map_subclass_instance.list)
main()