import sys


def plugin_loaded():
    try:
        from package_control import events

        if events.install('package_control-tester'):
            print('Installed %s!' % events.install('package_control-tester'))
        elif events.post_upgrade('package_control-tester'):
            print('Upgraded to %s!' % events.post_upgrade('package_control-tester'))
        else:
            print('Loaded!')

    except (ImportError):
        print('Loaded!')


def plugin_unloaded():
    try:
        from package_control import events

        if events.pre_upgrade('package_control-tester'):
            print('Upgrading from %s!' % events.pre_upgrade('package_control-tester'))
        elif events.remove('package_control-tester'):
            print('Removing %s!' % events.remove('package_control-tester'))
        else:
            print('Unloading!')

    except (ImportError):
        print('Unloading!')


# Compat with ST2 - unfortunately there is no way to replicate plugin_unloaded()
if sys.version_info < (3,):
    plugin_loaded()
