# Generated from chef-0.10.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name chef
%global rubyabi 1.9.1

Summary: A client for the Chef systems integration framework
Name: rubygem-%{gem_name}
Version: 0.10.10
Release: 2%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://wiki.opscode.com/display/chef
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: chef-client_config.rb
# Tests for this package are not in the gem. To update:
# git clone https://github.com/opscode/chef.git && cd chef/chef
# git checkout 0.10.10
# tar czvf rubygem-chef-0.10.10.tgz spec/
Source2: rubygem-%{gem_name}-%{version}-specs.tgz
Patch0: rubygem-chef-0.10.10-change_json_requirement.patch

Requires: ruby
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: rubygem(mixlib-config) >= 1.1.2
Requires: rubygem(mixlib-cli) >= 1.1.0
Requires: rubygem(mixlib-log) >= 1.3.0
Requires: rubygem(mixlib-authentication) >= 1.1.0
Requires: rubygem(mixlib-shellout) => 1.0.0
Requires: rubygem(mixlib-shellout) < 1.1.0
Requires: rubygem(ohai) >= 0.6.0
Requires: rubygem(rest-client) >= 1.0.4
Requires: rubygem(rest-client) < 1.7.0
Requires: rubygem(bunny) >= 0.6.0
Requires: rubygem(json) >= 1.4.4
Requires: rubygem(json) <= 1.6.5
Requires: rubygem(yajl-ruby) >= 1.1.0
Requires: rubygem(treetop) => 1.4.9
Requires: rubygem(treetop) < 1.5
Requires: rubygem(net-ssh) => 2.2.2
Requires: rubygem(net-ssh) < 2.3
Requires: rubygem(net-ssh-multi) => 1.1
Requires: rubygem(net-ssh-multi) < 1.2
Requires: rubygem(erubis) 
Requires: rubygem(moneta) 
Requires: rubygem(highline) >= 1.6.9
Requires: rubygem(uuidtools) 

BuildRequires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(uuidtools)
BuildRequires: rubygem(erubis)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(thin)
BuildRequires: rubygem(rest-client)
BuildRequires: rubygem(treetop)
BuildRequires: rubygem(mixlib-shellout) => 1.0.0
BuildRequires: rubygem(mixlib-shellout) < 1.1.0
BuildRequires: rubygem(mixlib-log) >= 1.3.0
BuildRequires: rubygem(mixlib-config) >= 1.1.2
BuildRequires: rubygem(mixlib-authentication) >= 1.1.0
BuildRequires: rubygem(mixlib-cli) >= 1.1.0
BuildRequires: rubygem(yajl-ruby) >= 1.1.0
BuildRequires: rubygem(highline)
BuildRequires: rubygem(ohai) >= 0.6.0
BuildRequires: rubygem(bunny) >= 0.6.0
BuildRequires: rubygem(moneta)
BuildRequires: rubygem(json) >= 1.4.4
BuildRequires: rubygem(json) <= 1.6.5
BuildRequires: rubygem(net-ssh) => 2.2.2
BuildRequires: rubygem(net-ssh) < 2.3
BuildRequires: rubygem(net-ssh-multi) => 1.1
BuildRequires: rubygem(net-ssh-multi) < 1.2
# These tests are disabled currently
#BuildRequires: rubygem(dep_selector)

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A client for the Chef systems integration framework

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
# Adjust the JSON gem requirement:
%patch0 -p2

%build
mkdir -p .%{gem_dir}
gem build %{gem_name}.gemspec

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install -V \
            --local \
            --install-dir ./%{gem_dir} \
            --bindir ./%{_bindir} \
            --force \
            --rdoc \
            %{SOURCE0}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

# Move the /etc/ elements into place
install -D -p -m 755 %{buildroot}%{gem_instdir}/distro/redhat/etc/init.d/chef-client \
        %{buildroot}%{_sysconfdir}/rc.d/init.d/chef-client
install -D -p -m 644 %{buildroot}%{gem_instdir}/distro/redhat/etc/logrotate.d/chef-client \
        %{buildroot}%{_sysconfdir}/logrotate.d/chef-client
install -D -p -m 644 %{buildroot}%{gem_instdir}/distro/redhat/etc/sysconfig/chef-client \
        %{buildroot}%{_sysconfdir}/sysconfig/chef-client
install -D -p -m 644 %{SOURCE1} \
        %{buildroot}%{_sysconfdir}/chef/client.rb

# Remove un-needed distro files
rm -rf %{buildroot}%{gem_instdir}/distro/{redhat,arch,debian,windows}

# Move man fles
mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{gem_instdir}/distro/common/man/{man1,man8} \
        %{buildroot}%{_mandir}
rmdir %{buildroot}%{gem_instdir}/distro/common/man
# Remove markdown files; only needed to generate man pages and HTML docs
rm -rf %{buildroot}%{gem_instdir}/distro/common/markdown

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd %{buildroot}%{gem_instdir}
tar zxvf %{SOURCE2}
rspec -Ilib
rm -rf spec
popd

%post
/sbin/chkconfig --add chef-client || :

%preun
if [ $1 -eq 0 ] ; then
  /sbin/service chef-client stop &>/dev/null || :
  /sbin/chkconfig --del chef-client || :
fi

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
* Sun May 27 2012 Jonas Courteau <rpms@courteau.org> - 0.10.10-2
- Fixed license short name
- Updated summary
- Don't package markdown docs
- Don't package tests
- Added chkconfig to post/preun sections
- Converted to fc17 Rubygem build format

* Sat May 12 2012 Jonas Courteau <rpms@courteau.org> - 0.10.10-1
- Updated to 0.10.10

* Sun Apr 22 2012 Jonas Courteau <rpms@courteau.org> - 0.10.8-1
- Initial package
