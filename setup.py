from distutils.core import setup

setup(
    name='ndrive',
    packages=['ndrive'],
    version='0.0.1',
    description='python wrapper for Naver Ndrive',
    long_description=open('README.md').read(),
    license='MIT License',
    author='Kim Tae Hoon',
    author_email='carpedm20@gmail.com',
    url='https://github.com/carpedm20/ndrive',
    keywords=['Ndrive','ndrive'],
    classifiers=[],
    install_requires=[
        'requests',
        'python-magic',
        'clint',
        'json',
    ]
)
