from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim
from config import Config

class Connect(Config):

    def __init__(self):
        Config.__init__(self)

        try:
            self.si = SmartConnectNoSSL(host=self.vcenter_host,
                                       user=self.vcenter_user,
                                       pwd=self.vcenter_password)
        except vim.fault.InvalidLogin:
            raise SystemExit("Unable to connect to host with supplied credentials.")
