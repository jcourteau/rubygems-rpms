# Generated from moneta-0.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name moneta
%global rubyabi 1.9.1

Summary: A unified interface to key/value stores
Name: rubygem-%{gem_name}
Version: 0.6.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/wycats/moneta
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby 
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A unified interface to key/value stores

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

# Unneeded file
rm .%{gem_instdir}/TODO

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/LICENSE
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile

%changelog
* Tue May 01 2012  <rpms@courteau.org> - 0.6.0-1
- Initial package
- not including tests at this time (not in the gem, and they have complicated requirements)
