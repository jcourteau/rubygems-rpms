# Generated from mixlib-authentication-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname mixlib-authentication
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

%global rubyabi 1.8

Summary: Simple per-request authentication
Name: rubygem-%{gemname}
Version: 1.1.4
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-authentication
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
Patch0: rubygem-mixlib-authentication-1.1.4-spec.patch
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(mixlib-log)
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires(check): rubygem(rake), rubygem(rspec), rubygem(mixlib-log)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Mixlib::Authentication provides a class-based header signing authentication
object.

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

%clean
rm -rf %{buildroot}

%check
pushd .%{geminstdir}
rake spec

%files
%defattr(-,root,root,-)
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/NOTICE
%dir %{geminstdir}
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%{geminstdir}/Rakefile
%{geminstdir}/spec
%{gemdir}/doc/%{gemname}-%{version}

%changelog
* Sun Apr 8 2012 Jonas Courteau <rpms@courteau.org> - 1.1.4-1
- New upstream version
- Patch to fix broken spec (fixed in upstream commit fe5cd0116)

* Mon Mar 19 2010 Matthew Kent <matt@bravenet.com> - 1.1.2-2
- Let check phase fail.
- Fix duplicate inclusion of Rakefile.

* Wed Mar 17 2010 Matthew Kent <matt@bravenet.com> - 1.1.2-1
- Initial package
