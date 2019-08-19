from .parser import parse_config_file, parse_groups_file
from flask import abort

class NodeGroups:
    def __init__(self, config_file_path):
        self.node = list()
        self.config_file_path = config_file_path
        self.node_groups = self.get_groups

    @property
    def get_groups(self):
        return parse_groups_file(self.config_file_path)

    @property
    def get_all_serialize_processes(self):
        nodes = parse_config_file(self.config_file_path)['nodes']
        nodes_processes = dict()
        serialize_processes = dict()
        for j in nodes:
            processes = j.serialize_processes()
            for k in processes:
                unique_key = k['nodeName'] + ':' + k['group'] + ':' + k['name']
                nodes_processes[unique_key] = k

        node_groups = self.get_groups
        for k, v in node_groups.items():
            groups_list = list()
            for j in v:
                unique_key = j['nodeName'] + ':' + j['group'] + ':' + j['name']
                if unique_key in nodes_processes:
                    groups_list.append(nodes_processes[unique_key])
                else:
                    abort(400, description="The Group Setting is error , please Check it.")

            serialize_processes[k] = groups_list

        return serialize_processes

    @property
    def get_all_serialize_general(self):
        serialize_general = dict()
        for k, v in self.node_groups.items():
            defaults = {'connected': True, 'environment': '', "meta": "group"}
            defaults['name'] = k
            serialize_general[k] = defaults

        return serialize_general

    def serialize_nodes(self):
        return [{"general": self.get_all_serialize_general[name],
                 "processes": self.get_all_serialize_processes[name]}
                for name in self.node_groups]

    @property
    def get_node_groups(self):
        serialize_nodes = self.serialize_nodes()
        return {i['general']['name']:i for i in serialize_nodes}

    def get_node_group(self,node_name):
        for n,v in self.get_node_groups.items():
            if n == node_name:
                return v

        return None
