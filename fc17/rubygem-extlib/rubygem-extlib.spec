# Generated from extlib-0.9.15.gem by gem2rpm -*- rpm-spec -*-
%global gem_name extlib
%global rubyabi 1.9.1

Summary: Support library for DataMapper and Merb
Name: rubygem-%{gem_name}
Version: 0.9.15
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/datamapper/extlib
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are built around older version of rspec, but run with patched file:
Patch0: rubygem-extlib-0.9.17-fix_rspec.patch
Requires: ruby 
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: rubygem(bigdecimal)
BuildRequires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(bigdecimal)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Support library for DataMapper and Merb


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
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p2
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -Ilib spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%{gem_instdir}/Rakefile
%{gem_instdir}/tasks
%{gem_instdir}/VERSION
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.autotest

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/spec
%{gem_instdir}/extlib.gemspec

%changelog
* Mon Apr 30 2012  <rpms@courteau.org> - 0.9.15-1
- Initial package
- Patch tests to work with rspec 2
