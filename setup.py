from setuptools import setup, find_packages

setup(
    name='st_webcam',
    version='0.0.3',    
    description='Effortless webcam integration for computer vision projects with Streamlit.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SaarthRajan/st_webcam',
    author='SaarthRajan',
    author_email='saarth.rajan@uwaterloo.ca',
    license='MIT',
    packages=find_packages(),  # Automatically discover packages
    keywords=['Computer Vision', 'Streamlit', 'Python', 'Webcam', 'Artificial Intelligence'],
    install_requires=[
        "opencv-python>=4.0.0,<5.0.0",
        "streamlit>=1.0.0,<2.0.0"
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
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Video"
    ]
)
