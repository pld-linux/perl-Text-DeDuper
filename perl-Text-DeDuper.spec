#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	DeDuper
Summary:	Text::DeDuper - near duplicates detection module
#Summary(pl.UTF-8):	
Name:		perl-Text-DeDuper
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b1211e3828a28418ca2436048a91752c
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Text-DeDuper/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Digest::MD4) >= 1.5
BuildRequires:	perl-Encode >= 2.12
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module uses the resemblance measure as proposed by Andrei Z. Broder at al
(http://www.ra.ethz.ch/CDstore/www6/Technical/Paper205/Paper205.html) to detect
similar (near-duplicate) documents based on their text.

Note of caution: The module only works correctly with languages where texts can
be tokenised to words by detecting alphabetical characters sequences. Therefore
it might not provide very good results for e.g. Chinese.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv t/pod{.t,.notused}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Text/*.pm
%{_mandir}/man3/*
