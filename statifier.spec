Summary:	Convert ELF dynamically linked execulables to "pseudo-static"
Summary(pl.UTF-8):	Konwersja dynamicznych binarek ELF do pseudo-statycznych
Name:		statifier
Version:	1.7.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/statifier/%{name}-%{version}.tar.gz
# Source0-md5:	858ab8e3dc3aacc23e69f681d671479f
URL:		http://statifier.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.213
%ifarch amd64
BuildRequires:	glibc-static(amd64)
# can be athlon after Ac
BuildRequires:	glibc-static(i686)
%endif
%ifarch ia32e
BuildRequires:	glibc-static(i686)
BuildRequires:	glibc-static(ia32e)
%endif
%ifarch x86_64
BuildRequires:	glibc-static(x86_64)
BuildRequires:	glibc-static(i686)
%endif
BuildRequires:	sed >= 4.0
Requires:	coreutils
Requires:	gawk
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statifier create from dynamically linked ELF executable and all it's
libraries (and all LD_PRELOAD libraries if any) one file. This file
can be copied and run on another machine without need to drag all it's
libraries.

%description -l pl.UTF-8
Statifier tworzy z dynamicznie zlinkowanej binarki ELF i wszystkich
jej bibliotek (oraz wszystkich bibliotek LD_PRELOAD jeżeli takie
występują) jeden plik. Ten plik może być kopiowany i uruchamiany na
innej maszynie bez potrzeby przenoszenia wszystkich bibliotek.

%prep
%setup -q

sed -i -e 's/-O2 -g/%{rpmcflags}/' src/Makefile

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO doc
%attr(755,root,root) %{_bindir}/statifier
%dir %{_prefix}/lib/statifier
%{_prefix}/lib/statifier/VERSION
%attr(755,root,root) %{_prefix}/lib/statifier/*.sh
%attr(755,root,root) %{_prefix}/lib/statifier/*.src
%attr(755,root,root) %{_prefix}/lib/statifier/elf_class
%ifarch %{ix86} %{x8664}
%dir %{_prefix}/lib/%{name}/32
%attr(755,root,root) %{_prefix}/lib/statifier/32/*
%endif
%ifarch %{x8664}
%dir %{_prefix}/lib/%{name}/64
%attr(755,root,root) %{_prefix}/lib/statifier/64/*
%endif
%{_mandir}/man1/%{name}.1*
