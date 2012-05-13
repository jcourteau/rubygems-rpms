# Generated from dep_selector-0.0.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name dep_selector
%global rubyabi 1.9.1

Summary: Given packages, versions, and a dependency graph, find a valid assignment of package versions
Name: rubygem-%{gem_name}
Version: 0.0.8
Release: 1%{?dist}
Group: Development/Languages
License: Apache v2
# Originally at https://github.com/algorist/dep_selector
# Seems to have moved to the opscode repo now
# NOTE - some discrepancy in names - dep-selector vs dep_selector.
# Currently all the gem contents use the underscore version
URL: http://github.com/opscode/dep-selector
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests for this package are not in the gem. To update:
# git clone https://github.com/opscode/dep-selector.git && cd dep-selector
# git checkout rel-0.0.8
# tar czvf rubygem-dep_selector-0.0.8-specs.tgz spec/
Source1: rubygem-%{gem_name}-%{version}-specs.tgz

Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: gecode
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: gecode-devel
BuildRequires: rubygem(rspec)
Provides: rubygem(%{gem_name}) = %{version}

%description
Given packages, versions, and a dependency graph, find a valid assignment of
package versions


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
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force %{SOURCE0}

# Unpack the tests
tar zxvf %{SOURCE1}
cp -pr spec/ .%{gem_instdir}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir}/lib
mv %{buildroot}%{gem_instdir}/lib/dep_gecode.so %{buildroot}%{gem_extdir}/lib/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

%check
pushd .%{gem_instdir}
rspec -Ilib spec/*
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir}/lib/dep_gecode.so
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec

%changelog
* Sat May 12 2012  <rpms@courteau.org> - 0.0.8-1
- Initial package
