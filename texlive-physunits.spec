Name:		texlive-physunits
Version:	58728
Release:	1
Summary:	Macros for commonly used physical units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/physunits
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physunits.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physunits.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physunits.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a collection of macros to simplify using
physical units (e.g. m for meters, J for joules, etc.),
especially in math mode. All major SI units are included, as
well as some cgs units used in astronomy.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/physunits
%{_texmfdistdir}/tex/latex/physunits
%doc %{_texmfdistdir}/doc/latex/physunits

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
