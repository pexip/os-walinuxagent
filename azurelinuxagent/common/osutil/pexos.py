from azurelinuxagent.common.exception import OSUtilError
from azurelinuxagent.common.osutil.default import DefaultOSUtil

class PexOSUtil(object):
    def __init__(self):
        self._default = DefaultOSUtil()
        self.jit_enabled = False # ga/remoteaccess.py
        self.service_name = self.get_service_name()

    @staticmethod
    def get_service_name():
        return "walinuxagent"

    def get_agent_conf_file_path(self):
        # agent.py
        return self._default.get_agent_conf_file_path()

    def start_agent_service(self):
        # agent.py
        pass

    def stop_agent_service(self):
        # agent.py
        pass

    def register_agent_service(self):
        # agent.py
        pass


    @staticmethod
    def is_cgroups_supported():
        # common/cgroups.py
        return False

    def get_total_cpu_ticks_since_boot(self):
        # common/cgroup.py
        return self._default.get_total_cpu_ticks_since_boot()


    def is_dhcp_available(self):
        # common/dhcp.py common/protocol/util.py
        return False


    def check_pid_alive(self, pid):
        # daemon/main.py ga/env.py ga/update.py
        return self._default.check_pid_alive(pid)


    def get_instance_id(self):
        # pa/provision/default.py
        return ''


    def get_dhcp_pid(self):
        # ga/env.py
        return []

    def get_hostname_record(self):
        # ga/env.py
        return None

    def remove_rules_files(self):
        # ga/env.py
        pass


    def get_firewall_dropped_packets(self, dst_ip=None):
        # ga/monitor.py
        return 0

    @staticmethod
    def read_route_table():
        # ga/monitor.py
        return []

    @staticmethod
    def get_list_of_routes(route_table):
        # ga/monitor.py
        return []

    def get_nic_state(self):
        # ga/monitor.py
        return {}

    def get_total_mem(self):
        # ga/monitor.py
        return self._default.get_total_mem()

    def get_processor_cores(self):
        # ga/monitor.py cgroups.py
        return self._default.get_processor_cores()


    # For tests only: runtime configuration ensures these aren't used
    def device_for_ide_port(self, port_id):
        return None

    def try_load_atapiix_mod(self):
        return

    def mount_dvd(self, **kwargs):
        return self._default.mount_dvd(**kwargs)

    def umount_dvd(self, **kwargs):
        return self._default.umount_dvd(**kwargs)

    def set_hostname(self, hostname):
        return

    def set_dhcp_hostname(self, hostname):
        return

    def del_root_password(self):
        return
