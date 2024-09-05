from setuptools import setup, find_packages
from linux_command.linux_command import VERSION, PROJECT_URL


setup(
    name='linux-command',
    version=VERSION,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cmd=linux_command.linux_command:main',
        ],
    },
    install_requires=[],
    author='Mouxiao Huang',
    author_email='huangmouxiao@gmail.com',
    description='A command line tool to perform custom tasks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url=PROJECT_URL,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
