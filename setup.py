from setuptools import setup, find_packages

setup(
    name='pydictvalidator',             
    version='1.0.0',                   
    packages=find_packages(),           
    install_requires=[],                
    author='Pandiselvi',                 
    author_email='pandiselvi024@gmail.com', 
    description='A Python package to validate JSON dictionaries', 
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    url='https://github.com/yourusername/pydictvalidator',  # URL of the project repository
    classifiers=[
        'Programming Language :: Python :: 3',           # Indicates compatibility with Python 3
        'License :: OSI Approved :: MIT License',        # License type
        'Operating System :: OS Independent',            # OS compatibility
    ],
    python_requires='>=3.6',  # Specifies minimum Python version
)
