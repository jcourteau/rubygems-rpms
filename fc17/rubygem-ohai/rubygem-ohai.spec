# Generated from ohai-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ohai

%global rubyabi 1.9.1

Summary: Profiles your system and emits JSON
Name: rubygem-%{gem_name}
Version: 0.6.12
Release: 2%{?dist}
Group: Development/Languages
License: ASL 2.0 
URL: http://wiki.opscode.com/display/chef/Ohai
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(json)
Requires: rubygem(extlib)
Requires: rubygem(systemu)
Requires: rubygem(mixlib-cli)
Requires: rubygem(mixlib-config)
Requires: rubygem(mixlib-log)
Requires: rubygem(yajl-ruby)
Requires: rubygem(ipaddress)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: ruby(abi) = %{rubyabi}
# For checks:
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(json)
BuildRequires: rubygem(extlib)
BuildRequires: rubygem(yajl-ruby)
BuildRequires: rubygem(ipaddress)
BuildRequires: rubygem(systemu)
BuildRequires: rubygem(mixlib-cli)
BuildRequires: rubygem(mixlib-config)
BuildRequires: rubygem(mixlib-log)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ohai detects data about your operating system and prints out a JSON data blob.
It can be used standalone, but it's primary purpose is to provide node data to
Chef.

%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

mkdir -p .%{gem_dir}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/docs/man/man1/%{gem_name}.1 %{buildroot}%{_mandir}/man1/ohai.1
rm -rf {%{buildroot}%{gem_dir}/docs

find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'

%check
pushd .%{gem_instdir}
# Workaround for test that expects a UTF-8 encoding.
# Upstream ticket: http://tickets.opscode.com/browse/OHAI-379
ruby -EUTF-8 %{_bindir}/rspec -Ilib spec/
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%{_bindir}/ohai
%{gem_libdir}
%{gem_instdir}/bin
%{gem_cache}
%{gem_spec}
%{_mandir}/man1/%{gem_name}.1.gz
%exclude %{gem_instdir}/spec

%files doc
%{gem_instdir}/Rakefile
%doc %{gem_docdir}

%changelog
* Sun Jun 3 2012 Jonas Courteau <rpms@courteau.org> - 0.6.12-2
- Re-enabled all tests
- Added explicit external encoding for tests, pending http://tickets.opscode.com/browse/OHAI-379
- Exclude tests from rpm
- Updated URL and source0

* Sun Apr 8 2012 Jonas Courteau <rpms@courteau.org> - 0.6.12-1
- Disable spec testing OHAI-275; fails due to character set under mock
- Re-enabled all other tests
- New upstream version

* Fri Mar 19 2010 Matthew Kent <mkent@magoazul.com> - 0.5.0-1
- Initial package
