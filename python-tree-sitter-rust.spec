Name:		python-tree-sitter-rust
Version:	0.24.2
Release:	1
Summary:	Tree-sitter rust grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-rust
Source0:	https://files.pythonhosted.org/packages/b7/87/75cbd22b927267d310f76cca1ab3c1d9d41035dfa3eb9cc95f96ee199440/tree_sitter_rust-0.24.2.tar.gz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for rust, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_rust-0.24.2

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_rust*
