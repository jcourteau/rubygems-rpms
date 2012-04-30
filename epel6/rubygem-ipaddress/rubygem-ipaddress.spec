# Generated from ipaddress-0.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ipaddress

%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global rubyabi 1.8

Summary: IPv4/IPv6 addresses manipulation library
Name: rubygem-%{gem_name}
Version: 0.8.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/bluemonk/ipaddress
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires(check): rubygem(rake)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
IPAddress is a Ruby library designed to make manipulation
of IPv4 and IPv6 addresses both powerful and simple. It mantains
a layer of compatibility with Ruby's own IPAddr, while 
addressing many of its issues.


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
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%clean
rm -rf %{buildroot}

%check
pushd .%{gem_instdir}
rake test


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/.document

%changelog
* Sun Apr 29 2012 Jonas Courteau <rpms@courteau.org> - 0.8.0-1
- Initial package
