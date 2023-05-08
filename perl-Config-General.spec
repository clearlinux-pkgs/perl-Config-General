#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Config-General
Version  : 2.65
Release  : 48
URL      : https://cpan.metacpan.org/authors/id/T/TL/TLINDEN/Config-General-2.65.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TL/TLINDEN/Config-General-2.65.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libconfig-general-perl/libconfig-general-perl_2.63-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl Artistic-2.0 GPL-1.0
Requires: perl-Config-General-license = %{version}-%{release}
Requires: perl-Config-General-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Config::General - Generic Config Module
SYNOPSIS
use Config::General;
$conf = new Config::General(-ConfigFile => "myconfig.rc");
my %config = $conf->getall;

%package dev
Summary: dev components for the perl-Config-General package.
Group: Development
Provides: perl-Config-General-devel = %{version}-%{release}
Requires: perl-Config-General = %{version}-%{release}

%description dev
dev components for the perl-Config-General package.


%package license
Summary: license components for the perl-Config-General package.
Group: Default

%description license
license components for the perl-Config-General package.


%package perl
Summary: perl components for the perl-Config-General package.
Group: Default
Requires: perl-Config-General = %{version}-%{release}

%description perl
perl components for the perl-Config-General package.


%prep
%setup -q -n Config-General-2.65
cd %{_builddir}
tar xf %{_sourcedir}/libconfig-general-perl_2.63-1.debian.tar.xz
cd %{_builddir}/Config-General-2.65
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Config-General-2.65/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-General
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Config-General/d507aaceb6d11adba0cf2787a8afe267130cd751
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::General.3
/usr/share/man/man3/Config::General::Extended.3
/usr/share/man/man3/Config::General::Interpolated.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-General/d507aaceb6d11adba0cf2787a8afe267130cd751

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
