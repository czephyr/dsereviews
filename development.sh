#!/bin/bash

ansible-playbook -i inventories/dev/hosts.ini playbook.yml --vault-password-file .vault.pwd "$@" --tags local -vvvv