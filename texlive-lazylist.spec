# revision 17691
# category Package
# catalog-ctan /macros/latex/contrib/lazylist
# catalog-date 2006-12-30 10:59:01 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-lazylist
Version:	1.0a
Release:	7
Summary:	Lists in TeX's "mouth"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lazylist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lazylist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lazylist.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-2
+ Revision: 753208
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 718835
- texlive-lazylist
- texlive-lazylist
- texlive-lazylist
- texlive-lazylist

