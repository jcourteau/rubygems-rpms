# Generated from mixlib-cli-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname mixlib-cli
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

%global rubyabi 1.8

Summary: Simple ruby mixin for CLI interfaces
Name: rubygem-%{gemname}
Version: 1.2.0
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-cli
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
Patch0: rubygem-mixlib-cli-1.1.0-yaml.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires(check): rubygem(rake), rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A simple mixin for CLI interfaces, including option parsing.

%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

mkdir -p .%{gemdir}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gemdir} \
  --force --rdoc \
  %{SOURCE0}

pushd .%{geminstdir}
%patch0 -p1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/

# Shouldn't be in the gem
rm %{buildroot}%{geminstdir}/.gitignore

%clean
rm -rf %{buildroot}

%check
pushd .%{geminstdir}
rake spec

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/NOTICE
%doc %{geminstdir}/README.rdoc
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/VERSION.yml
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%{geminstdir}/spec
%{geminstdir}/features
%{gemdir}/doc/%{gemname}-%{version}

%changelog
* Fri Apr 6 2012 Jonas Courteau <rpm@courteau.org> - 1.2.0-1
- New upstream version

* Wed Jun 9 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-3
- New patch to enable check again.

* Tue Jun 8 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-2
- Disable check for now.

* Tue Mar 23 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-1
- New upstream version - moves to jeweler for gem creation.

* Mon Oct 5 2009 Matthew Kent <mkent@magoazul.com> - 1.0.4-3
- Remove unused ruby_sitelib macro (#526179).
- Remove redundant doc Requires on rubygems (#526179).

* Sun Oct 4 2009 Matthew Kent <mkent@magoazul.com> - 1.0.4-2
- Remove redundant path in doc package (#526179).
- Use global over define (#526179).

* Mon Sep 28 2009 Matthew Kent <mkent@magoazul.com> - 1.0.4-1
- Initial package
