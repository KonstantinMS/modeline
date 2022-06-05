import re

class monitor():
    def __init__(self, str):
        self._inputStr = str
        self.parse()

    # todo: data check
    def isValid(self):
        pass

    def parse(self):
        paramList = self._inputStr.split(' ')
        paramNames = ['name', 'Pixel Clock', 'HRes', 'HSyncStart', 'HSyncEnd', 'HTotal',
                      'VRes', 'VSyncStart', 'VSyncEnd', 'VTotal']
        self.params = dict(zip(paramNames, paramList[1:11] ))
        self.params['HSync'] = str(int(self.params['HSyncEnd']) - int(self.params['HSyncStart']))
        self.params['VSync'] = str(int(self.params['VSyncEnd']) - int(self.params['VSyncStart']))

    def getFreq(self):
        pass

    def getName(self):
        return (re.findall(r"\"(.+)\"", self._inputStr))

    def printParam(self):
        print(self.params)

    def printDefines(self):
        s=''
        s += r'// ' + self.params['name'] + '\n'
        s += r'// pix clk ' + self.params['Pixel Clock'] + ' MHz\n'
        s += r'`define VISIBLE_X       ' + self.params['HRes'] + '\n'
        s += r'`define VISIBLE_Y       ' + self.params['VRes'] + '\n'
        s += r'`define SYNC_X_BEGIN    ' + self.params['HSyncStart'] + '\n'
        s += r'`define SYNC_X_END      ' + self.params['HSyncEnd'] + '\n'
        s += r'`define SYNC_Y_BEGIN    ' + self.params['VSyncStart'] + '\n'
        s += r'`define SYNC_Y_END      ' + self.params['VSyncEnd'] + '\n'
        s += r'`define WHOLE_X         ' + self.params['HTotal'] + ' - 1' + '\n'
        s += r'`define WHOLE_Y         ' + self.params['VTotal'] + ' - 1' + '\n'
        print(s)

if __name__ == '__main__':
    m = monitor(r'ModeLine "800x600" 40.00 800 840 968 1056 600 601 605 628 +HSync +VSync');
    m.printDefines()