import logging
from config import Config
from utils import SshUtil

log = logging.getLogger(__name__)

class VMwareOps(Config):

    def __init__(self):
        log.debug("Initialized VMwareOps")
        Config.__init__(self)

    def clients(self):
        for node, creds in self.esxi_hosts.items():
            yield SshUtil(node,
                          creds[0],
                          creds[1])

    def health_ok(self):
        """ Not sure if that makes sense
        """
        for client in self.clients():
            if client.run_cmd('ls'):
                log.info('Vmware cluster is up.')
                return True
            else:
                return False
