import logging

logging.basicConfig(filename='test6.log', level=logging.DEBUG,
                    format= '[%(levelname)s]: %(asctime)s : %(name)s : %(message)s')


class Tuples:

    def __init__(self,t):
        logging.info('Class initialization started. data added to constructor')
        self.tuples = t

    def get_tuple(self):
        try:
            logging.info('Enter the function which gives tuple from given list')
            logging.debug('Result of the function given below')
            m = []
            for i in self.tuples:
                if type(i) == tuple:
                    m.append(i)
            logging.debug(m)
            return m
        except Exception as e:
            logging.error(e)

    def get_elements(self,start,stop,step=1):
        try:
            logging.info('Enter the function which gives range of elements in tuple')
            logging.debug('Result of the function given below')
            logging.info(self.tuples[start:stop:step])
            return self.tuples[start:stop:step]
        except Exception as e:
            logging.error(e)


l = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]