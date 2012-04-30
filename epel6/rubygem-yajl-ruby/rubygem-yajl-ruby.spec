# Generated from yajl-ruby-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname yajl-ruby

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library
Name: rubygem-%{gemname}
Version: 1.1.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/brianmario/yajl-ruby
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
# Patches go here
# Patch0: such_and_such.patch
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby-devel
Provides: rubygem(%{gemname}) = %{version}

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local \
  --install-dir $(pwd)%{gemdir} \
  -V \
  --force --rdoc \
   %{SOURCE0}

# Patches go here:
# pushd .%{geminstdir}
# %patch0 -p1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/
# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext
# Remove other cruft from the gem
rm %{buildroot}%{geminstdir}/.gitignore \
   %{buildroot}%{geminstdir}/.travis.yml \
   %{buildroot}%{geminstdir}/Gemfile \
   %{buildroot}%{geminstdir}/%{gemname}.gemspec

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{geminstdir}/MIT-LICENSE
%doc %{geminstdir}/CHANGELOG.md
%doc %{geminstdir}/README.md
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/benchmark
%{geminstdir}/tasks
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{gemdir}/doc/%{gemname}-%{version}
%{geminstdir}/Rakefile
%{geminstdir}/spec
%{geminstdir}/examples
%{geminstdir}/.rspec

%changelog
* Sat Apr 14 2012  <rpms@courteau.org> - 1.1.0-1
- Initial package
- disabling check due to dependencies on rspec 2.x
