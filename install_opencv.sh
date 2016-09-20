brew install cmake pkg-config
brew install jpeg libpng libtiff openexr
brew install eigen tbb
cd ~
echo "Downloading OpenCV"
wget -O OpenCV-2.4.9.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.9/opencv-2.4.9.zip/download
echo "Installing OpenCV"
unzip OpenCV-2.4.9.zip
cd opencv-2.4.9
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_OPENGL=ON ..
make -j4
sudo make install
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages
echo "OpenCV installed”