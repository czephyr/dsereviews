# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.require_version ">= 2.0"

Vagrant.configure("2") do |config|

  config.vm.define "server" do |bs|
    bs.vm.hostname = "server"
    bs.vm.box = "debian/bullseye64"
    bs.vm.network "private_network", ip: "192.168.56.66"
    bs.vm.provider "virtualbox" do |vb|
      vb.name = "dev_vm_garr"
      vb.memory = "2048"
    end
    bs.vm.synced_folder ".", "/vagrant", type: "rsync",
      rsync__exclude: ".git/"
  end
  
  # Ensure that all Vagrant machines will use the same SSH key pair.
  config.ssh.insert_key = false

  # Enable provisioning with ansible
  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    #ansible.install_mode = "pip3"
    #ansible.version = "latest"
    ansible.playbook = "ansible/playbook.yml"
   # ansible.verbose = "vvv"
    ansible.groups = {
      "dev" => ["server"]
    }
    ansible.vault_password_file = "ansible/.vault.pwd"
    #ansible.tags = "docker"
    #ansible.tags = "nfs,kube"
  end

end