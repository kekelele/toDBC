#coding:utf-8

import argparse
import xlrd

__version__ = '0.1'




class CanMsg( ):
    def __init__(self, data):
        print data
        self.canid_source = data[0]
        self.canid_hex = data[0][2:]
        self.canid_int = int(data[0], 16)
        self.dlc = int(data[1])
        self.cycleTime = int(data[2][:-2])
        self.orientation = data[3]

    def show(self):
        print self.canid_int,self.dlc,self.cycleTime,self.orientation
def parserExcel( excel_name , sheet_name):
    print excel_name , sheet_name
    workbook = xlrd.open_workbook(excel_name)
    sheet = workbook.sheet_by_name(sheet_name)
    if sheet == None:
        print 'No exist sheet name: %s'%sheet_name
        sys.exit()
    Msgs = []
    for index in range( 1, sheet.nrows ):
        Msgs.append( CanMsg(sheet.row_values(index)) )
    pass

if __name__ == "__main__":
    """[summary]
        usage: use "python main.py --help" for more information

        optional arguments:
            -h, --help            show this help message and exit.
            -v, --version         show program's version number and exit.
            -e, --excel           show J2534 Device Infomation and Dll message.
    """
    parser = argparse.ArgumentParser(
        description = 'For generate DBC',
        version = __version__,
        usage = 'use "python %(prog)s --help" for more information!')
    parser.add_argument(
        '-E',
        '--excel',
        help=' excel file name! '
        )
    parser.add_argument(
        '-S',
        '--sheet',
        help=' sheet name! '
        )

    args = parser.parse_args()

    if args.excel and args.sheet:
        parserExcel( args.excel, args.sheet)