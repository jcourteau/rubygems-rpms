# Generated from chef-0.10.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name chef

%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global rubyabi 1.8

Summary: A systems integration framework, built to bring the benefits of configuration management to your entire infrastructure
Name: rubygem-%{gem_name}
Version: 0.10.8
Release: 1%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: http://wiki.opscode.com/display/chef
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: chef-client_config.rb
# changed ssh requirement pending chef 0.10.10
Patch0: chef-0.10.8-change_net-ssh_requirement.patch

Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: rubygem(mixlib-config) >= 1.1.2
Requires: rubygem(mixlib-cli) >= 1.1.0
Requires: rubygem(mixlib-log) >= 1.3.0
Requires: rubygem(mixlib-authentication) >= 1.1.0
Requires: rubygem(ohai) >= 0.6.0
Requires: rubygem(rest-client) >= 1.0.4
Requires: rubygem(rest-client) < 1.7.0
Requires: rubygem(bunny) >= 0.6.0
Requires: rubygem(json) >= 1.4.4
Requires: rubygem(json) <= 1.6.1
Requires: rubygem(treetop) => 1.4.9
Requires: rubygem(treetop) < 1.5
Requires: rubygem(net-ssh) => 2.1.3
Requires: rubygem(net-ssh-multi) => 1.1
Requires: rubygem(net-ssh-multi) < 1.2
Requires: rubygem(erubis) 
Requires: rubygem(moneta) 
Requires: rubygem(highline) 
Requires: rubygem(uuidtools) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
# may need rdoc sdoc ronn rake rack rspec_junit_formatter rspec2 for tests
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

# change the net-ssh requirement
pushd .%{gem_dir}
%patch0 -p6
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

install -D -p -m 755 %{buildroot}%{gem_instdir}/distro/redhat/etc/init.d/chef-client \
	%{buildroot}%{_sysconfdir}/rc.d/init.d/chef-client
install -D -p -m 644 %{buildroot}%{gem_instdir}/distro/redhat/etc/logrotate.d/chef-client \
	%{buildroot}%{_sysconfdir}/logrotate.d/chef-client
install -D -p -m 644 %{buildroot}%{gem_instdir}/distro/redhat/etc/sysconfig/chef-client \
	%{buildroot}%{_sysconfdir}/sysconfig/chef-client
install -D -p -m 644 %{SOURCE1} \
	%{buildroot}%{_sysconfdir}/chef/client.rb

rm -rf %{buildroot}%{gem_instdir}/distro/{redhat,arch,debian}

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{gem_instdir}/distro/common/man/{man1,man8} \
	%{buildroot}%{_mandir}
rmdir %{buildroot}%{gem_instdir}/distro/common/man

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/chef-client
%{_bindir}/chef-solo
%{_bindir}/knife
%{_bindir}/shef

%{_sysconfdir}/rc.d/init.d/chef-client
%config(noreplace) %{_sysconfdir}/logrotate.d/chef-client
%config(noreplace) %{_sysconfdir}/sysconfig/chef-client
%dir %{_sysconfdir}/chef
%config(noreplace) %{_sysconfdir}/chef/client.rb

%{gem_instdir}/bin
%{gem_instdir}/lib
%{_mandir}/man1/knife*
%{_mandir}/man1/shef*
%{_mandir}/man8/chef*
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/distro/common
%doc %{gem_instdir}/distro/README
%changelog
* Sun Apr 22 2012 Jonas Courteau <rpms@courteau.org> - 0.10.8-1
- Initial package
