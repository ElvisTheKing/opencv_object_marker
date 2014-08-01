from setuptools import setup

setup(
    name='opencv_object_marker',
    version='0.1.0',
    description='simple tool to mark up objects in positive images collection for opencv cascade classifier training, requires opencv for python',
    url='https://github.com/ElvisTheKing/opencv_object_marker',
    author='Sergey Konyukhovskiy',
    license='MIT',
    scripts=['bin/opencv_object_marker'],
    install_requires = [
        'click==2.1',
    ],
)
