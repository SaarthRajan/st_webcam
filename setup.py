from setuptools import setup

setup(
    name='st_webcam',
    version='0.0.1',    
    description='Effortless webcam integration for computer vision projects with Streamlit.',
    url='https://github.com/SaarthRajan/st_webcam',
    author='Saarth Rajan',
    author_email='saarth.rajan@uwaterloo.ca',
    license='MIT',
    packages=['st_webcam'],
    install_requires=[
        "opencv-python==4.10.0.84",
        "streamlit==1.39.0"
    ],

    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Computer Vision",
        "Topic :: Software Development :: Libraries :: Streamlit",
        "Natural Language :: English",
    ]
)