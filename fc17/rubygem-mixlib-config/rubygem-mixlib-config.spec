# Generated from mixlib-config-1.0.9.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-config

%global rubyabi 1.9.1

Summary: Simple ruby config mix-in
Name: rubygem-%{gem_name}
Version: 1.1.2
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-config
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
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
A class based config mix-in, similar to the one found in Chef.

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

# Shouldn't be in the gem
rm %{buildroot}%{gem_instdir}/.gitignore

%check
pushd .%{gem_instdir}
rspec -Ilib spec/mixlib/config_spec.rb
popd

%files
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NOTICE
%doc %{gem_instdir}/README.rdoc
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/VERSION.yml
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%{gem_instdir}/features
%doc %{gem_docdir}

%changelog
* Mon Apr 30 2012 Jonas Courteau <rpm@courteau.org> - 1.1.2-1
- Repackaged for fc17
- Call tests directly, eliminating need for patch, Rakefile modification
- New upstream version

* Wed Jun 9 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-4
- New patch to enable check again.

* Tue Jun 8 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-3
- Disable check for now.

* Tue Mar 23 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-2
- New upstream version - moves to jeweler for gem creation.

* Mon Oct 5 2009 Matthew Kent <mkent@magoazul.com> - 1.0.12-2
- Missing complete source url (#526180).
- Remove unused ruby_sitelib macro (#526180).
- Remove redundant doc Requires on rubygems (#526180).

* Sun Oct 4 2009 Matthew Kent <mkent@magoazul.com> - 1.0.12-1
- Remove redundant path in doc package (#526180).
- Use global over define (#526180).
- New upstream version (#526180).

* Mon Sep 28 2009 Matthew Kent <mkent@magoazul.com> - 1.0.9-1
- Initial package
