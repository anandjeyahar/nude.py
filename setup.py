try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='nudepy',
      version='0.2',
      description="Nudity detection with Python. Port of nude.js to Python.",
      long_description=open('README.md').read(),
      author='Software Mechanic',
      author_email='softwaremechanic32@gmail.com',
      url='https://github.com/softwaremechanic/nude.py',
      license='GPLv2',
      platforms='Linux',
      py_modules=['nude'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'],
      keywords="nude",
      zip_safe=False,
      install_requires=['pillow'],
      entry_points={'console_scripts': ['nudepy = nude:main']},
      )
