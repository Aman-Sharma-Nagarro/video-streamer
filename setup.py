# import setup function from 
# python distribution utilities
from distutils.core import setup 
  
# Calling the setup function
setup(
      name = 'vidstrm',
      version = '1.0.0',
      py_modules = ['camera', 'backend'],
      author ='Aman Sharma',
      author_email = 'aman.sharma@nagarro.com',
      url = 'https;//ageek.com',
      description = 'video streamer',
      keywords='video streamer',
)