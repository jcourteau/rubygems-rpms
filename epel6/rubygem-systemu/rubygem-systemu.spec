# Generated from systemu-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname systemu
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

%global rubyabi 1.8

Summary: Multi-platform command execution and capture
Name: rubygem-%{gemname}
Version: 2.5.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2 or Ruby
URL: https://github.com/ahoward/systemu
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires(check): rubygem(rake)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
systemu can be used on any platform to return status, stdout, and stderr of any
command.

%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%package -n ruby-%{gemname}
Summary: Non-Gem support package for %{gemname}
Group: Development/Languages

Requires: %{name} = %{version}-%{release}
Provides: ruby(%{gemname}) = %{version}-%{release}

%description -n ruby-%{gemname}
This package provides non-Gem support for %{gemname}.

%prep
%setup -q -c -T

%build
mkdir -p .%{gemdir}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gemdir} \
  --force --rdoc \
  %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/

# Also ships as tar.gz with installer, so provide non-gem support
# thanks rubygem-json!
create_symlink_rec(){

ORIGBASEDIR=$1
TARGETBASEDIR=$2

## First calculate relative path of ORIGBASEDIR 
## from TARGETBASEDIR
TMPDIR=$TARGETBASEDIR
BACKDIR=
DOWNDIR=
num=0
nnum=0
while true
do
        num=$((num+1))
        TMPDIR=$(echo $TMPDIR | %{__sed} -e 's|/[^/][^/]*$||')
        DOWNDIR=$(echo $ORIGBASEDIR | %{__sed} -e "s|^$TMPDIR||")
        if [ x$DOWNDIR != x$ORIGBASEDIR ]
        then
                nnum=0
                while [ $nnum -lt $num ]
                do
                        BACKDIR="../$BACKDIR"
                        nnum=$((nnum+1))
                done
                break
        fi
done

RELBASEDIR=$( echo $BACKDIR/$DOWNDIR | %{__sed} -e 's|//*|/|g' )

## Next actually create symlink
pushd %{buildroot}/$ORIGBASEDIR
find . -type f | while read f
do
        DIRNAME=$(dirname $f)
        BACK2DIR=$(echo $DIRNAME | %{__sed} -e 's|/[^/][^/]*|/..|g')
        %{__mkdir_p} %{buildroot}${TARGETBASEDIR}/$DIRNAME
        LNNAME=$(echo $BACK2DIR/$RELBASEDIR/$f | \
                %{__sed} -e 's|^\./||' | %{__sed} -e 's|//|/|g' | \
                %{__sed} -e 's|/\./|/|' )
        %{__ln_s} -f $LNNAME %{buildroot}${TARGETBASEDIR}/$f
done
popd

}

create_symlink_rec %{geminstdir}/lib %{ruby_sitelib}

%clean
rm -rf %{buildroot}

%check
pushd .%{geminstdir}
rake test

%files
%defattr(-,root,root,-)
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README
%dir %{geminstdir}
%{geminstdir}/systemu.gemspec
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%{geminstdir}/samples
%{geminstdir}/test
%{geminstdir}/Rakefile
%{geminstdir}/README.erb
%{gemdir}/doc/%{gemname}-%{version}

%files -n ruby-%{gemname}
%defattr(-,root,root,-)
%{ruby_sitelib}/%{gemname}.rb

%changelog
* 
* Mon Oct 5 2009 Matthew Kent <mkent@magoazul.com> - 1.2.0-3
- Remove redundant doc Requires on rubygems.

* Tue Sep 29 2009 Matthew Kent <mkent@magoazul.com> - 1.2.0-2
- Include a copy of the license (#525988).
- Fix license (#525988).
- Use global over define (#525988).

* Wed Sep 23 2009 Matthew Kent <mkent@magoazul.com> - 1.2.0-1
- Initial package
