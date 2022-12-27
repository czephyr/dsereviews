#!/bin/bash

ansible-playbook -i inventories/preprod/hosts.ini playbook.yml --vault-password-file .vault.pwd "$@"