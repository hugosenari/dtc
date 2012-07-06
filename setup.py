'''
Created on Jun 1, 2012

@author: hugosenari
'''
from distutils.core import setup

setup(name='dtc',
      version='0.1',
      description='Python plugnplay interfaces for app runner',
      author='hugosenari',
      author_email='hugosenari@gmail.com',
      url='https://github.com/hugosenari/dtc',
      keywords = ["plugnplay", "script runner"],
      packages=('dtc', 'dtc.core', 'dtc.modules', 'dtc.core.interfaces', 'dtc.core.utils'),
      requires=('plugnplay (>=4.0)', ),
      license = "GPL",
      classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: X11 Applications",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Programming Language :: Python :: 2.7"
      ],
      long_description = """\
          DTC have one objective
          
          Create simple way to run batch/app script
          
          This are base for others 
          
          * Linux python app runner (included)
          * Windows python app runner
          * Mac pythonn app runner
          
          For some reason I can't make windows and mac versions, feel free to implement.
      """
)