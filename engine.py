#!/usr/bin/env python3

import argparse
import yaml
import os
from pprint import pprint
from time import sleep
from protocols import http, ssh

DEBUG = False # os.getenv("DEBUG")

def main():
    parser = argparse.ArgumentParser(
        description="Spawn the scoring engine"
    )
    parser.add_argument(
        "--infra-file", 
        type=argparse.FileType('r'),
        help="The yaml file containing the infrastructure config",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=30,
        help="The interval at which the engine repeats in seconds",
    )
    args = parser.parse_args()
    config = yaml.load(args.infra_file.read(), Loader=yaml.FullLoader)
    if DEBUG:
        print("The config ⤵")
        for machine, conf in config.items():
            print(machine)
            pprint(conf)
        print("The interval ⤵")
        pprint(args.interval)
    for i in range(10):        # Change to while for prod
        for machine, conf in config.items():
            for service, properties in conf["services"].items():
                if service == "http":
                    status_code = http.http_status(
                        conf["address"],
                        properties["status_codes"]
                    ) 
                    print(f"{machine}-http, {'up' if status_code else 'down'}")
                elif service == "ssh":
                    ssh_auth = ssh.ssh_user_password_check(
                        conf["address"],
                        (22 if 'port' not in properties else properties["port"]),
                        properties["username"],
                        properties["password"]
                    )
                    print(f"{machine}-ssh, {'up' if ssh_auth else 'down'}")
        sleep(args.interval)
if __name__ == "__main__":
    main()
