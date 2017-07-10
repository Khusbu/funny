from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='funny',
      version='0.1',
      description='The funny joke in the world',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funny joke comedy flying circus',
      url='https://github.com/Khusbu/funny',
      download_url = 'https://github.com/Khusbu/funny/archive/0.1.tar.gz',
      author='Khusbu Mishra',
      author_email='meetkhusbumishra@example.com',
      license='MIT',
      packages=['funny'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)
