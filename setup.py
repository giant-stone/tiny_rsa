try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='tiny_rsa',
    version='0.0.1',
    url='https://github.com/giant-stone/tiny_rsa',
    license='MIT License',
    author='tony95271',
    author_email='63030915+tony95271@users.noreply.github.com',
    description='RSA in pure Python',

    keywords='rsa',
    
    packages = [
        "tiny_rsa",
        "tiny_rsa.tests",
    ],
    test_suite ="tiny_rsa.tests",
)
