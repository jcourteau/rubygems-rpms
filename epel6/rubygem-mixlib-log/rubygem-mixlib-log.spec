# Generated from mixlib-log-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname mixlib-log
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

%global rubyabi 1.8

Summary: Ruby mixin for log functionality
Name: rubygem-%{gemname}
Version: 1.3.0
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-log
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
#Patch0: rubygem-mixlib-log-1.1.0-yaml.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires(check): rubygem(rake), rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A gem that provides a simple mixin for log functionality.

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

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/NOTICE
%dir %{geminstdir}
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/NOTICE
%{gemdir}/doc/%{gemname}-%{version}

%changelog
* Sun Apr 8 2012 Jonas Courteau <rpms@courteau.org> - 1.3.0-1
- New upstream version
- Removed check - no rspec tests in upstream gem anymore

* Wed Jun 9 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-3
- New patch to enable check again.

* Tue Jun 8 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-2
- Disable check for now.

* Tue Mar 23 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-1
- New upstream version - moves to jeweler for gem creation.

* Mon Oct 5 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-3
- Missing complete source url (#526181).
- Remove unused ruby_sitelib macro (#526181).
- Remove redundant doc Requires on rubygems (#526181).

* Sun Oct 4 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-2
- Remove redundant path in doc package (#526181).
- Use global over define (#526181).

* Mon Sep 28 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-1
- Initial package
