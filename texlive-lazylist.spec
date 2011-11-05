# revision 17691
# category Package
# catalog-ctan /macros/latex/contrib/lazylist
# catalog-date 2006-12-30 10:59:01 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-lazylist
Version:	1.0a
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides a pile of lambda-calculus and list-
handling macros of an incredibly obtuse nature. The TUGboat
paper serves as a manual for the macros. This TeX code was
formally verified.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lazylist/lazylist.sty
%doc %{_texmfdistdir}/doc/latex/lazylist/lazylist.pdf
%doc %{_texmfdistdir}/doc/latex/lazylist/lazylist.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
