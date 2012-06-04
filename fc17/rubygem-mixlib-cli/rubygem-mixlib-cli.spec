# Generated from mixlib-cli-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-cli

%global rubyabi 1.9.1

Summary: Simple ruby mix-in for CLI interfaces
Name: rubygem-%{gem_name}
Version: 1.2.2
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-cli
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
Requires: ruby
Requires: ruby(abi) = %{rubyabi}
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: ruby(abi) = %{rubyabi}
# Needed to run checks:
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A simple mix-in for CLI interfaces, including option parsing.

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
rspec -Ilib spec/mixlib/cli_spec.rb
popd

%files
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NOTICE
%doc %{gem_instdir}/README.rdoc
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}

%changelog
* Mon Apr 30 2012 Jonas Courteau <rpm@courteau.org> - 1.2.2-1
- Repackaged for fc17
- Changed check to avoid need for patch
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
