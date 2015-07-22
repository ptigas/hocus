from fabric.api import *

env.user = 'ptigas'
env.hosts = ['ptigas.com']

def deploy():
	with cd('repos/hocus'):
		run('git pull')				

	with cd('repos/hocus/webapp'):
		run('composer install')

	with cd('repos/hocus'):
		run('cp -r webapp/* ~/Sites/hocus.io/')	
		run('cp -r vendor ~/Sites/hocus.io/.')