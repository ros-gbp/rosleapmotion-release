Name:           ros-jade-leap-motion
Version:        0.0.11
Release:        0%{?dist}
Summary:        ROS leap_motion package

Group:          Development/Libraries
License:        BSD
URL:            https://wiki.ros.org/leap_motion
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-camera-calibration-parsers
Requires:       ros-jade-camera-info-manager
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-transport
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslib
Requires:       ros-jade-rospack
Requires:       ros-jade-rospy
Requires:       ros-jade-std-msgs
Requires:       ros-jade-visualization-msgs
BuildRequires:  ros-jade-camera-calibration-parsers
BuildRequires:  ros-jade-camera-info-manager
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rospack
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-visualization-msgs

%description
ROS driver for the Leap Motion gesture sensor

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Jan 14 2017 Florian Lier <flier@techfak.uni-bielefeld.de> - 0.0.11-0
- Autogenerated by Bloom

* Sat Jun 18 2016 Florian Lier <flier@techfak.uni-bielefeld.de> - 0.0.10-0
- Autogenerated by Bloom

* Mon Dec 14 2015 Florian Lier <flier@techfak.uni-bielefeld.de> - 0.0.9-0
- Autogenerated by Bloom

