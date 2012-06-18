# Generated from mixlib-log-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-log

%global rubyabi 1.9.1

Summary: Ruby mix-in for log functionality
Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-log
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# See http://tickets.opscode.com/browse/CHEF-3169
# Download tests seperately:
# git clone http://github.com/opscode/mixlib-log.git && cd mixlib-log
# git checkout 1.3.0
# tar -czf rubygem-mixlib-log-1.3.0-specs.tgz spec/
Source1: %{name}-%{version}-specs.tgz

Requires: ruby
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: ruby(abi) = %{rubyabi}
# Needed for check:
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A gem that provides a simple mix-in for log functionality.

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

%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}
rspec -Ilib spec/mixlib/log_spec.rb
popd

%files
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/NOTICE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}

%changelog
* Sun Apr 29 2012 Jonas Courteau <rpms@courteau.org> - 1.3.0-1
- Repackaged for fc17
- New upstream version
- Removed check patch
- Modified check - pull tests manually as they've been removed from gem

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
