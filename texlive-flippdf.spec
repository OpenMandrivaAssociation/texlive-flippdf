%global tl_name flippdf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0b
Release:	%{tl_revision}.1
Summary:	Horizontal flipping of pages with pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/flippdf
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the production of a document with pages "mirrored".
This is sometimes required by publishers who want camera-ready documents
to be printed on transparent film (to be viewed from the "wrong" side).
The package only works with pdfLaTeX or LuaLaTeX in PDF output mode.
Package everypage is required on LaTeX releases before Fall 2020.

