Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "psidialogs_ubuntu2004"
    #   vb.gui = true
    vb.memory = "2048" # ste high because of Xephyr memory leak
  end

  config.vm.provision "shell", path: "tests/vagrant/ubuntu2004.sh"

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=tests/vagrant/Vagrantfile.ubuntu2004.rb;export VAGRANT_DOTFILE_PATH=tests/vagrant/.vagrant_Vagrantfile.ubuntu2004.rb
# vagrant up && vagrant ssh
