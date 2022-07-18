import logging

logging.basicConfig(filename='test5.log', level=logging.DEBUG,
                    format= '[%(levelname)s]: %(asctime)s : %(name)s : %(message)s')


class Dicts:

    def __init__(self, d):
        self.dicts = d

    def get_dicts(self):
        try:
            logging.info('Enter the function which gives tuple from given list')
            logging.debug('Result of the function given below')
            m = []
            for i in self.dict:
                if type(i) == dict:
                    m.append(i)
            logging.debug(m)
            return m
        except Exception as e:
            logging.error(e)

    def get_list_ele(self):
        try:
            logging.info('Enter the function which gives tuple from given list')
            logging.debug('Result of the function given below')
            logging.info(list(self.dicts.items()))
            return list(self.dicts.items())
        except Exception as e:
            logging.error(e)


l = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]
d = Dicts(l)
print(d.get_dicts())
