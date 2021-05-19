from setuptools import setup

setup(
    name='django-loki',
    version='0.1.0',
    packages=['django_loki'],
    url='https://github.com/zepc007/django-loki',
    license='MIT',
    author='zepc007',
    author_email='zepc007@gmail.com',
    description='logging handler with loki for django',
    keywords=['python', 'loki', 'grafana', 'logging', 'metrics'],
    install_requires=[
        'requests',
        'pytz',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Environment :: Web Environment",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 3 - Alpha '
    ],
)
