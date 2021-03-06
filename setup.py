from setuptools import setup, find_packages

setup(name='hassmart-home-assistant-frontend',
      version='20171217.0',
      description='The Hassmart frontend, powered by homeassistant',
      url='https://github.com/hassmart/home-assistant-polymer',
      author='The Home Assistant Authors',
      author_email='hello@home-assistant.io',
      license='Apache License 2.0',
      packages=find_packages(include=[
          'hass_frontend',
          'hass_frontend_es5',
          'hass_frontend.*',
          'hass_frontend_es5.*'
      ]),
      include_package_data=True,
      zip_safe=False)
