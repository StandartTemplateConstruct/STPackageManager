#!/usr/bin/env python
import argparse
import re

import yaml

class PackageRegistry:
    def __init__(self):
        self._packages = {}

    def add_package(self, package):
        self._packages[package.name] = package

    def get_package(self, package_name):
        return self._packages[package_name]

    def all(self):
        for name, package in self._packages.items():
            yield package

PACKAGE_REGISTRY = PackageRegistry()

class PackageDependency:
    def __init__(self, yaml, params):
        if isinstance(yaml, str):
            self.name = yaml
        else:
            self.name = yaml['n']
            self.params = params


class Package:
    def __init__(self, yaml):
        self.name = yaml['n']
        self.params = yaml.get('params')
        if yaml.get('depends'):
            self.depends = [PackageDependency(dep, self.params) for dep in yaml['depends']]
    def __str__(self):
        return "{}".format(self.name)


class Object:
    def __init__(self, yaml):
        self.name = yaml['name']
        self.package = PACKAGE_REGISTRY.get_package(yaml['type'])
        if yaml.get('content'):
            self.content = [Object(obj) for obj in yaml['content']]
        else:
            self.content = []

    def default_object_name(self):
        return "{}1".format(self.package.name.split(".")[-1].capitalize())

    def __str__(self):
        def prepend_space_at_each_line(s):
            return "\n".join([" {}".format(s) for s in s.split("\n")])

        result = "{}           type: {}\n".format(self.name, self.package.name)
        if len(self.content):
            children_strs = [prepend_space_at_each_line(o.__str__()) for o in self.content]
            result += "\n".join(children_strs)

        #there is a bug in line joins, just clearing up output with a REGEX. try disabling this like see whats happens!
        result = re.sub("\n( )*\n", "\n", result)

        #fixme make output pretty
        return result


def init_argparse():
    parser = argparse.ArgumentParser(prog='stc')
    subparsers = parser.add_subparsers()
    parser_install = subparsers.add_parser('install')
    parser_install.add_argument('package', metavar='PACKAGE', type=str, nargs='+')
    parser_available = subparsers.add_parser('list-available')
    parser_installed = subparsers.add_parser('list-installed')
    return parser


ARG_PARSER = init_argparse()


def load_installed_packages_yamls():

    with open("avaliable-packages.yaml", "r") as stream:
        try:
            for p in yaml.safe_load(stream)['packages']:
                package = Package(p)
                PACKAGE_REGISTRY.add_package(package)

        except yaml.YAMLError as exc:
            print(exc)
    with open("installed-packages.yaml", "r") as stream:
        try:
            world = Object(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)

    return world


world = load_installed_packages_yamls()

if __name__ == "__main__":
    init_argparse()

    """
    command options parsing test
    """
    ARG_PARSER.parse_args(['list-available'])
    ARG_PARSER.parse_args(['list-installed'])
    ARG_PARSER.parse_args(['install', 'woodwork.hammer'])
    ARG_PARSER.parse_args(['list-installed'])
    ARG_PARSER.parse_args(['install', 'woodwork.hammer'])

    #fixme bring all readme

    args, unknownargs = ARG_PARSER.parse_known_args(['install', 'electronics.display.crt', "--diagonal", "32.5"])

    for package in PACKAGE_REGISTRY.all():
        print(package)
    print(world)
