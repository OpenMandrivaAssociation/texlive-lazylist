Name:		texlive-lazylist
Version:	17691
Release:	1
Summary:	Lists in TeX's "mouth"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lazylist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lazylist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lazylist.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a pile of lambda-calculus and list-
handling macros of an incredibly obtuse nature. The TUGboat
paper serves as a manual for the macros. This TeX code was
formally verified.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lazylist/lazylist.sty
%doc %{_texmfdistdir}/doc/latex/lazylist/lazylist.pdf
%doc %{_texmfdistdir}/doc/latex/lazylist/lazylist.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
