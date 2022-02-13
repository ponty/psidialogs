Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"
  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |vb|
    #  vb.gui = true
    vb.memory = "2048"
    vb.name = "psidialogs_debian10"
  end

  config.vm.provision "shell", path: "tests/vagrant/debian10.sh", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=tests/vagrant/Vagrantfile.debian10.rb;export VAGRANT_DOTFILE_PATH=tests/vagrant/.vagrant_Vagrantfile.debian10.rb
# vagrant up && vagrant ssh
