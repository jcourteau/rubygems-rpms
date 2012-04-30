# Generated from net-ssh-gateway-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh-gateway

%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global rubyabi 1.8

Summary: A simple library to assist in establishing tunneled Net::SSH connections
Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 6%{?dist}
Group: Development/Languages
License: MIT
URL: http://net-ssh.rubyforge.org/gateway
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
Requires: rubygem(net-ssh) >= 1.99.1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby
BuildRequires: rubygem(net-ssh) >= 1.99.1
BuildRequires(check): rubygem(mocha)
BuildRequires(check): rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A simple library to assist in establishing tunneled Net::SSH connections


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm %{buildroot}%{gem_instdir}/setup.rb

%check
pushd .%{gem_instdir}
RUBYOPT="-Ilib -rrubygems" testrb test/*_test.rb
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/lib
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/net-ssh-gateway.gemspec
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/test


%changelog
* Sat Apr 14 2012 Jonas Courteau <rpms@courteau.org> - 1.1.0-6
- Ported to EPEL6

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.0-5
- Fix broken dependency.

* Tue Jan 31 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.0-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 06 2011 Vít Ondruch <vondruch@redhat.com> - 1.1.0-2
- Removed unnecessary setup.rb.

* Thu May 26 2011 Vít Ondruch <vondruch@redhat.com> - 1.1.0-1
- Initial package
