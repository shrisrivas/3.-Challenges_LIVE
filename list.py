#
# l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
# 1 . Try to reverse a list
# 2. try to access 234 out of this list
# 3 . try to access 456
# 4 . Try to extract only a list collection form list l
# 5 . Try to extract "sudh"
# 6 . Try to list all the key in dict element avaible in list
# 7 . Try to extract all the value element form dict available in list
import logging
logging.basicConfig(filename="test3.log" ,level = logging.INFO)
logging.info("this is code for logging ")

class list:
    """list operation task implementation using oops and parameterisation and init(object call during runtime.)"""
    def __init__(self,l):
        logging.info('list Constructor is called....')
        self.l=l
    def reverse(self):
        """try to reverse the list"""
        try:
            logging.info('reversing all list entity from the collection')
            return self.l[::-1]
        except Exception as e:
            logging.error(e)
    def extract_234(self):
        """try to access 234 out of this list"""
        try:
            logging.info('Accessing 234 from List without for loop')
            for i in self.l:
                if type(i) == tuple:
                    for j in i:
                        if j == 234:
                            logging.info(j)
        except Exception as e:
            logging.error(e)
    def access_456(self):
        """try to access 456 """
        try:
            logging.info('Accessing 234 from List without for loop')
            for i in self.l:
                if type(i) == list:
                    print(i)
                    for j in i:
                        if j == 456:
                            logging.info(j)
        except Exception as e:
            logging.error(e)
    def extract(self):
        """Try to extract only a list collection form list l"""
        try:
            logging.info('extracting all list entity from the collection')
            for i in self.l:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def extract_sudh(self):
        """Try to extract "sudh"""
        try:
            logging.info("extract_sudh")
            for i in self.l:
                if type(i) == dict:
                    print(i)
                    for j in i:
                        if j[1] == 'sudh':
                            logging.info(j)
        except Exception as e:
            logging.error(e)

    def extract_dict(self):
        """Try to list all the key in dict element avaible in list"""
        try:
            logging.info("extract_dict")
            for i in self.l:
                for i in self.l:
                    if type(i) == dict:
                        print(dict)
                        for j in i.keys():
                            logging.info(j)
        except Exception as e:
            logging.error(e)


    def extract_dict_values(self):
        """Try to extract all the value element form dict available in list """
        try:
            logging.info("extract_dict_values")
            for i in self.l:
                if type(i) == dict:
                    for j in i.values():
                        logging.info(j)
        except Exception as e:
            logging.error(e)

a=list([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])
print(a.reverse()
