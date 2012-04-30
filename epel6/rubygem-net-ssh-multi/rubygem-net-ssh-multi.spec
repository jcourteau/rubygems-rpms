# Generated from net-ssh-multi-1.1.gem by gem2rpm -*- rpm-spec -*-
%global gemname net-ssh-multi

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Control multiple Net::SSH connections via a single interface
Name: rubygem-%{gemname}
Version: 1.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/net-ssh/net-ssh
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: rubygem(net-ssh) >= 2.1.4
Requires: rubygem(net-ssh-gateway) >= 0.99.0
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires(check): rubygem(minitest)
BuildRequires(check): rubygem(mocha)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Control multiple Net::SSH connections via a single interface.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local \
  --install-dir $(pwd)%{gemdir} \
  --force --rdoc \
   %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%clean
rm -rf %{buildroot}

%check
pushd %{buildroot}%{geminstdir}
ruby -Ilib -Itest -rrubygems test/test_all.rb
popd

%files
%defattr(-,root,root,-)
%doc %{geminstdir}/README.rdoc
%dir %{geminstdir}
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/CHANGELOG.rdoc
%{geminstdir}/Rakefile
%{geminstdir}/test


%changelog
* Sat Apr 14 2012 Jonas Courteau <rpms@courteau.org> - 1.1-1
- Initial package
