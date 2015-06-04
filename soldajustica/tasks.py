from invoke import (run, task,)


@task
def heroku(command):
    run('heroku run:detached {0}'.format(command))
    

@task
def manage(command):
    heroku('python soldajustica/manage.py {0}'.format(command))


@task
def migrate(app=''):
    manage('migrate {0}'.format(app))


@task
def deploy():
    run('git push heroku')
    manage('migrate')