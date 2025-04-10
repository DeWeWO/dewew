from setuptools import setup, find_packages

setup(
    name='dewew',
    version='0.0.7',
    packages=find_packages(),
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
    install_requires=[
        'colorama',
        'requests',
    ],
    python_requires='>=3.6',
    license='MIT',
)
