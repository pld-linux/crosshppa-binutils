Summary:	Cross HP Parisc GNU binary utility development utilities - binutils
Summary(es):	Utilitarios para desarrollo de binarios de la GNU - HP Parisc binutils
Summary(fr):	Utilitaires de développement binaire de GNU - HP Parisc binutils
Summary(pl):	Skro¶ne narzêdzia programistyczne GNU dla HP Parisc - binutils
Summary(pt_BR):	Utilitários para desenvolvimento de binários da GNU - HP Parisc binutils
Summary(tr):	GNU geliþtirme araçlarý - HP Parisc binutils
Name:		crosshppa-binutils
Version:	2.14.90.0.7
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.kernel.org/pub/linux/devel/binutils/binutils-%{version}.tar.bz2
# Source0-md5:	b5b1608f7308c487c0f3af8e4592a71a
URL:		http://sourceware.cygnus.com/binutils/
Prereq:		/sbin/ldconfig
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	perl-devel
BuildRequires:	bash
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		hppa-pld-linux
%define		arch		%{_prefix}/%{target}

%description
Binutils is a collection of binary utilities, including:
- ar - create, modify and extract from archives,
- nm - lists symbols from object files,
- objcopy - copy and translate object files,
- objdump - display information from object files,
- ranlib - generate an index for the contents of an archive,
- size - list the section sizes of an object or archive file,
- strings - list printable strings from files,
- strip - discard symbols,
- c++filt - a filter for demangling encoded C++ symbols,
- addr2line - convert addresses to file and line,
- nlmconv - convert object code into an NLM.

This package contains the cross version for HP Parisc.

%description -l pl
Pakiet binutils zawiera zestaw narzêdzi umo¿liwiaj±cych kompilacjê
programów. Znajduj± siê tutaj miêdzy innymi assembler, konsolidator
(linker), a tak¿e inne narzêdzia do manipulowania binarnymi plikami
programów i bibliotek.

Ten pakiet zawiera wersjê skro¶n± generuj±c± kod dla HP Parisc

%prep
%setup -q -n binutils-%{version}

%build
# ldscripts won't be generated properly if SHELL is not bash...
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
CONFIG_SHELL="/bin/bash" \
%ifarch sparc
sparc32 \
%endif
./configure \
	--disable-shared \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--target=%{target}

%{__make} tooldir=%{_prefix} EXEEXT="" all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{*dlltool,*nlmconv,*windres}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{target}-*
%dir %{arch}/bin
%attr(755,root,root) %{arch}/bin/*
%dir %{arch}/lib
%dir %{arch}/lib/*
%{_mandir}/man?/%{target}-*
