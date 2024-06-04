#   Importing responsories
import argparse
import pytest


#   Importing the test subject
from project import CommandlineInterface, SCChecker

class TestParser():

    '''
        Testing the argparser

    '''

    def Setup(self, cmd):

        ''' Setting up the test'''

        #   Creating a parser
        parser  = argparse.ArgumentParser(prog = 'Site Connectivity Checker', formatter_class= argparse.ArgumentDefaultsHelpFormatter, description= 'Site Connectivity Checker', epilog= 'by @krigjo25')

        #   Initializing command line arguments
        parser.add_argument('-p', '--ping', dest = 'ping', help ='Ping a website', action = 'append')
        parser.add_argument('-u', '--urls', dest = 'urls', metavar = 'URLs', nargs='+', default=[], type= str, help ='urls to check')
        parser.add_argument('-info', '--information', dest = 'info', help = '%(prog)s Information Center', action='store_true')

        return parser.parse_args(cmd)

    def test_parser(self):

      #   Strings to be tested
      url = 'www.cs50.harvard.edu/'
      urls = ['www.vg.no', 'smp.no']
      path = 'test.txt'

      #   Testing commands

      assert self.Setup(['-info'])
      assert self.Setup(['-p', url])
      assert self.Setup(['-u', url])
      assert self.Setup(['-u', urls])
      assert self.Setup(['-u', path])
      assert self.Setup(['-p', path])

      assert self.Setup(['--ping', url])
      assert self.Setup(['--urls', url])
      assert self.Setup(['--ping', path])
      assert self.Setup(['--urls', urls])
      assert self.Setup(['--urls', path])
      assert self.Setup(['--information'])

      return

    def test_RaiseSystemExit(self):
      with pytest.raises(SystemExit):
        self.Setup(['--help'])

      return


class TestProject:

    ''' Testing the function of the projects'''

    def test_PingConnection(self):

      url = ['google.com']
      urls = ['google.com', 'www.pypi.org']
      path = ['test.txt']
      paths = ['demo.txt', 'test.txt']

      p = SCChecker()

      p.PingConnection(url)
      p.PingConnection(urls)
      p.PingConnection(path)
      p.PingConnection(paths)

      return

    def test_UrlConnection(self):

      url = ['google.com']
      urls = ['google.com', 'www.pypi.org']
      path = ['test.txt']
      paths = ['demo.txt', 'test.txt']

      p = SCChecker()

      p.UrlParse(url)
      p.UrlParse(urls)
      p.UrlParse(path)
      p.UrlParse(paths)

      return