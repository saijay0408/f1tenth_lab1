import os
from glob import glob
from setuptools import setup

package_name = 'lab1_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='saijay0408',
    maintainer_email='sai2001jayanth@gmail.com',
    description='talker and relay nodes',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = lab1_pkg.talker:main',
            'relay = lab1_pkg.relay:main',
        ],
    },
)
