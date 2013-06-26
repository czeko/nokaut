from setuptools import find_packages, setup

setup (
	name='nokaut',
	version='0.1.1',
	author='Malwina Nowakowska',
	author_email = 'malwina.nowakowska@stxnext.pl',
	packages=find_packages(),

	#packages=['tests','lib'],
	#scripts=['lib/nokaut.py', 'lib/funkcja.py'],
	#script_name='nokaut',
	#py_modules=['nokaut'],
	entry_points="""\
		[console_scripts]
		nokaut=nokaut.script:main
	""",
	description='zadnianie z nokaut',
	long_description = 'README.txt',
	install_requires=[
		'python >= 2.7',
		'lxml',
	],
)
