# Generated from yajl-ruby-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name yajl-ruby

%global rubyabi 1.9.1

Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library
Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/brianmario/yajl-ruby
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
BuildRequires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
Provides: rubygem(%{gem_name}) = %{version}

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
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local \
  --install-dir $(pwd)%{gem_dir} \
  -V \
  --force --rdoc \
   %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext
# Remove other cruft from the gem
rm %{buildroot}%{gem_instdir}/.gitignore \
   %{buildroot}%{gem_instdir}/.travis.yml \
   %{buildroot}%{gem_instdir}/Gemfile \
   %{buildroot}%{gem_instdir}/%{gem_name}.gemspec
# Move C extension to extdir:
mkdir -p %{buildroot}%{gem_extdir}/lib/yajl
mv %{buildroot}%{gem_instdir}/lib/yajl/yajl.so %{buildroot}%{gem_extdir}/lib/yajl/

# Fix permissions
# https://github.com/brianmario/yajl-ruby/issues/103
chmod -x %{buildroot}%{gem_instdir}/benchmark/subjects/unicode.json

%check
pushd .%{gem_instdir}
rspec -Ilib spec/
popd


%files
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%dir %{gem_instdir}
%{gem_extdir}/lib/yajl/yajl.so
%{gem_libdir}
%{gem_instdir}/benchmark
%{gem_instdir}/tasks
%{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec
# https://github.com/brianmario/yajl-ruby/issues/103
%exclude %{gem_instdir}/.rspec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/examples

%changelog
* Mon Apr 30 2012  <rpms@courteau.org> - 1.1.0-1
- Initial package
