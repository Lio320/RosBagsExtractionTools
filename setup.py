from setuptools import setup, find_packages
import os

setup(
    name='rosbag-extraction-tool',  # Choose a name for your package
    version='0.1.0',  # Start with a version number
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'rosbag',
        'cv_bridge',
        'tqdm',
        'rospy', # Add rospy as dependency
        'pycryptodomex',
        'gnupg',
        'PyYaml',
        'rospkg',
    ],
    entry_points={
        'console_scripts': [
            'extract = extract:main_cli',  # Command to run your script
        ],
    },
    author='Leonardo Saraceni',  # Replace with your name
    author_email='saracenileonardo01@gmail.com', # Replace with your email
    description='Extract data from ROS bag files for specified topics.',
    long_description=open('README.md').read() if os.path.exists('README.md') else '', # Optional README
    long_description_content_type='text/markdown', # If you use Markdown for README
    url='https://github.com/Lio320/RosBagsExtractionTools.git', # Replace with your project's URL if you have one
    license='MIT',  # Choose a license (e.g., MIT, GPL, Apache 2.0)
)