# Generated from mixlib-authentication-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-authentication

%global rubyabi 1.9.1

Summary: Simple per-request authentication
Name: rubygem-%{gem_name}
Version: 1.1.4
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-authentication
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-mixlib-authentication-1.1.4-spec.patch
Requires: ruby
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(mixlib-log)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: ruby(abi) = %{rubyabi}
# Needed to run checks:
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(mixlib-log)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

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

mkdir -p .%{gem_dir}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -Ilib spec/mixlib/authentication/
popd

%files
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NOTICE
%dir %{gem_instdir}
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%{gem_instdir}/Rakefile
%doc %{gem_docdir}

%changelog
* Sun Apr 29 2012 Jonas Courteau <rpms@courteau.org> - 1.1.4-1
- Repackaged for fc17
- New upstream version
- Patch to fix broken spec (fixed in upstream commit fe5cd0116)

* Mon Mar 19 2010 Matthew Kent <matt@bravenet.com> - 1.1.2-2
- Let check phase fail.
- Fix duplicate inclusion of Rakefile.

* Wed Mar 17 2010 Matthew Kent <matt@bravenet.com> - 1.1.2-1
- Initial package
