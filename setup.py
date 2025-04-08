from setuptools import setup, find_packages

setup(
    name='dewew',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['requests'],
    author='DeWeW',
    author_email='dewel000per@gmail.com',
    description='GitHub fayllarini yuklovchi oddiy vosita.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DeWeWO/uzb_kitoblar',  # GitHub sahifangiz
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',
)
