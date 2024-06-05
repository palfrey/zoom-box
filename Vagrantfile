Vagrant.configure(2) do |config|
  config.vm.box = "bento/debian-12"
  config.vm.box_check_update = false

  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end

  config.vm.provider :virtualbox do |p|
    p.customize ["modifyvm", :id, "--cableconnected1", "on"]
    p.customize ["modifyvm", :id, "--memory", 2048]
    p.customize ["modifyvm", :id, "--cpus", 2]
  end
end
