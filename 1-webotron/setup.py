from setuptools import setup

setup(
    name='webotron',
    version='1.0',
    author='Aparajit Ananya',
    author_email='aparajitananya9@gmail.com',
    description='Tool to deploy static websites to AWS',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/aparajitananya/aws-python/tree/master/1-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
