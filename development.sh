#!/bin/bash

VM_STATUS=$(vagrant status --machine-readable | grep ",state," | egrep -o '([a-z_]*)$')
case "${VM_STATUS}" in
  running)
     vagrant rsync
     vagrant provision
  ;;
  *)
     vagrant up
  ;;
esac

