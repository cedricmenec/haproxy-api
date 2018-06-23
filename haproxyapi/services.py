
import subprocess
from haproxyadmin import haproxy
from haproxyadmin import server as haproxy_server

from .serialization import BackendSchema, ServerSchema

HAPROXY_EXE = 'haproxy'
#HAPROXY_SOCKET_FILE = '/var/run/haproxy.sock'
HAPROXY_SOCKET_FILE = '/var/lib/haproxy/stats'

SYSTEMCTL_EXE = '/bin/systemctl'


def stop():
    """
    Stop haproxy service via systemctl command
    """
    command = ['sudo', SYSTEMCTL_EXE, 'stop', HAPROXY_EXE]
    subprocess.call(command)
    return status()


def start():
    """
    Start haproxy service via systemctl command
    """
    command = ['sudo', SYSTEMCTL_EXE, 'start', HAPROXY_EXE]
    subprocess.call(command)
    return status()

def restart():
    """
    Restart haproxy service via systemctl command
    """
    command = ['sudo', SYSTEMCTL_EXE, 'restart', HAPROXY_EXE]
    subprocess.call(command)
    return status()


def reload():
    """
    Reload haproxy configuration
    """
    command = ['sudo', SYSTEMCTL_EXE, 'reload', HAPROXY_EXE]
    subprocess.call(command)
    return status()


def status():
    """
    Get status of haproxy service
    """
    cmd = "sudo {} status haproxy".format(SYSTEMCTL_EXE)

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout = ''
    for line in p.stdout.readlines():
        stdout += line.decode("utf-8")

    return_code = p.wait()

    result = {}
    result["code"] = return_code

    if return_code == 3:
        result["text"] = "stopped"
    elif return_code == 0:
        result["text"] = "started"
    else:
        result["text"] = "unknow"

    return result


def list_backends():
    hap = haproxy.HAProxy(socket_file=HAPROXY_SOCKET_FILE)
    backends = hap.backends()
    return BackendSchema().dump(backends, many=True).data


def list_servers(backend_name):
    hap = haproxy.HAProxy(socket_file=HAPROXY_SOCKET_FILE)
    backend = hap.backend(backend_name)
    servers = backend.servers()
    return ServerSchema().dump(servers, many=True).data


def get_server(backend_name, server_name):
    hap = haproxy.HAProxy(socket_file=HAPROXY_SOCKET_FILE)
    servers = hap.server(server_name, backend=backend_name)
    if (len(servers) > 0):
        return ServerSchema().dump(servers[0]).data
    else:
        return None


def set_server_state(backend_name, server_name, state):
    hap = haproxy.HAProxy(socket_file=HAPROXY_SOCKET_FILE)
    servers = hap.server(server_name, backend=backend_name)
    if (len(servers) > 0):
        servers[0].setstate(state)


def enable_server(backend_name, server_name):
    set_server_state(backend_name, server_name, haproxy_server.STATE_ENABLE)
    return get_server(backend_name, server_name)


def disable_server(backend_name, server_name):
    set_server_state(backend_name, server_name, haproxy_server.STATE_DISABLE)
    return get_server(backend_name, server_name)
