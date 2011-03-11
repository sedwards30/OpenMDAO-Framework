

import unittest
import os
import shutil
import tempfile
from subprocess import check_call

from openmdao.main.plugin import plugin_quickstart, plugin_build_docs, plugin_makedist
from openmdao.util.fileutil import find_files

class PluginsTestCase(unittest.TestCase):
    def setUp(self):
        self.tdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tdir)

    def test_quickstart(self):
        argv = ['foobar', '-v', '1.1', '-d', self.tdir]
        plugin_quickstart(argv)
        fandd = find_files(self.tdir, nodirs=False)
        self.assertEqual(set([os.path.basename(f) for f in fandd]), 
                         set(['foobar', 'src', 'docs', 'setup.cfg', 'setup.py',
                              'MANIFEST.in', '__init__.py', 'conf.py', 'usage.rst', 'index.rst',
                              'srcdocs.rst', 'pkgdocs.rst', 'foobar.py', 
                              'README.txt',
                              'test','test_foobar.py']))
    
    def test_makedist(self):
        argv = ['foobar', '-v', '1.1', '-d', self.tdir]
        plugin_quickstart(argv)
        
        startdir = os.getcwd()
        try:
            os.chdir(self.tdir)
            plugin_makedist(['foobar'])
            self.assertTrue(os.path.exists('foobar-1.1.tar.gz'))
        finally:
            os.chdir(startdir)

if __name__ == '__main__':
    unittest.main()
    
