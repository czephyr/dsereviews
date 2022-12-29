#!/bin/bash

ansible-playbook -i inventories/prod/hosts.ini playbook.yml --vault-password-file .vault.pwd "$@" --tags remote