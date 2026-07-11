%global tl_name lazylist
%global tl_revision 17691

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Lists in TeXs mouth
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lazylist
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lazylist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lazylist.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package was developed to provide flexible lists, whose ordering can
be altered on the fly. The implementation involves a pile of lambda-
calculus and list-handling macros of an incredibly obtuse nature. The
TUGboat paper serves as a manual for the macros. Having said all of
which, confidence is enhanced by the knowledge that the TeX code was
formally verified.

