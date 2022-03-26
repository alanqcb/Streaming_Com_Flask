from setuptools import setup

setup(
    name='streaming_service',
    packages=['streaming_service'],
    include_package_data=True,
    install_requires=[
        'flask',
        'watchdog',
        'opencv-python',
        'scipy',
        'psutil',
        'numpy'
    ],
)
