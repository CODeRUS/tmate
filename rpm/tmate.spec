Name:           tmate
Version:        2.4.0
Release:        1%{?dist}
Group:          System/Utilities
Summary:        Instant terminal sharing
License:        MIT
Url:            http://tmate.io

Source0:        https://github.com/tmate-io/tmate/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  msgpack-devel >= 1.1.8
BuildRequires:  libssh-devel >= 0.8.4

%description
Tmate is a fork of tmux providing an instant pairing solution.

%prep
%setup -q  -n %{name}-%{version}/upstream

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/tmate
%{_mandir}/man1/tmate.1*