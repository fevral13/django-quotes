from setuptools import setup

setup(
    name='django-quotes',
    version='0.1',
    description="Quotes application for Django.",
    #long_description=open('README.markdown').read(),
    author='Dave Merwin',
    author_email='',
    url='https://github.com/fevral13/django-quotes',
    packages=['quotes', 'quotes.templatetags'],
    #data_files=['quotes/templates/quotes/random_quote.html'],
    package_data={'quotes': ['templates/quotes/*.html']},
    #data_files=[('quotes', ['templates/quotes/*.html',])],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
