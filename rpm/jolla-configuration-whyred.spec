# Device variables including vendor & device (model)
%include rpm/header-whyred.inc

Name: jolla-configuration-%{device}
Summary: Jolla Configuration %{device}
Version: 1.3.1
Release: 0
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz

# Packages required for the device HW adaptation
%include rpm/jolla-hw-adaptation-whyred.inc

# General Jolla & Sailfish OS configuration packages
%include rpm/jolla-configuration-whyred.inc

%description
Meta-package to install packages for %{device} HW adaptation configurations
%files
